package com.asher.threeline.db.bean;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * 数据基类
 */
class DbBase extends RealmObject {

    /**
     * 主键
     */
    @PrimaryKey
    private String id;

    /**
     * 同步KEY
     */
    private Long syncKey;

    /**
     * 创建时间
     */
    private Long createTime;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Long getSyncKey() {
        return syncKey;
    }

    public void setSyncKey(Long syncKey) {
        this.syncKey = syncKey;
    }

    public Long getCreateTime() {
        return createTime;
    }

    public void setCreateTime(Long createTime) {
        this.createTime = createTime;
    }

    @Override
    public String toString() {
        return "DbBase{" +
                "id='" + id + '\'' +
                ", syncKey=" + syncKey +
                ", createTime=" + createTime +
                '}';
    }
}
