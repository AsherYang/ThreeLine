package com.asher.threeline.ui.setting;

import com.asher.threeline.ActivityScope;

import dagger.Component;

/**
 * Created by ouyangfan on 17/5/9.
 * <p>
 * setting component
 */
@ActivityScope
@Component(
        modules = {SettingModule.class}
)
public interface SettingComponent {

    void inject(SettingActivity settingActivity);
}
