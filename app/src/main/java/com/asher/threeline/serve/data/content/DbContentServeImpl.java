package com.asher.threeline.serve.data.content;

import com.asher.threeline.aop.annotation.DbRealmAdd;
import com.asher.threeline.db.bean.DbContent;

import java.util.List;

import io.realm.Realm;

/**
 * Created by ouyangfan on 2017/3/28.
 * <p>
 * 数据库content表操作实现类
 */
public class DbContentServeImpl implements IDbContentServe {

    @DbRealmAdd
    @Override
    public void addContentList(List<DbContent> contentList) {
        // you need do nothing. just do it auto.
    }

    @DbRealmAdd
    @Override
    public void addContent(DbContent content) {
        // you need do nothing. just do it auto.
    }

    @Override
    public void delContent(DbContent content) {

    }

    @Override
    public DbContent getContent(Integer syncKey) {
        Realm realm = Realm.getDefaultInstance();
        return realm.where(DbContent.class).equalTo("syncKey", syncKey).findFirst();
    }

    @Override
    public List<DbContent> getAllContents() {
        Realm realm = Realm.getDefaultInstance();
        return realm.where(DbContent.class).findAll();
    }
}
