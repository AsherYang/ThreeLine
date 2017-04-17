package com.asher.threeline.serve.data.content;

import com.asher.threeline.ActivityScope;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/6.
 *
 * db content component
 */
@ActivityScope
@Component(
        modules = {DbContentServeModule.class}
)
public interface DbContentServeComponent {

    IDbContentServe provideDbContentServe();
}
