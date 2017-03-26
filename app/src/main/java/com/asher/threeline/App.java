package com.asher.threeline;

import android.app.Application;
import android.content.Context;

import io.realm.Realm;

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
        initRealm();
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

    /**
     * 初始化realm数据库
     */
    private void initRealm() {
        Realm.init(this);
    }

    public AppComponent component() {
        return component;
    }

    public static App get(Context context) {
        return (App) context.getApplicationContext();
    }
}
