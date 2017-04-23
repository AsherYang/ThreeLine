package com.asher.threeline.ui.theme;

import android.content.Context;

import com.asher.threeline.util.PreferenceUtil;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ouyangfan on 17/4/24.
 *
 * 装入随Theme改变的Activity
 */
public class ThemeViewCollector {

    private static ThemeViewCollector instance;
    private List<ThemeActivity> mActivityList;

    private ThemeViewCollector() {
        mActivityList = new ArrayList<>();
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

    public void addActivity(ThemeActivity activity) {
        mActivityList.add(activity);
    }

    public void removeActivity(ThemeActivity activity) {
        if (null == mActivityList || mActivityList.isEmpty()) {
            return;
        }
        mActivityList.remove(activity);
    }

    public void clearAll() {
        mActivityList.clear();
    }

    // TODO: 17/4/24 可该用javassist实现
    public void themeChanged(Context context) {
        Theme theme = ThemeHelper.getBaseTheme(context);
        switch (theme) {
            case DARK:
                showDarkTheme();
                break;
            case LIGHT:
            default:
                showLightTheme();
                break;
        }
    }

    private void showDarkTheme() {
        for (ThemeActivity activity : mActivityList) {
            activity.updateUiElements();
        }
    }

    private void showLightTheme() {
        for (ThemeActivity activity : mActivityList) {
            activity.updateUiElements();
        }
    }
}
