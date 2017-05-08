package com.asher.threeline.ui.setting;

import android.os.Bundle;

import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.ui.base.BaseActivity;

/**
 * Created by ouyangfan on 17/5/9.
 *
 * setting activity
 */
public class SettingActivity extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_setting);
    }

    @Override
    protected void setupComponent(AppComponent appComponent) {

    }
}
