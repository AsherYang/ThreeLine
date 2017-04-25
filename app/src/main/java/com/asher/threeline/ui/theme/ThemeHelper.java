package com.asher.threeline.ui.theme;

import android.content.Context;
import android.support.annotation.ColorRes;
import android.support.v4.content.ContextCompat;

import com.asher.threeline.R;
import com.asher.threeline.util.IPreferenceKey;
import com.asher.threeline.util.PreferenceUtil;

/**
 * Created by ouyangfan on 17/4/19.
 * <p>
 * 获取Theme相关的颜色值
 */
public class ThemeHelper {

    private PreferenceUtil SP;
    private Context context;
    private Theme baseTheme;

    public ThemeHelper(Context context) {
        this.SP = PreferenceUtil.getInstance(context);
        this.context = context;
    }

    public static ThemeHelper getThemeHelper(Context context) {
        ThemeHelper t = new ThemeHelper(context);
        t.updateTheme();
        return t;
    }

    public void updateTheme() {
        baseTheme = Theme.fromValue(SP.getInt(IPreferenceKey.BASE_THEME, 1));
    }

    public Theme getBaseTheme() {
        return baseTheme;
    }

    public void setBaseTheme(Theme baseTheme) {
        this.baseTheme = baseTheme;
        SP.putInt(IPreferenceKey.BASE_THEME, getBaseTheme().getValue());
    }

    public static Theme getBaseTheme(Context context) {
        PreferenceUtil SP = PreferenceUtil.getInstance(context);
        return Theme.fromValue(SP.getInt(IPreferenceKey.BASE_THEME, Theme.LIGHT.value));
    }

    /**
     * change theme to `toTheme`
     * <p>
     * 请注意： 这个方法不要删除，用于暴露给外部调用
     *
     * @param toTheme theme
     */
    public void changeTheme(Theme toTheme) {
        setBaseTheme(toTheme);
        // notice: the other notification code completed in javassist which named MyInject.groovy
    }

    private int getColor(@ColorRes int color) {
        return ContextCompat.getColor(context, color);
    }

    public int getBackgroundColor() {
        switch (baseTheme) {
            case DARK:
                return getColor(R.color.theme_dark_background);
            case LIGHT:
            default:
                return getColor(R.color.theme_light_background);
        }
    }

    public int getTextColor() {
        switch (baseTheme) {
            case DARK:
                return getColor(R.color.grey_200);
            case LIGHT:
            default:
                return getColor(R.color.grey_800);
        }
    }
}
