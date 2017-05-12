package com.asher.threeline;

import android.app.Application;
import android.content.Context;

import com.github.moduth.blockcanary.BlockCanary;
import com.squareup.leakcanary.LeakCanary;

import cn.jpush.android.api.JPushInterface;
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
        initJPush();
        initCanary();
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

    /**
     * 初始化极光推送
     */
    private void initJPush() {
        JPushInterface.setDebugMode(true);
        JPushInterface.init(this);
    }

    private void initCanary() {
        if (LeakCanary.isInAnalyzerProcess(this)) {
            // This process is dedicated to LeakCanary for heap analysis.
            // You should not init your app in this process.
            return;
        }
        LeakCanary.install(this);
        BlockCanary.install(this, new AppBlockCanaryContext()).start();
    }

    public AppComponent component() {
        return component;
    }

    public static App get(Context context) {
        return (App) context.getApplicationContext();
    }
}
