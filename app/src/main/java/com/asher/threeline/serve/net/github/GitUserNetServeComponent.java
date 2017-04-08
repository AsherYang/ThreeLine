package com.asher.threeline.serve.net.github;

import com.asher.threeline.AppComponent;
import com.asher.threeline.AppScope;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * github net server component
 */
@AppScope
@Component(
        dependencies = {AppComponent.class},
        modules = {GitUserNetServeModule.class}
)
public interface GitUserNetServeComponent {

    IGitHubNetServe provideGitHubNetServe();
}
