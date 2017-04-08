package com.asher.threeline.ui.github;

import com.asher.threeline.serve.net.github.IGitHubNetServe;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 2017/4/8.
 * <p>
 * github module
 */
@Module
public class GithubModule {

    private GithubView githubView;

    public GithubModule(GithubView githubView) {
        this.githubView = githubView;
    }

    @Provides
    GithubView provideGithubView() {
        return githubView;
    }

    @Provides
    GithubPresenter provideGithubPresenter(IGitHubNetServe gitHubNetServe) {
        return new GithubPresenterImpl(githubView, gitHubNetServe);
    }

}
