package com.asher.threeline.ui.theme;

/**
 * Created by ouyangfan on 17/4/19.
 * <p>
 * 用于自定义view 随Theme刷新的接口
 * 若某个view需要随Theme改变而改变,则可实现该接口
 */
public interface IThemeable {

    void refreshTheme(ThemeHelper themeHelper);
}