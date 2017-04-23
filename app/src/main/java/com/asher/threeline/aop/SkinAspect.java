package com.asher.threeline.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.After;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * realm aspect
 */
@Aspect
public class SkinAspect {

    //方法切入点
    @Pointcut("execution(@com.asher.threeline.aop.annotation.Skin * *(..))")
    public void skinFieldAnnotated() {
    }

    // 定义通知，织入代码
    @After("skinFieldAnnotated()")
    public void doJointPoint(ProceedingJoinPoint joinPoint) throws Throwable {
        // 执行原方法
        joinPoint.proceed();

    }
}
