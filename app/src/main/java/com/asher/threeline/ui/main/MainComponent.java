package com.asher.threeline.ui.main;

import com.asher.threeline.ActivityScope;
import com.asher.threeline.serve.data.music.DbMusicServeComponent;
import com.asher.threeline.serve.net.content.ContentNetServeComponent;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * component
 */
@ActivityScope
@Component(
        dependencies = {DbMusicServeComponent.class, ContentNetServeComponent.class},
        modules = {MainModule.class}
)
public interface MainComponent {

    void inject(MainActivity mainActivity);
}
