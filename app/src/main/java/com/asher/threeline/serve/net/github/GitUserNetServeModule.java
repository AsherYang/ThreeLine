package com.asher.threeline.serve.net.github;

import com.asher.threeline.api.IGetDataHttp;

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

    @Provides
    IGetDataHttp provideHttpService(Retrofit retrofit) {
        return retrofit.create(IGetDataHttp.class);
    }

    @Provides
    IGitHubNetServe provideGitHubNetServe(IGetDataHttp dataHttp) {
        return new GitHubNetServeImpl(dataHttp);
    }
}
