package com.asher.threeline.ui.main;

import com.asher.threeline.db.bean.DbMusic;

import java.util.List;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * Mvp 中的presenter层
 */
public interface MainPresenter {

    void onBtnClick();

    void prepareMusicToDb();

    DbMusic getMusicFromDb(Integer syncKey);

    List<DbMusic> getAllMusicsFromDb();

    void getDataFromNet();
}
