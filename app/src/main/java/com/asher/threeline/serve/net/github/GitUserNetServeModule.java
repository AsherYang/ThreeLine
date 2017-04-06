package com.asher.threeline.serve.net.github;

import com.asher.threeline.api.IGetDataHttp;

import javax.inject.Inject;

import dagger.Module;
import dagger.Provides;
import retrofit2.Retrofit;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 网络操作module
 */
@Module
public class GitUserNetServeModule {

    @Inject
    Retrofit mRetrofit;

    @Provides
    IGetDataHttp provideHttpService() {
        return mRetrofit.create(IGetDataHttp.class);
    }

    @Provides
    IGitHubNetServe provideGitHubNetServe() {
        return new GitHubNetServeImpl();
    }
}
