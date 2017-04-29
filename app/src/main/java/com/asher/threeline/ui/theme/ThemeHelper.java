package com.asher.threeline.ui.theme;

import android.content.Context;

import com.asher.threeline.util.IPreferenceKey;
import com.asher.threeline.util.PreferenceUtil;

/**
 * Created by ouyangfan on 17/4/19.
 * <p>
 * 获取Theme相关的颜色值
 */
public class ThemeHelper {

    private PreferenceUtil SP;

    public ThemeHelper(Context context) {
        this.SP = PreferenceUtil.getInstance(context);
    }

    public static ThemeHelper getThemeHelper(Context context) {
        return new ThemeHelper(context);
    }

    public Theme getBaseTheme() {
        return Theme.fromValue(SP.getInt(IPreferenceKey.BASE_THEME, Theme.LIGHT.value));
    }

    // 不要删除，groovy中会用到
    public static Theme getBaseTheme(Context context) {
        PreferenceUtil SP = PreferenceUtil.getInstance(context);
        return Theme.fromValue(SP.getInt(IPreferenceKey.BASE_THEME, Theme.LIGHT.value));
    }

    public void setBaseTheme(Theme baseTheme) {
        SP.putInt(IPreferenceKey.BASE_THEME, baseTheme.getValue());
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

}
