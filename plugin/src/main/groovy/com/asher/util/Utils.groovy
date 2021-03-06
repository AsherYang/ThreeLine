package com.asher.util

import javassist.ClassPool
import javassist.CtMethod

public class Utils {

    final static String SkinAnnotation = "com.asher.threeline.aop.annotation.Skin"
    final static String ThemeViewCollector = "com.asher.threeline.ui.theme.ThemeViewCollector"
    final static String ThemeHelper = "com.asher.threeline.ui.theme.ThemeHelper"
    final static String ITheme = "com.asher.threeline.ui.theme.ITheme"
    static def UPDATE_UI_ELEMENTS = 'updateUiElements'
    static def CHANGE_THEME = 'changeTheme'
    static def NOTIFY_UI_REFRESH = "notifyUiRefresh"
    static def ON_CREATE = "onCreate"
    static def ON_ACTIVITY_CREATE = "onActivityCreated"
    static def ON_DESTROY = 'onDestroy'
    static def ACTIVITY_CLASS = 'android.app.Activity'
    static def ADD_ACTIVITY = 'addActivity'
    static def HAS_CONTAIN_ACTIVITY = 'hasContainActivity'

    /**
     * 事先载入相关类
     * @param pool
     */
    static void importBaseClass(ClassPool pool) {
        pool.importPackage(SkinAnnotation)
        pool.importPackage("com.asher.debug.util.ClassTagUtil")
        pool.importPackage("android.util.Log")
        pool.importPackage("android.os.Bundle")
        pool.importPackage("android.os.Message")
        pool.importPackage("com.asher.threeline.ui.theme.ThemeHelper")
        pool.importPackage("com.asher.threeline.ui.theme.Theme")
        pool.importPackage("com.asher.threeline.ui.theme.ITheme")
        pool.importPackage("com.asher.threeline.ui.theme.ThemeViewCollector")
        pool.importPackage("com.asher.threeline.ui.main.MainView")
        pool.importPackage("java.util.ArrayList")
    }

    static String getSimpleName(CtMethod ctMethod) {
        def methodName = ctMethod.getName();
        return methodName.substring(
                methodName.lastIndexOf('.') + 1, methodName.length());
    }

    static String getClassName(int index, String filePath) {
        int end = filePath.length() - 6 // .class = 6
        return filePath.substring(index, end).replace('\\', '.').replace('/', '.')
    }

    static String getClassFileDir(String filePath) {
        return filePath.substring(0, filePath.lastIndexOf("\\"))
    }
}
