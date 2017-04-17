package com.asher.threeline.ui.main;

import com.asher.threeline.db.bean.DbContent;

import java.util.List;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * MVP 中view 层
 */
public interface MainView {

    void showClick(String showText);

    void refreshAdapter(List<DbContent> contents);
}
