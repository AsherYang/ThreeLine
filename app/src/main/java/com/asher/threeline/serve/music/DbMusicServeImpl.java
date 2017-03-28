package com.asher.threeline.serve.music;

import com.asher.threeline.aop.annotation.DbRealm;
import com.asher.threeline.db.bean.DbMusic;

import java.util.List;

import io.realm.Realm;

/**
 * Created by ouyangfan on 2017/3/28.
 * <p>
 * 数据库music 表操作实现类
 */
public class DbMusicServeImpl implements IDbMusicServe {

    @DbRealm
    @Override
    public void addMusicList(List<DbMusic> musicList) {

    }

    @DbRealm
    @Override
    public void addMusic(DbMusic music) {

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
