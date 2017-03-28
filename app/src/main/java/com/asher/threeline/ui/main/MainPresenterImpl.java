package com.asher.threeline.ui.main;

import com.asher.threeline.db.bean.DbMusic;
import com.asher.threeline.serve.music.IDbMusicServe;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * presenter 实现类
 */
public class MainPresenterImpl implements MainPresenter {

    private MainView mainView;
    private IDbMusicServe dbMusicServe;

    public MainPresenterImpl(MainView mainView, IDbMusicServe dbMusicServe) {
        this.mainView = mainView;
        this.dbMusicServe = dbMusicServe;
    }

    @Override
    public void onBtnClick() {
        String songName = getMusicFromDb(9).getSongName();
        mainView.showClick(songName);
    }

    @Override
    public void prepareMusicToDb() {
        List<DbMusic> dbMusics = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            DbMusic music = new DbMusic();
            music.setSongName("song name = " + i);
            music.setId(String.valueOf(i));
            music.setSyncKey((long) i);
            dbMusics.add(music);
        }
        dbMusicServe.addMusicList(dbMusics);
    }

    @Override
    public DbMusic getMusicFromDb(Integer syncKey) {
        return dbMusicServe.getMusic(syncKey);
    }

    @Override
    public List<DbMusic> getAllMusicsFromDb() {
        return dbMusicServe.getAllMusic();
    }
}
