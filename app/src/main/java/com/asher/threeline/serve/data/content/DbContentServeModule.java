package com.asher.threeline.serve.data.content;

import dagger.Module;
import dagger.Provides;

/**
 * Created by ouyangfan on 2017/3/28.
 */
@Module
public class DbContentServeModule {
    @Provides
    public IDbContentServe provideDbContentServe() {
        return new DbContentServeImpl();
    }
}
