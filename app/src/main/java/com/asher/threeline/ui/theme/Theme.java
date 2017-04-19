package com.asher.threeline.ui.theme;

/**
 * Created by ouyangfan on 17/4/19.
 *
 * 主题种类
 */
public enum Theme {
    LIGHT(1), DARK(2);

    int value;

    Theme(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public static Theme fromValue(int value) {
        switch (value) {
            case 1:
                return LIGHT;
            case 2:
                return DARK;
            default:
                return LIGHT;
        }
    }
}
