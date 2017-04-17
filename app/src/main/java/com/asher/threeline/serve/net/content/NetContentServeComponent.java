package com.asher.threeline.serve.net.content;

import com.asher.threeline.AppComponent;
import com.asher.threeline.AppScope;
import com.asher.threeline.serve.data.content.DbContentServeModule;
import com.asher.threeline.serve.data.content.IDbContentServe;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * github net server component
 */
@AppScope
@Component(
        dependencies = {AppComponent.class},
        modules = {NetContentServeModule.class, DbContentServeModule.class}
)
public interface NetContentServeComponent {

    IDbContentServe provideDbContentServe();

    INetContentServe provideNetServe();
}
