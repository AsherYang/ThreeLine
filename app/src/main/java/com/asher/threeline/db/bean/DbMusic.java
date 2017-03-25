package com.asher.threeline.db.bean;

import io.realm.RealmObject;
import io.realm.annotations.PrimaryKey;

/**
 * Created by ouyangfan on 2017/3/22.
 *
 * 类型为music
 * music database
 */

public class DbMusic extends RealmObject{

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

    /**
     * 歌曲名称
     */
    private String songName;

    /**
     * 歌手
     */
    private String singer;

    /**
     * 简言之。概述,简短说明
     */
    private String brief;

    /**
     * downloadManager downloadId
     * 下载ID
     */
    private Long downloadId;

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

    public String getBrief() {
        return brief;
    }

    public void setBrief(String brief) {
        this.brief = brief;
    }

    public Long getDownloadId() {
        return downloadId;
    }

    public void setDownloadId(Long downloadId) {
        this.downloadId = downloadId;
    }

    @Override
    public String toString() {
        return "DbMusic{" +
                "id='" + id + '\'' +
                ", syncKey=" + syncKey +
                ", createTime=" + createTime +
                ", songName='" + songName + '\'' +
                ", singer='" + singer + '\'' +
                ", brief='" + brief + '\'' +
                ", downloadId=" + downloadId +
                '}';
    }
}
