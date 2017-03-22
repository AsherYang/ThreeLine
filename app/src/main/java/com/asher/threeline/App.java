package com.asher.threeline;

import android.app.Application;
import android.content.Context;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * MVP + dagger2 模式
 * <p/>
 * dagger2 通过inject将M-V-P关联起来
 * 可以使mvp的V–>P–>M的之间依赖也轻松解决 方便不少
 */
public class App extends Application {

    private AppComponent component;

    @Override
    public void onCreate() {
        super.onCreate();
        setupGraph();
    }

    /**
     * application 中初始化构建图
     */
    private void setupGraph() {
        component = DaggerAppComponent.builder()
                .appModule(new AppModule(this))
                .build();
        component.inject(this);
    }

    public AppComponent component() {
        return component;
    }

    public static App get(Context context) {
        return (App) context.getApplicationContext();
    }
}
