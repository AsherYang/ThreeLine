package com.asher.threeline.ui.base;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;

import com.asher.threeline.App;
import com.asher.threeline.AppComponent;

import uk.co.chrisjenx.calligraphy.CalligraphyContextWrapper;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * baseActivity
 */
public abstract class BaseActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setupComponent(App.get(this).component());
    }

    // 提供初始化组件方法，交由各类实现
    protected abstract void setupComponent(AppComponent appComponent);

    @Override
    protected void attachBaseContext(Context newBase) {
        super.attachBaseContext(CalligraphyContextWrapper.wrap(newBase));
    }
}
