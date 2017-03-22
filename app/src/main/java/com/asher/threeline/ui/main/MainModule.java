package com.asher.threeline.ui.main;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * module 模块，将view、presenter与Model关联起来
 */
@Module
public class MainModule {

    private MainView mainView;

    public MainModule(MainView mainView) {
        this.mainView = mainView;
    }

    @Provides
    MainView provideMainView() {
        return mainView;
    }

    @Provides
    MainPresenter providePresenter() {
        return new MainPresenterImpl(mainView);
    }
}
