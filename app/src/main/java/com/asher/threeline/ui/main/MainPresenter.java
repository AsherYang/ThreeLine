package com.asher.threeline.ui.main;

import com.asher.threeline.db.bean.DbContent;

import java.util.List;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * Mvp 中的presenter层
 */
public interface MainPresenter {

    void onBtnClick();

    void prepareContentToDb();

    DbContent getContentFromDb(Integer syncKey);

    List<DbContent> getAllContentsFromDb();

    void getDataFromNet();
}
