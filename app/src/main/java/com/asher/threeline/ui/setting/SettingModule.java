package com.asher.threeline.ui.setting;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 17/5/9.
 *
 * Setting module
 */
@Module
public class SettingModule {

    private SettingView settingView;

    public SettingModule(SettingView settingView) {
        this.settingView = settingView;
    }

    @Provides
    SettingView provideSettingView() {
        return settingView;
    }

    @Provides
    SettingPresenter provideSettingPresenter() {
        return new SettingPresenterImpl();
    }
}
