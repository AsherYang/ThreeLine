package com.asher.threeline.serve.data.music;

import com.asher.threeline.db.bean.DbMusic;

import java.util.List;

/**
 * Created by ouyangfan on 2017/3/28.
 * <p>
 * 数据库music表的操作
 */
public interface IDbMusicServe {

    void addMusicList(List<DbMusic> musicList);

    void addMusic(DbMusic music);

    void delMusic(DbMusic music);

    DbMusic getMusic(Integer syncKey);

    List<DbMusic> getAllMusic();
}
