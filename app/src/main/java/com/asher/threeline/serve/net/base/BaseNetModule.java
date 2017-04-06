package com.asher.threeline.serve.net.base;

import android.content.Context;

import com.asher.threeline.api.ApiConstant;
import com.asher.threeline.util.FileUtil;
import com.asher.threeline.util.NetWorkUtil;

import java.io.IOException;
import java.util.concurrent.TimeUnit;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;
import okhttp3.Cache;
import okhttp3.CacheControl;
import okhttp3.Interceptor;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import okhttp3.logging.HttpLoggingInterceptor;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava2.RxJava2CallAdapterFactory;
import retrofit2.converter.jackson.JacksonConverterFactory;

/**
 * Created by ouyangfan on 17/4/4.
 * <p>
 * 基础网络封装
 * Retrofit2 + Dagger2 + RxJava2
 * 本基础module不提供component，且为全局单例模式，直接由applicationComponent处理提供
 */
@Module
public class BaseNetModule {

    /**
     * 使用缓存,离线缓存,在线请求数据
     *
     * @return okHttpClient
     */
    @Provides
    @Singleton
    OkHttpClient provideOkHttpClient(Context context) {
        OkHttpClient.Builder builder = new OkHttpClient.Builder();
        builder.connectTimeout(ApiConstant.CONNECT_TIMEOUT, TimeUnit.SECONDS);
        builder.readTimeout(ApiConstant.READ_TIMEOUT, TimeUnit.SECONDS);
        builder.writeTimeout(ApiConstant.WRITE_TIMEOUT, TimeUnit.SECONDS);
        builder.addNetworkInterceptor(getNetWorkInterceptor(context));
        builder.addInterceptor(getInterceptor(context));
        builder.addInterceptor(getLogInterceptor());
        builder.cache(new Cache(FileUtil.getHttpCacheDir(context.getApplicationContext()),
                FileUtil.getHttpCacheSize()));
        return builder.build();
    }

    /**
     * 设置拦截器
     *
     * @return 拦截器
     */
    private Interceptor getInterceptor(final Context context) {
        return new Interceptor() {
            @Override
            public Response intercept(Chain chain) throws IOException {
                Request request = chain.request();
                if (!NetWorkUtil.isAvailable(context)) {
                    request = request.newBuilder()
                            .cacheControl(CacheControl.FORCE_CACHE)
                            .build();
                }
                return chain.proceed(request);
            }
        };
    }

    /**
     * 设置超时拦截器
     */
    public Interceptor getNetWorkInterceptor(final Context context) {
        return new Interceptor() {
            @Override
            public Response intercept(Chain chain) throws IOException {
                Request request = chain.request();
                Response response = chain.proceed(request);
                if (NetWorkUtil.isAvailable(context)) {
                    int maxAge = 1 * 60;
                    // 有网络时,设置缓存超时时间为1小时
                    response.newBuilder()
                            .header("Cache-Control", "public, max-age=" + maxAge)
                            .removeHeader("Pragma")
                            .build();
                } else {
                    // 无网络,设置超时时间为1周
                    int maxStale = 7 * 24 * 60 * 60;
                    response.newBuilder()
                            .header("Cache-Control", "public, only-if-cached, max-stale=" + maxStale)
                            .removeHeader("Pragma")
                            .build();
                }
                return response;
            }
        };
    }

    /**
     * 网络日志拦截器
     */
    private Interceptor getLogInterceptor() {
        HttpLoggingInterceptor logging = new HttpLoggingInterceptor();
        logging.setLevel(HttpLoggingInterceptor.Level.BASIC);
        return logging;
    }

    @Provides
    @Singleton
    Retrofit provideRetrofit(OkHttpClient okHttpClient) {
        return new Retrofit.Builder()
                .baseUrl(ApiConstant.BASE_URL)
                .addConverterFactory(JacksonConverterFactory.create())
                .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
                .client(okHttpClient)
                .build();
    }
}
