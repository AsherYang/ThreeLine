package com.asher.threeline;

import android.content.Context;
import android.content.res.Resources;

import javax.inject.Singleton;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 2017/3/22.
 *
 * application 模块
 */
@Module
public class AppModule {
    private App app;

    AppModule(App application) {
        this.app = application;
    }

    @Provides
    @Singleton
    public Context provideApplication() {
        return app;
    }

    @Provides
    @Singleton
    public Resources provideResources(Context context) {
        return context.getResources();
    }
}
