package com.asher.transform

import com.asher.util.Utils
import javassist.*
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
                                    generateLightTheme(annotation, c, ctField)
                                    generateDarkTheme(annotation, c, ctField)
                                    ThemeViewCollector.getInstance().addActivity($c.simpleName);
                                }
                            }
                        }
                        // updateUiElements
                        project.logger.error "----> 11 = $c.simpleName"
                        if (ThemeViewCollector.getInstance().hasContainActivity($c.simpleName)) {
                            project.logger.error "----> annoName = $c.simpleName"
                            for (CtMethod ctMethod : c.getDeclaredMethods()) {
                                String methodName = Utils.getSimpleName(ctMethod, project);
                                /* for (Annotation mAnnotation : ctMethod.getAnnotations()) {
                                     String annoName = mAnnotation.annotationType().canonicalName
                                     project.logger.error "----> annoName = $annoName"
                                     if (mAnnotation.annotationType().canonicalName.equals(Utils.SkinAnnotation)) {
                                         project.logger.error "==== @Time 方法正在修改 ===="
                                         String insertStr = "{Log.i(\"-- TAG --\", \"Time插入代码成功\");}\n"
                                         ctMethod.insertBefore(insertStr)
                                     }
                                 }*/
                                if (Utils.UPDATE_UI_ELEMENTS.contains(methodName)) {
                                    project.logger.error "==== updateUiElements 方法正在修改 ===="
                                    StringBuffer buffer2 = new StringBuffer();
                                    buffer2.append("Theme theme = ThemeHelper.getBaseTheme(this);\n")
                                    buffer2.append("Log.i(\"TAG\", \"Theme=\" + theme);\n")
                                    buffer2.append("if (theme == Theme.DARK) {\n")
                                    buffer2.append("    setDarkTheme();\n")
                                    buffer2.append("} else {\n")
                                    buffer2.append("    setLightTheme();\n")
                                    buffer2.append("}");
                                    ctMethod.insertBefore(buffer2.toString())
                                }
                            }
                        }

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
    private
    static void generateLightTheme(Annotation annotation, CtClass ctClass, CtField ctField) {
        //获取注解的值
        // set light background and color
        int backgroundColorResId = annotation.lightBackgroundColorResId()
        int textColorResId = annotation.lightTextColorResId()
        CtMethod lightMethod;
        try {
            // 找到就使用原来的setLightTheme()方法
            lightMethod = ctClass.getDeclaredMethod("setLightTheme");
            if (backgroundColorResId != -1) {
                lightMethod.insertBefore("($ctField.name).setBackgroundColor($backgroundColorResId);\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                lightMethod.insertBefore("($ctField.name).setTextColor($textColorResId);\n")
            }
        } catch (NotFoundException e) {
            // do nothing
        }
        if (null == lightMethod) {
            // 没有找到就创建一个
            //添加自定义方法
            lightMethod = new CtMethod(CtClass.voidType, "setLightTheme",
                    null, ctClass);
            //为自定义方法设置修饰符
            lightMethod.setModifiers(Modifier.PUBLIC);
            //为自定义方法设置函数体
            StringBuffer buffer2 = new StringBuffer();
            buffer2.append("{\n ");
            if (backgroundColorResId != -1) {
                buffer2.append("($ctField.name).setBackgroundColor($backgroundColorResId);\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                buffer2.append("($ctField.name).setTextColor($textColorResId);\n")
            }
            buffer2.append("}");
            lightMethod.setBody(buffer2.toString());
            ctClass.addMethod(lightMethod);
        }
    }

    /**
     * generate dark Theme
     * @param annotation
     * @param ctClass
     * @param ctField
     */
    private static void generateDarkTheme(Annotation annotation, CtClass ctClass, CtField ctField) {
        //获取注解的值
        // set light background and color
        int backgroundColorResId = annotation.darkBackgroundColorResId()
        int textColorResId = annotation.darkTextColorResId()
        CtMethod darkMethod;
        try {
            // 找到就使用原来的setLightTheme()方法
            darkMethod = ctClass.getDeclaredMethod("setDarkTheme");
            if (backgroundColorResId != -1) {
                darkMethod.insertBefore("($ctField.name).setBackgroundColor($backgroundColorResId);\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                darkMethod.insertBefore("($ctField.name).setTextColor($textColorResId);\n")
            }
        } catch (NotFoundException e) {
            // do nothing
        }
        if (null == darkMethod) {
            // 没有找到就创建一个
            //添加自定义方法
            darkMethod = new CtMethod(CtClass.voidType, "setDarkTheme",
                    null, ctClass);
            //为自定义方法设置修饰符
            darkMethod.setModifiers(Modifier.PUBLIC);
            //为自定义方法设置函数体
            StringBuffer buffer2 = new StringBuffer();
            buffer2.append("{\n ");
            if (backgroundColorResId != -1) {
                buffer2.append("($ctField.name).setBackgroundColor($backgroundColorResId);\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                buffer2.append("($ctField.name).setTextColor($textColorResId);\n")
            }
            buffer2.append("}");
            darkMethod.setBody(buffer2.toString());
            ctClass.addMethod(darkMethod);
        }
    }
}