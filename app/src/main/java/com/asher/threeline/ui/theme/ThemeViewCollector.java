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

    public void themeChanged(Context context) {
        for (ThemeActivity activity : mActivityList) {
            activity.updateUiElements();
        }
    }

    public boolean hasContainActivity(ThemeActivity activity) {
        if (null == mActivityList || mActivityList.isEmpty()) {
            return false;
        }
        return mActivityList.contains(activity);
    }

}
