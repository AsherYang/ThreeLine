package com.asher.threeline.ui.main;

import com.asher.threeline.ActivityScope;
import com.asher.threeline.AppComponent;
import com.asher.threeline.serve.music.DbMusicServeModule;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/3/22.
 */
@ActivityScope
@Component(
        dependencies = AppComponent.class,
        modules = {MainModule.class, DbMusicServeModule.class}
)
public interface MainComponent {
    void inject(MainActivity mainActivity);
}
