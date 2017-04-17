package com.asher.threeline.ui.main;

import com.asher.threeline.ActivityScope;
import com.asher.threeline.serve.net.content.NetContentServeComponent;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * component
 */
@ActivityScope
@Component(
        dependencies = {NetContentServeComponent.class},
        modules = {MainModule.class}
)
public interface MainComponent {

    void inject(MainActivity mainActivity);
}
