package com.asher.threeline.serve.music;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 2017/3/28.
 */
@Module
public class DbMusicServeModule {
    @Provides
    public IDbMusicServe provideDbMusicServe() {
        return new DbMusicServeImpl();
    }
}
