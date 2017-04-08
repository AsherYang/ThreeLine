package com.asher.threeline.ui.github;

import com.asher.threeline.ActivityScope;
import com.asher.threeline.serve.net.github.GitUserNetServeComponent;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/8.
 * <p>
 * github component
 */
@ActivityScope
@Component(
        dependencies = {GitUserNetServeComponent.class},
        modules = {GithubModule.class}
)
public interface GithubComponent {

    void inject(GithubActivity activity);
}
