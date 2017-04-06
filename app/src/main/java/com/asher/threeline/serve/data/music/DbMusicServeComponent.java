package com.asher.threeline.serve.data.music;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/6.
 */
@Component(
        modules = {DbMusicServeModule.class}
)
public interface DbMusicServeComponent {

    IDbMusicServe provideDbMusicServe();
}
