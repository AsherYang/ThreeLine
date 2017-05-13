package com.asher.threeline.ui.setting;

import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import com.asher.threeline.App;
import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.ui.base.BaseActivity;
import com.asher.threeline.ui.view.TitleBar;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

/**
 * Created by ouyangfan on 17/5/9.
 * <p>
 * setting activity
 */
public class SettingActivity extends BaseActivity {

    @BindView(R.id.setting_title_bar)
    TitleBar settingTitleBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_setting);
        ButterKnife.bind(this);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        // 观察内存泄露情况
        App.getRefWatcher(this).watch(this);
    }

    @Override
    protected void setupComponent(AppComponent appComponent) {
        // TODO: 2017/5/11

    }

    @OnClick({R.id.left_image, R.id.tv_collect})
    void onClick(View view) {
        switch (view.getId()) {
            case R.id.left_image:
                finish();
                break;
            case R.id.tv_collect:
                Toast.makeText(SettingActivity.this, "123", Toast.LENGTH_SHORT).show();
                break;
            default:
                break;
        }
    }
}
