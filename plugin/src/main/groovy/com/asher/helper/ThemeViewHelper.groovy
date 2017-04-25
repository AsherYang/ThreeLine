package com.asher.helper

import javassist.CtClass
import org.gradle.api.Project

public class ThemeViewHelper {

    static void addClass(CtClass ctClass, Project project) {
        ThemeViewInfo themeViewInfo = ThemeViewInfo.getInstance()
        themeViewInfo.ctClasses.add(ctClass)
        project.logger.error "-----add $ctClass.name ------"
    }

    static String invokeRefreshUiCmd(Project project) {
        ThemeViewInfo themeViewInfo = ThemeViewInfo.getInstance()
        project.logger.error themeViewInfo.toString()
        List<CtClass> ctClassList = themeViewInfo.getCtClasses()
        project.logger.error "----- ctClassList $ctClassList.size ------"
        if (null == ctClassList || ctClassList.isEmpty()) {
            return null
        }
        // invoke must use java.lang.reflect, because of javassist don`t deal it @see javassist api
        StringBuffer buffer2 = new StringBuffer()
        for (CtClass ctClazz : ctClassList) {
            // invoke updateUiElements
            try {
                // 解冻
                if (ctClazz.isFrozen()) {
                    ctClazz.defrost()
                }
                project.logger.error "----- cz $ctClazz.name ------"
                Class clazz = ctClazz.toClass()
                project.logger.error "-----cc ------ ------"
                buffer2.append("($clazz).updateUiElements()")
                project.logger.error "----- ctClassList clazz ------"
            } catch (Exception e) {
                // do nothing
                project.logger.error e.getMessage()
            }
        }
        return buffer2.toString()
    }
}