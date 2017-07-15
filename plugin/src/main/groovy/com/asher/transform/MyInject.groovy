package com.asher.transform

import com.asher.util.Utils
import javassist.*
import org.gradle.api.Project

import java.lang.annotation.Annotation

/**
 * use javassist
 *
 * http://jboss-javassist.github.io/javassist/tutorial/tutorial2.html
 */
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
                        boolean hasAnnotationed = false
                        for (CtField ctField : c.getDeclaredFields()) {
                            for (Annotation annotation : ctField.getAnnotations()) {
                                String annoName = annotation.annotationType().canonicalName
                                if (annoName.equals(Utils.SkinAnnotation)) {
                                    hasAnnotationed = true
                                    generateLightTheme(annotation, c, ctField)
                                    generateDarkTheme(annotation, c, ctField)
                                    generateITheme(path)
                                    // after generateITheme
                                    modifyToImplITheme(c, path)
                                    modifyUpdateUiElementMethod(c)
                                    // after modifyUpdateUiElementMethod
                                    generateThemeViewCollector(c, path, project)
                                    // after generateThemeViewCollector
                                    modifyActivityLife(c, path, project);
                                }
                            }
                        }
                        if (hasAnnotationed) {
                            modifyChangeThemeMethodToNotify(c, project)
                            c.writeFile(path)
                        }
                        //用完一定记得要卸载，否则pool里的永远是旧的代码
                        c.detach()
                    }
                }
            }

        }
    }

    /**
     * generate Light Theme to activity
     * @param annotation
     * @param ctClass
     * @param ctField
     */
    static void generateLightTheme(Annotation annotation, CtClass ctClass, CtField ctField) {
        if (ctClass.isFrozen()) {
            ctClass.defrost()
        }
        //获取注解的值
        // set light background and color
        int backgroundDrawableResId = annotation.lightBackgroundDrawableResId()
        int backgroundColorResId = annotation.lightBackgroundColorResId()
        int textColorResId = annotation.lightTextColorResId()
        CtMethod lightMethod;
        try {
            // 找到就使用原来的setLightTheme()方法
            lightMethod = ctClass.getDeclaredMethod("setLightTheme");
            if (backgroundDrawableResId != -1) {
                lightMethod.insertBefore("($ctField.name).setBackgroundDrawable(getResources().getDrawable($backgroundDrawableResId));\n")
            } else if (backgroundColorResId != -1) {
                lightMethod.insertBefore("($ctField.name).setBackgroundColor(getResources().getColor($backgroundColorResId));\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                lightMethod.insertBefore("($ctField.name).setTextColor(getResources().getColor($textColorResId));\n")
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
            if (backgroundDrawableResId != -1) {
                buffer2.append("($ctField.name).setBackgroundDrawable(getResources().getDrawable($backgroundDrawableResId));\n")
            } else if (backgroundColorResId != -1) {
                buffer2.append("($ctField.name).setBackgroundColor(getResources().getColor($backgroundColorResId));\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                buffer2.append("($ctField.name).setTextColor(getResources().getColor($textColorResId));\n")
            }
            buffer2.append("}");
            lightMethod.setBody(buffer2.toString());
            ctClass.addMethod(lightMethod);
        }
    }

    /**
     * generate dark Theme to activity
     * @param annotation
     * @param ctClass
     * @param ctField
     */
    static void generateDarkTheme(Annotation annotation, CtClass ctClass, CtField ctField) {
        if (ctClass.isFrozen()) {
            ctClass.defrost()
        }
        //获取注解的值
        // set dark background and color
        int backgroundDrawableResId = annotation.darkBackgroundDrawableResId()
        int backgroundColorResId = annotation.darkBackgroundColorResId()
        int textColorResId = annotation.darkTextColorResId()
        CtMethod darkMethod;
        try {
            // 找到就使用原来的setLightTheme()方法
            darkMethod = ctClass.getDeclaredMethod("setDarkTheme");
            if (backgroundDrawableResId != -1) {
                darkMethod.insertBefore("($ctField.name).setBackgroundDrawable(getResources().getDrawable($backgroundDrawableResId));\n")
            } else if (backgroundColorResId != -1) {
                darkMethod.insertBefore("($ctField.name).setBackgroundColor(getResources().getColor($backgroundColorResId));\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                darkMethod.insertBefore("($ctField.name).setTextColor(getResources().getColor($textColorResId));\n")
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
            if (backgroundDrawableResId != -1) {
                buffer2.append("($ctField.name).setBackgroundDrawable(getResources().getDrawable($backgroundDrawableResId));\n")
            } else if (backgroundColorResId != -1) {
                buffer2.append("($ctField.name).setBackgroundColor(getResources().getColor($backgroundColorResId));\n")
            }
            if (textColorResId != -1 && ctField.fieldInfo.toString().contains("TextView")) {
                buffer2.append("($ctField.name).setTextColor(getResources().getColor($textColorResId));\n")
            }
            buffer2.append("}");
            darkMethod.setBody(buffer2.toString());
            ctClass.addMethod(darkMethod);
        }
    }

    /**
     * modify updateUiElements method to activity
     * @param ctClass
     */
    static void modifyUpdateUiElementMethod(CtClass ctClass) {
        if (ctClass.isFrozen()) {
            ctClass.defrost()
        }
        StringBuffer buffer2 = new StringBuffer()
        // method/constructor body must be surrounded by {}
        buffer2.append("{");
        buffer2.append("Theme theme = ThemeHelper.getBaseTheme(this);\n")
//        buffer2.append("Log.i(\"TAG\", \"Theme=\" + theme);\n")
        buffer2.append("if (theme == Theme.DARK) {\n")
        buffer2.append("    setDarkTheme();\n")
        buffer2.append("} else {\n")
        buffer2.append("    setLightTheme();\n")
        buffer2.append("}");
        buffer2.append("}");
        CtMethod updateUiElementMethod;
        try {
            updateUiElementMethod = ctClass.getDeclaredMethod(Utils.UPDATE_UI_ELEMENTS);
            updateUiElementMethod.insertBefore(buffer2.toString())
        } catch (NotFoundException e) {
            // do nothing
        }

        if (null == updateUiElementMethod) {
            // 没有找到就创建一个
            //添加自定义方法
            updateUiElementMethod = new CtMethod(CtClass.voidType, Utils.UPDATE_UI_ELEMENTS,
                    null, ctClass);
            //为自定义方法设置修饰符
            updateUiElementMethod.setModifiers(Modifier.PUBLIC);
            //为自定义方法设置函数体
            updateUiElementMethod.setBody(buffer2.toString());
            ctClass.addMethod(updateUiElementMethod);
        }
    }

    /**
     * modify changeTheme method to notify all activity update
     *
     * modify ThemeHelper class
     */
    static void modifyChangeThemeMethodToNotify(CtClass ctClass, Project project) {
        if (!Utils.ThemeHelper.equals(ctClass.name)) {
            return
        }
        if (ctClass.isFrozen()) {
            ctClass.defrost()
        }
        CtMethod notifyUiMethod
        CtMethod changeThemeMethod
        try {
            notifyUiMethod = ctClass.getDeclaredMethod(Utils.NOTIFY_UI_REFRESH)
        } catch (Exception e) {
            // do nothing
        }
        try {
            changeThemeMethod = ctClass.getDeclaredMethod(Utils.CHANGE_THEME)
        } catch (Exception e1) {
            // do nothing
        }

        // 没有就创建
        if (null == changeThemeMethod) {
            changeThemeMethod = CtMethod.make("public void changeTheme(Theme toTheme) {\n" +
                    "setBaseTheme(toTheme);\n}", ctClass)
            ctClass.addMethod(changeThemeMethod)
        }

        if (null == notifyUiMethod) {
            notifyUiMethod = CtMethod.make("public void notifyUiRefresh() {\n" +
                    "ThemeViewCollector.getInstance().themeChanged();\n}", ctClass)
            ctClass.addMethod(notifyUiMethod)
            // insert into changeThemeMethod
            changeThemeMethod.insertAfter("notifyUiRefresh();")
        }
    }

    /**
     * generate ThemeViewCollector class
     * the ThemeViewCollector class possess the activity which annotation by @skin
     *
     * @param ctClassWithSkin
     * @param path
     * @param project
     */
    static void generateThemeViewCollector(CtClass ctClassWithSkin, String path, Project project) {
        if (ctClassWithSkin.isFrozen()) {
            ctClassWithSkin.defrost()
        }
        CtClass themeViewCtClass
        CtMethod instanceMethod
        try {
            themeViewCtClass = pool.get(Utils.ThemeViewCollector)
            instanceMethod = themeViewCtClass.getDeclaredMethod("getInstance")
        } catch (Exception e) {
            // do nothing
        }
        // 没有ThemeViewCollector 类就新建
        if (null == instanceMethod) {
            themeViewCtClass = pool.makeClass(Utils.ThemeViewCollector)
            // create fields
            CtField ctF1 = CtField.make("private static ThemeViewCollector instance;\n", themeViewCtClass)
            // List 方式需要使用这种pool.get()方式，因为javassist由低版本Java改造。没有List泛型等高级特性。
            // 故需要手动引入List, Java编译器正常编译源码后List里面也是存Object，然后转换的，
            // 所以这里我们泛型也可以是Object默认。然后在使用时进行强转
            CtClass arrListClazz = ClassPool.getDefault().get("java.util.ArrayList");
            CtField ctF2 = new CtField(arrListClazz, "mList", themeViewCtClass);
            ctF2.setModifiers(Modifier.PRIVATE)
            themeViewCtClass.addField(ctF1)
            themeViewCtClass.addField(ctF2)

            // create constructor ， 本来想传无参，但是发现new CtClass[] {} 编译不了，就随便传一个int 类型算了
            CtClass[] param = CtClass.intType;
            CtConstructor constructor = new CtConstructor(param, themeViewCtClass)
            constructor.setBody("{mList = new ArrayList();}")
            constructor.setModifiers(Modifier.PRIVATE)
            themeViewCtClass.addConstructor(constructor)
            // create methods
            CtMethod ctM1 = CtMethod.make("public static ThemeViewCollector getInstance() { " +
                    "if(instance == null) {instance = new ThemeViewCollector(1);} return instance;}",
                    themeViewCtClass)
            themeViewCtClass.addMethod(ctM1)
            CtMethod ctM2 = CtMethod.make("public void addThemeClass(ITheme themeClass) {\n " +
                    "if (!mList.contains(themeClass)) {\n mList.add(themeClass);\n}}",
                    themeViewCtClass)
            themeViewCtClass.addMethod(ctM2)
            CtMethod ctM3 = CtMethod.make("public void removeThemeClass(ITheme themeClass) {\n " +
                    "mList.remove(themeClass);}",
                    themeViewCtClass)
            themeViewCtClass.addMethod(ctM3)
            // 写if 判断逻辑,尽量使用正向逻辑,比如 !isEmpty(), 因为编译器编译后class就是这个逻辑
            // 同时由于javassist 使用的是由低版本Java(1.4)改造。导致很多新功能不可用。比如增强for循环,不支持范型等,需要自己强制转换。
            // 使用增强for循环,会造成编译不过,提示缺少";",其实是for循环条件导致
            String themeMethodSrc = "public void themeChanged() { if(null != mList" +
                    "&& !mList.isEmpty()) {\n for(int i = 0; i < mList.size(); i++) { Object obj = mList.get(i); \n " +
                    "if(obj instanceof ITheme) {((ITheme)obj).updateUiElements();}}}}"
            CtMethod ctM4 = CtMethod.make(themeMethodSrc, themeViewCtClass)
            themeViewCtClass.addMethod(ctM4)

            // write file
            project.logger.error "---- create themeViewCollector $path"
            themeViewCtClass.writeFile(path)
        }

        if (null != themeViewCtClass && themeViewCtClass.isFrozen()) {
            themeViewCtClass.defrost()
        }

    }

    /**
     * modify activity life method
     *
     * @param ctClassWithSkin
     * @param path
     */
    static void modifyActivityLife(CtClass ctClassWithSkin, String path, Project project) {
        if (ctClassWithSkin.isFrozen()) {
            ctClassWithSkin.defrost()
        }

        CtClass activityClazz = pool.get(Utils.ACTIVITY_CLASS)
        if (!ctClassWithSkin.subclassOf(activityClazz)) {
            return
        }
        CtMethod onCreateMethod = ctClassWithSkin.getDeclaredMethod(Utils.ON_CREATE)
        // insert add activity to ThemeViewCollector
        onCreateMethod.insertAfter("ThemeViewCollector.getInstance().addThemeClass(this);\n")
        // 同时刷新一下，设置第一次加载默认的主题
        onCreateMethod.insertAfter("updateUiElements();\n")

        CtMethod onDestroyMethod
        try {
            onDestroyMethod = ctClassWithSkin.getDeclaredMethod(Utils.ON_DESTROY)
        } catch (Exception e) {
            // do nothing
        }
        if (null == onDestroyMethod) {
            // 没有就新建
            // create methods
            onDestroyMethod = CtMethod.make("protected void onDestroy() {super.onDestroy();}", ctClassWithSkin)
            ctClassWithSkin.addMethod(onDestroyMethod)
        }
        // onDestroy 时释放,防止内存泄漏
        onDestroyMethod.insertAfter("ThemeViewCollector.getInstance().removeThemeClass(this);\n")
        ctClassWithSkin.writeFile(path)
    }

    /**
     * generate ITheme interface
     *
     * public interface ITheme {
     *    void updateUiElements();
     * }
     * @param path
     * @param project
     */
    static void generateITheme(String path) {
        CtClass iThemeInterface
        CtMethod updateUiElementMethod
        try {
            iThemeInterface = pool.get(Utils.ITheme)
            updateUiElementMethod = iThemeInterface.getDeclaredMethod(Utils.UPDATE_UI_ELEMENTS)
        } catch (Exception e) {
            // do nothing
        }

        // 没有ITheme 类就新建
        if (null == updateUiElementMethod) {
            iThemeInterface = pool.makeInterface(Utils.ITheme)
            updateUiElementMethod = CtMethod.make("void updateUiElements();", iThemeInterface)
            iThemeInterface.addMethod(updateUiElementMethod)
            // write file
            iThemeInterface.writeFile(path)
        }
    }

    /**
     * modify class to implements ITheme
     * @param ctClass
     */
    static void modifyToImplITheme(CtClass ctClass, String path) {
        if (ctClass.isFrozen()) {
            ctClass.defrost()
        }
        CtClass iThemeInterface = pool.get(Utils.ITheme)
        if (iThemeInterface.isFrozen()) {
            iThemeInterface.defrost()
        }
        ctClass.addInterface(iThemeInterface)
        ctClass.writeFile(path)
    }
}