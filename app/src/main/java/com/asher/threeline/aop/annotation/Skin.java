package com.asher.threeline.aop.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

/**
 * Created by ouyangfan on 17/4/22.
 * <p>
 * 换肤注解
 */
@Retention(RetentionPolicy.CLASS)
@Target(ElementType.FIELD)
public @interface Skin {

    /**
     * 日间模式
     */
    int lightBackgroundColorResId() default -1;

    int lightTextColorResId() default -1;

    /**
     * 夜间模式
     */
    int darkBackgroundColorResId() default -1;

    int darkTextColorResId() default -1;
}
