package com.asher.threeline.ui.main;

import com.asher.threeline.serve.data.music.IDbMusicServe;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * module 模块，将view、presenter与Model关联起来
 * 一个module模块包含其他的module模块的写法
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

    /**
     * 注意点：这里的IDbMusicServe是通过DbMusicServeModule的provider的
     * 无需再进行额外初始化，可直接使用IDbMusicServe
     * 1. 放在参数里，是可靠的
     * 2. 如果将IDbMusicServe 放在本类全局变量的话，是需要进行另外实例化的，这样就显式依赖了
     */
    @Provides
    MainPresenter providePresenter(IDbMusicServe dbMusicServe) {
        return new MainPresenterImpl(mainView, dbMusicServe);
    }
}
