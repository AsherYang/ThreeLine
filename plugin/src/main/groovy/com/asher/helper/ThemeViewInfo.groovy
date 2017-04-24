package com.asher.helper

import com.asher.util.Utils
import javassist.ClassPool
import javassist.CtClass
import javassist.CtMethod
import org.gradle.api.Project

public class ThemeViewInfo {

    public final static ClassPool pool = ClassPool.getDefault()
    private Project project

    public ThemeViewInfo(Project project) {
        this.project = project
    }

    public void invokeAddActivity(CtClass ctClazz) {
        project.logger.error "----> themeViewInfo add ======"
        CtClass c = pool.getCtClass(Utils.ThemeViewCollector)
        CtMethod m = c.getDeclaredMethod(Utils.ADD_ACTIVITY)
        project.logger.error "----> themeViewInfo $m.name ======"
        c.invokeMethod(m.name, ctClazz.simpleName)
//        project.logger.error "----> theme = $ctMethod.getName()"
        /*for (CtMethod ctMethod : c.getDeclaredMethods()) {
            String methodName = Utils.getSimpleName(ctMethod, project);
            if (Utils.ADD_ACTIVITY.contains(methodName)) {
                c.invokeMethod(ctMethod.name, ctClass)
                project.logger.error "----> theme = $ctMethod.getName()"
            }
        }*/
    }

    public boolean invokeHasContainActivity(CtClass ctClazz) {
        CtClass c = pool.getCtClass(Utils.ThemeViewCollector)
        project.logger.error "---->444 $c.name,  $ctClazz.simpleName"
        project.logger.error "---->555 $ctClazz.interfaces"
        if (!ctClazz.interfaces.toArrayString().contains('ThemeActivity')) {
            return false
        }
        CtMethod m = c.getDeclaredMethod(Utils.HAS_CONTAIN_ACTIVITY)
        project.logger.error "---->m $m"
        // todo error msg how to invoke method ?
        boolean result = c.invokeMethod(m.name, ctClazz.simpleName)
        /*for (CtMethod ctMethod : c.getDeclaredMethods()) {
            project.logger.error "---->ctMethod $ctMethod"
            String methodName = Utils.getSimpleName(ctMethod, project);
            if (Utils.HAS_CONTAIN_ACTIVITY.contains(methodName)) {
                CtClass[] param = new CtClass[1];
                param[0] = pool.get(className)
                param[0] = pool.get("java.security.PublicKey") ;
                result = c.invokeMethod(methodName, param)
                project.logger.error "----> theme = $result"
            }
        }*/

        project.logger.error "----> result = $result"
        return result
    }
}