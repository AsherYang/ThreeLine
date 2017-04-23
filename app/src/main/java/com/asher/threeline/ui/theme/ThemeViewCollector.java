package com.asher.threeline.ui.theme;

import android.content.Context;
import android.view.View;

import com.asher.threeline.util.PreferenceUtil;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ouyangfan on 17/4/24.
 *
 * 装入随Theme改变的view
 */
public class ThemeViewCollector {

    private static ThemeViewCollector instance;
    private List<View> mViewList;

    private ThemeViewCollector() {
        mViewList = new ArrayList<>();
    }

    public static ThemeViewCollector getInstance() {
        if (instance == null) {
            synchronized (PreferenceUtil.class) {
                if (instance == null)
                    instance = new ThemeViewCollector();
            }
        }
        return instance;
    }

    public void addView(View view) {
        mViewList.add(view);
    }

    public void removeView(View view) {
        mViewList.remove(view);
    }

    public void themeChanged(Context context) {
        Theme theme = ThemeHelper.getBaseTheme(context);
        switch (theme) {
            case DARK:
                showtDarkTheme();
                break;
            case LIGHT:
            default:
                showtLightTheme();
                break;
        }
    }

    private void showtDarkTheme() {
        for (View view : mViewList) {

        }
    }

    private void showtLightTheme() {
        for (View view : mViewList) {

        }
    }
}
