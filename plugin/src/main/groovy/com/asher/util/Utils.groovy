package com.asher.util

import javassist.ClassPool
import javassist.CtMethod
import org.gradle.api.Project

public class Utils {

    final static String SkinAnnotation = "com.asher.threeline.aop.annotation.Skin"
    static def ON_CREATE = ['onCreate', "onActivityCreated"] as String[]
    static def ON_DESTROY = 'onDestroy'

    /**
     * 事先载入相关类
     * @param pool
     */
    static void importBaseClass(ClassPool pool) {
        pool.importPackage(SkinAnnotation)
        pool.importPackage("com.asher.debug.util.ClassTagUtil")
        pool.importPackage("android.util.Log")
        pool.importPackage("android.os.Bundle")
        pool.importPackage("com.base.event.OkBus")
        pool.importPackage("com.base.event.Event")
        pool.importPackage("android.os.Message")
    }

    static String getSimpleName(CtMethod ctMethod, Project project) {
        def methodName = ctMethod.getName();
        project.logger.error "------ methodName = $methodName"
        return methodName.substring(
                methodName.lastIndexOf('.') + 1, methodName.length());
    }

    static String getClassName(int index, String filePath) {
        int end = filePath.length() - 6 // .class = 6
        return filePath.substring(index, end).replace('\\', '.').replace('/', '.')
    }
}
