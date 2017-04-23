package com.asher.transform

import com.asher.util.Utils
import javassist.*
import javassist.bytecode.annotation.StringMemberValue
import org.gradle.api.Project

import java.lang.annotation.Annotation

public class MyInject {
    public final static ClassPool pool = ClassPool.getDefault();

    public static void injectDir(String path, String packageName, Project project) {
        pool.appendClassPath(path)

        // project.android.bootClassPath 加入android.jar，否则找不到android相关的所有类
        pool.appendClassPath(project.android.bootClasspath[0].toString())
        Utils.importBaseClass(pool);
        File dir = new File(path)
        if (dir.isDirectory()) {
            dir.eachFileRecurse { File file ->
                String filePath = file.absolutePath
                // 确保当前文件是class文件，并且不是系统自动生成的class文件
                if (filePath.endsWith(".class") && !filePath.contains('R$') && !filePath.contains('$') // 代理类
                        && !filePath.contains('R.class') && !filePath.contains('BuildConfig.class')) {
                    // 判断当前目录是否是在我们的应用包里面
                    int index = filePath.indexOf(packageName)
                    boolean isMyPackage = (index != -1)
                    if (isMyPackage) {
                        String className = Utils.getClassName(index, filePath)
                        CtClass c = pool.getCtClass(className)
                        c.stopPruning(true)
                        if (c.isFrozen()) {
                            c.defrost()
                        }
                        for (CtField ctField : c.getDeclaredFields()) {
                            for (Annotation annotation : ctField.getAnnotations()) {
                                String annoName = annotation.annotationType().canonicalName
                                if (annoName.equals(Utils.SkinAnnotation)) {
                                    generateLightTheme(annotation, c, ctField, project)
                                    generateDarkTheme(annotation, c, ctField)
                                }
                            }
                        }
                        /*for (CtMethod ctMethod : c.getDeclaredMethods()) {
                            String methodName = Utils.getSimpleName(ctMethod, project);
                            for (Annotation mAnnotation : ctMethod.getAnnotations()) {
                                String annoName = mAnnotation.annotationType().canonicalName
                                project.logger.error "----> annoName = $annoName"
                                if (mAnnotation.annotationType().canonicalName.equals(Utils.SkinAnnotation)) {
                                    project.logger.error "==== @Time 方法正在修改 ===="
                                    String insertStr = "{Log.i(\"-- TAG --\", \"Time插入代码成功\");}\n"
                                    ctMethod.insertBefore(insertStr)
                                }
                            }
                            if (Utils.ON_CREATE.contains(methodName)) {
                                project.logger.error "==== onCreate 方法正在修改 ===="
                                ctMethod.insertBefore("{Log.i(\"-- TAG --\", \"onCreate插入代码成功\");}\n")
                            }
                        }*/
//                        c.writeFile()
                        project.logger.error "path -> $path"
                        c.writeFile(path)
                        //用完一定记得要卸载，否则pool里的永远是旧的代码
                        c.detach()
                    }
                }

            }
        }
    }

    /**
     * generate Light Theme
     * @param annotation
     * @param ctClass
     * @param ctField
     */
    private static void generateLightTheme(Annotation annotation, CtClass ctClass, CtField ctField, Project project) {
        //获取注解的值
        // TODO: 17/4/23 set default background and color
        int backgroundColorResId = annotation.lightBackgroundColorResId()
        int colorResId =((StringMemberValue) annotation.getMemberValue("lightColorResId")).getValue() ;
        project.logger.error "backgroundResId = $backgroundColorResId, colorResId = $colorResId"
        //添加自定义方法
        CtMethod ctMethod = new CtMethod(CtClass.voidType, "set"+upperFirstCase(ctField.name)+"Light",
                new CtClass[""]{}, ctClass);
        //为自定义方法设置修饰符
        ctMethod.setModifiers(Modifier.PUBLIC);
        //为自定义方法设置函数体
        StringBuffer buffer2 = new StringBuffer();
        // todo 这里的colorResId还要想一下,并不一定是TextColor
        buffer2.append("{\nctField.name.setBackgroundColor($backgroundColorResId);\n")
                .append("ctField.name.setTextColor($colorResId);\n")
                .append("System.out.println(eno);\n")
                .append("System.out.println(\"over!\");\n")
                .append("}");
        ctMethod.setBody(buffer2.toString());
        ctClass.addMethod(ctMethod);
    }

    /**
     * generate dark Theme
     * @param annotation
     * @param ctClass
     * @param ctField
     */
    private static void generateDarkTheme(Annotation annotation, CtClass ctClass, CtField ctField) {
        // todo generate dark theme
        // TODO: 17/4/23 generate the night background and color, but not called
    }


    private static String upperFirstCase(String str) {
        char[] ch = str.toCharArray();
        if (ch[0] >= 'a' && ch[0] <= 'z') {
            ch[0] = (char) (ch[0] - 32);
        }
        return String.valueOf(ch);
    }
}