package com.asher.threeline;

import android.app.Application;
import android.content.Context;

import com.github.moduth.blockcanary.BlockCanary;
import com.squareup.leakcanary.LeakCanary;
import com.squareup.leakcanary.RefWatcher;

import io.realm.Realm;
import uk.co.chrisjenx.calligraphy.CalligraphyConfig;

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
    private RefWatcher mRefWatcher;

    @Override
    public void onCreate() {
        super.onCreate();
        setupGraph();
        initRealm();
//        initJPush();
        initCanary();
        initFresco();
        initFontStyle();
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
/*    private void initJPush() {
        JPushInterface.setDebugMode(true);
        JPushInterface.init(this);
    }*/

    private void initCanary() {
        if (LeakCanary.isInAnalyzerProcess(this)) {
            // This process is dedicated to LeakCanary for heap analysis.
            // You should not init your app in this process.
            return;
        }
        mRefWatcher = LeakCanary.install(this);
        BlockCanary.install(this, new AppBlockCanaryContext()).start();
    }

    private void initFresco() {
//        Fresco.initialize(this);
    }

    private void initFontStyle() {
        CalligraphyConfig.initDefault(new CalligraphyConfig.Builder()
                .setDefaultFontPath("fonts/jianshi_default.otf")
                .setFontAttrId(R.attr.fontPath)
                .build()
        );
    }

    public AppComponent component() {
        return component;
    }

    public static App get(Context context) {
        return (App) context.getApplicationContext();
    }

    // 提供检测内存泄漏watcher
    public static RefWatcher getRefWatcher(Context context) {
        App app = (App) context.getApplicationContext();
        return app.mRefWatcher;
    }
}
