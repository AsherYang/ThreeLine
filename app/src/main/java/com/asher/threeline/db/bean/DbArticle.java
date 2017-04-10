package com.asher.threeline.db.bean;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;
import io.realm.annotations.Required;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * 类型为长文的数据
 * article database
 */
public class DbArticle extends RealmObject {

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
     * 文章标题
     */
    private String title;

    /**
     * 文章内容
     */
    private String content;

    /**
     * 文章作者
     */
    private String author;

    /**
     * 配图
     */
    private String imagePath;

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

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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

    public String getImagePath() {
        return imagePath;
    }

    public void setImagePath(String imagePath) {
        this.imagePath = imagePath;
    }

    @Override
    public String toString() {
        return "DbArticle{" +
                "id='" + id + '\'' +
                ", syncKey=" + syncKey +
                ", createTime=" + createTime +
                ", title='" + title + '\'' +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                ", imagePath='" + imagePath + '\'' +
                '}';
    }
}
