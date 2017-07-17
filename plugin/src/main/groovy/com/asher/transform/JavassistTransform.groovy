package com.asher.transform

import com.android.build.api.transform.*
import com.google.common.collect.Sets
import javassist.ClassPool
import org.apache.commons.io.FileUtils
import org.gradle.api.Project

class JavassistTransform extends Transform {

    Project project

    public JavassistTransform(Project project) {
        this.project = project
    }

    // 设定我们自定义的transform对应的Task名称
    @Override
    String getName() {
        return "ThreeLine"
    }

    // 指定输入类型，通过这里的设定，可以指定我们要处理的文件类型，
    // 这样确保其他类型的文件不会被传入
    @Override
    Set<QualifiedContent.ContentType> getInputTypes() {
        return Sets.immutableEnumSet(QualifiedContent.DefaultContentType.CLASSES)
    }

    // 指定transform的作用范围
    @Override
    Set<QualifiedContent.Scope> getScopes() {
        return Sets.immutableEnumSet(QualifiedContent.Scope.PROJECT, QualifiedContent.Scope.PROJECT_LOCAL_DEPS,
                QualifiedContent.Scope.SUB_PROJECTS, QualifiedContent.Scope.SUB_PROJECTS_LOCAL_DEPS,
                QualifiedContent.Scope.EXTERNAL_LIBRARIES)
    }

    @Override
    boolean isIncremental() {
        return false;
    }

    @Override
    void transform(TransformInvocation transformInvocation) throws TransformException, InterruptedException, IOException {
        // Transform的inputs有两种类型，一种是目录，一种是jar包，要分开遍历
        Collection<TransformInput> inputs = transformInvocation.getInputs()
        TransformOutputProvider tfOutputProvider = transformInvocation.getOutputProvider()
        inputs.each { TransformInput input ->
            // jar 包形式
            try {
                input.jarInputs.each {
                    // inject code
                    MyInject.injectDir(it.file.getAbsolutePath(), "com", project)
                    String outputFileName = it.name.replace(".jar", "") + "-" + it.file.path.hashCode()
                    def output = tfOutputProvider.getContentLocation(outputFileName, it.contentTypes, it.scopes, Format.JAR)
                    FileUtils.copyFile(it.file, output)
                }
            } catch (Exception e) {
                project.logger.error e.getMessage()
            }

            // 文件夹形式
            input.directoryInputs.each { DirectoryInput directoryInput ->
                // inject code
                // 文件夹里面包含的是我们手写的类，以及R.class|BuildConfig.class以及R$xxx.class等
                MyInject.injectDir(directoryInput.file.absolutePath, "com.asher.three", project)
                // 获取output目录
                def dest = tfOutputProvider.getContentLocation(directoryInput.name,
                        directoryInput.contentTypes, directoryInput.scopes, Format.DIRECTORY)

                // 将input的目录复制到output指定目录
                FileUtils.copyDirectory(directoryInput.file, dest)
            }
        }
        ClassPool.getDefault().clearImportedPackages()
        super.transform(transformInvocation)
    }

}