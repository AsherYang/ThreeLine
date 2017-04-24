package com.asher.helper

import javassist.CtClass
import javassist.bytecode.annotation.Annotation
import org.gradle.api.Project

public class ThemeViewInfo {

    Project project//保留当前工程的引用
    CtClass clazz//当前处理的class
    List<Annotation> annotations = new ArrayList<>()//带有Bus注解的注解列表
}