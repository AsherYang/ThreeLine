package com.asher.threeline.serve.net.github;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * github net server component
 */
@Component(
        modules = {GitUserNetServeModule.class}
)
public interface GitUserNetServeComponent {

    IGitHubNetServe provideGitHubNetServe();
}
