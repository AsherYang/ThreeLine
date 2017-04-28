package com.asher.threeline.ui.theme;

import android.os.Bundle;
import android.support.annotation.CallSuper;
import android.util.Log;
import android.view.View;

import com.asher.threeline.ui.base.BaseActivity;
import com.asher.threeline.util.PreferenceUtil;
import com.asher.threeline.util.ViewUtil;

/**
 * Created by ouyangfan on 17/4/19.
 *
 * theme base activity
 *
 * TODO 需要删除, MyInject.groovy 已处理，
 * TODO 还需要生成一个ITheme的接口，注入到每个带@skin的activity上去
 */
public abstract class ThemeActivity extends BaseActivity {

    private ThemeHelper themeHelper;
    private PreferenceUtil SP;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        themeHelper = ThemeHelper.getThemeHelper(getApplicationContext());
        SP = PreferenceUtil.getInstance(getApplicationContext());
    }

    @Override
    protected void onResume() {
        super.onResume();
        updateTheme();
    }

    public void updateTheme() {
        themeHelper.updateTheme();
        updateUiElements();
    }

    @CallSuper
    public void updateUiElements() {
        for (View view : ViewUtil.getAllChildren(findViewById(android.R.id.content))) {
            if (view instanceof IThemeable) {
                ((IThemeable) view).refreshTheme(getThemeHelper());
            }
        }
        Log.i("TAG", "ThemeActivity changeTheme");
    }

    public ThemeHelper getThemeHelper() {
        return themeHelper;
    }
}
