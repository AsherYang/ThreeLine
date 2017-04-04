package com.asher.threeline.serve.net.base;

import android.content.Context;

import com.asher.threeline.api.ApiConstant;
import com.asher.threeline.util.FileUtil;

import java.util.concurrent.TimeUnit;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;
import okhttp3.Cache;
import okhttp3.OkHttpClient;

/**
 * Created by ouyangfan on 17/4/4.
 *
 * 基础封装
 * Retrofit2 + Dagger2 + RxJava2
 */
@Module
public class BaseNetModule {

    /**
     * 使用缓存,离线缓存,在线请求数据
     * @param context context
     * @return okHttpClient
     */
    @Provides
    @Singleton
    OkHttpClient provideOkHttpClient(Context context) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.connectTimeout(ApiConstant.CONNECT_TIMEOUT, TimeUnit.SECONDS);
        builder.readTimeout(ApiConstant.READ_TIMEOUT, TimeUnit.SECONDS);
        builder.writeTimeout(ApiConstant.WRITE_TIMEOUT, TimeUnit.SECONDS);
        builder.cache(new Cache(FileUtil.getExternalCacheDir(context.getApplicationContext()),
                FileUtil.getCacheSize()));
        return builder.build();
    }
}
