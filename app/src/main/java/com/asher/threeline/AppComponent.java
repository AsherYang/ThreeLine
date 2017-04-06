package com.asher.threeline;

import android.content.Context;
import android.content.res.Resources;

import com.asher.threeline.serve.net.base.BaseNetModule;

import javax.inject.Singleton;

import dagger.Component;
import retrofit2.Retrofit;

/**
 * Created by ouyangfan on 2017/3/22.
 */
@Singleton
@Component(
        modules = {AppModule.class, BaseNetModule.class}
)
public interface AppComponent {

    Context provideApplication();

    // 这里不需要设置context形参，因为这是component暴露给子组件的对象
    Resources provideResources();

    Retrofit provideRetrofit();

    void inject(App app);
}
