package com.asher.threeline;

import javax.inject.Singleton;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/3/22.
 */
@Singleton
@Component(
        modules = {AppModule.class}
)
public interface AppComponent {
    void inject(App app);
}
