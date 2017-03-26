package com.asher.threeline.db.bean;

/**
 * Created by ouyangfan on 2017/3/22.
 *
 * 类型为music的数据
 * music database
 */
public class DbMusic extends DbBase {

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
                "songName='" + songName + '\'' +
                ", singer='" + singer + '\'' +
                ", brief='" + brief + '\'' +
                ", downloadId=" + downloadId +
                '}';
    }
}
