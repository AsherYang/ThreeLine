package com.asher.threeline.serve.net.content;

import com.asher.threeline.api.IGetDataHttp;
import com.asher.threeline.serve.data.content.IDbContentServe;

import dagger.Module;
import dagger.Provides;
import retrofit2.Retrofit;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 网络操作module
 */
@Module
public class NetContentServeModule {

    @Provides
    IGetDataHttp provideHttpService(Retrofit retrofit) {
        return retrofit.create(IGetDataHttp.class);
    }

    @Provides
    INetContentServe provideNetServe(IGetDataHttp dataHttp, IDbContentServe dbContentServe) {
        return new NetContentServeImpl(dataHttp, dbContentServe);
    }
}
