package com.asher.threeline.serve.net.content;

import com.asher.threeline.AppComponent;
import com.asher.threeline.AppScope;

import dagger.Component;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * github net server component
 */
@AppScope
@Component(
        dependencies = {AppComponent.class},
        modules = {ContentNetServeModule.class}
)
public interface ContentNetServeComponent {

    IContentNetServe provideNetServe();
}
