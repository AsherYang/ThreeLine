package com.asher.helper

import javassist.CtClass

// todo delete
public class ThemeViewInfo {
    private static final ThemeViewInfo instance = new ThemeViewInfo()
    private ThemeViewInfo() {

    }
    public static ThemeViewInfo getInstance() {
        return instance
    }

    List<CtClass> ctClasses = new ArrayList<>()  // 保存所有带注解的类
}