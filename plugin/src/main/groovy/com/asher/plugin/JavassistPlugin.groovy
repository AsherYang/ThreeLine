package com.asher.plugin

import com.asher.transform.JavassistTransform
import org.gradle.api.Plugin
import org.gradle.api.Project

class JavassistPlugin implements Plugin<Project> {

    @Override
    void apply(Project project) {
        def log = project.logger;
        log.error "===================="
        log.error " 正在修改class !"
        log.error "===================="
        // to find why not use
        project.android.registerTransform(new JavassistTransform(project))
    }
}