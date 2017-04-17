package com.asher.threeline.db.bean;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;
import io.realm.annotations.Required;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * content database
 */
public class DbContent extends RealmObject {

    /**
     * 主键
     * 可以对应服务器serverId
     */
    @PrimaryKey
    private String serverId;

    /**
     * 类型：music|sentence|article
     * {@link com.asher.threeline.db.IType}
     */
    private Integer type;

    /**
     * 同步KEY
     * Required 数据不能为null
     */
    @Required
    private Long syncKey;

    /**
     * 创建时间
     */
    private String updateTime;

    /**
     * 文章标题
     */
    private String title;

    /**
     * 文章内容
     */
    private String content;

/*    *//**
     * 简言之。概述,简短说明
     *//*
    private String brief;*/

    /**
     * 文章作者
     */
    private String author;

    /**
     * 配图
     */
    private String imagePath;

    /**
     * 歌曲名称
     */
    private String songName;

    /**
     * 歌手
     */
    private String singer;

    /**
     * downloadManager downloadId
     * 下载ID
     */
    private Long downloadId;

    public String getServerId() {
        return serverId;
    }

    public void setServerId(String serverId) {
        this.serverId = serverId;
    }

    public Integer getType() {
        return type;
    }

    public void setType(Integer type) {
        this.type = type;
    }

    public Long getSyncKey() {
        return syncKey;
    }

    public void setSyncKey(Long syncKey) {
        this.syncKey = syncKey;
    }

    public String getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(String updateTime) {
        this.updateTime = updateTime;
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

/*    public String getBrief() {
        return brief;
    }

    public void setBrief(String brief) {
        this.brief = brief;
    }*/

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

    public String getSongName() {
        return songName;
    }

    public void setSongName(String songName) {
        this.songName = songName;
    }

    public String getSinger() {
        return singer;
    }

    public void setSinger(String singer) {
        this.singer = singer;
    }

    public Long getDownloadId() {
        return downloadId;
    }

    public void setDownloadId(Long downloadId) {
        this.downloadId = downloadId;
    }

    @Override
    public String toString() {
        return "DbContent{" +
                "serverId='" + serverId + '\'' +
                ", type=" + type +
                ", syncKey=" + syncKey +
                ", updateTime='" + updateTime + '\'' +
                ", title='" + title + '\'' +
                ", content='" + content + '\'' +
//                ", brief='" + brief + '\'' +
                ", author='" + author + '\'' +
                ", imagePath='" + imagePath + '\'' +
                ", songName='" + songName + '\'' +
                ", singer='" + singer + '\'' +
                ", downloadId=" + downloadId +
                '}';
    }
}
