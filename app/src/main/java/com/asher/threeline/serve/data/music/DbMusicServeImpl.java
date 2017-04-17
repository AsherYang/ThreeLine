package com.asher.threeline.serve.data.music;

import com.asher.threeline.aop.annotation.DbRealmAdd;
import com.asher.threeline.db.bean.DbMusic;

import java.util.List;

import io.realm.Realm;

/**
 * Created by ouyangfan on 2017/3/28.
 * <p>
 * 数据库music 表操作实现类
 */
public class DbMusicServeImpl implements IDbMusicServe {

    @DbRealmAdd
    @Override
    public void addMusicList(List<DbMusic> musicList) {
        // you need do nothing. just do it auto.
    }

    @DbRealmAdd
    @Override
    public void addMusic(DbMusic music) {
        // you need do nothing. just do it auto.
    }

    @Override
    public void delMusic(DbMusic music) {

    }

    @Override
    public DbMusic getMusic(Integer syncKey) {
        Realm realm = Realm.getDefaultInstance();
        return realm.where(DbMusic.class).equalTo("syncKey", syncKey).findFirst();
    }

    @Override
    public List<DbMusic> getAllMusic() {
        Realm realm = Realm.getDefaultInstance();
        return realm.where(DbMusic.class).findAll();
    }
}
