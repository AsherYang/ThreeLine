package com.asher.threeline.aop;

import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;

import java.util.List;

import io.reactivex.Observable;
import io.reactivex.functions.Consumer;
import io.reactivex.functions.Predicate;
import io.realm.Realm;
import io.realm.RealmObject;

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
    @Around("skinFieldAnnotated()")
    public void doJointPoint(ProceedingJoinPoint joinPoint) throws Throwable {
        // 执行原方法
        joinPoint.proceed();
        final Realm realm = Realm.getDefaultInstance();
        Observable.fromArray(joinPoint.getArgs())
                .filter(new Predicate<Object>() {
                    @Override
                    public boolean test(Object obj) throws Exception {
                        return obj instanceof RealmObject || obj instanceof List;
                    }
                })
                .subscribe(new Consumer<Object>() {
                    @Override
                    public void accept(Object obj) throws Exception {
                        // 接收
                        realm.beginTransaction();
                        if (obj instanceof List) {
                            realm.copyToRealmOrUpdate((List) obj);
                        } else {
                            realm.copyToRealmOrUpdate((RealmObject) obj);
                        }
                        realm.commitTransaction();
                    }
                }, new Consumer<Throwable>() {
                    @Override
                    public void accept(Throwable throwable) throws Exception {
                        // 失败
                        throwable.printStackTrace();
                    }
                });

    }
}
