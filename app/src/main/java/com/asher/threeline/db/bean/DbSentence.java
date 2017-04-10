package com.asher.threeline.db.bean;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;
import io.realm.annotations.Required;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * 类型为语录(短文)的数据
 *  sentence database
 */
public class DbSentence extends RealmObject {

    /**
     * 主键
     * 可以对应服务器serverId
     */
    @PrimaryKey
    private String id;

    /**
     * 同步KEY
     * Required 数据不能为null
     */
    @Required
    private Long syncKey;

    /**
     * 创建时间
     */
    private Long createTime;

    /**
     * 短文内容
     */
    private String content;

    /**
     * 短文作者
     */
    private String author;

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

    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    @Override
    public String toString() {
        return "DbSentence{" +
                "id='" + id + '\'' +
                ", syncKey=" + syncKey +
                ", createTime=" + createTime +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                '}';
    }
}
