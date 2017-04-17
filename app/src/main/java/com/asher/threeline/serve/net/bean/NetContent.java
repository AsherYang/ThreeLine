package com.asher.threeline.serve.net.bean;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 网络数据
 */
public class NetContent {

    /**
     * sever id
     */
    private Long id;

    /**
     * type：music|sentence|article
     * {@link com.asher.threeline.db.IType}
     */
    private Integer type;

    /**
     * title
     */
    private String title;

    /**
     * content
     */
    private String content;

    /**
     * author
     */
    private String author;

    /**
     * time
     */
    private String updateTime;

    /**
     * sync key
     */
    private Long syncKey;

    /**
     * image path
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

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public Integer getType() {
        return type;
    }

    public void setType(Integer type) {
        this.type = type;
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

    public String getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(String updateTime) {
        this.updateTime = updateTime;
    }

    public Long getSyncKey() {
        return syncKey;
    }

    public void setSyncKey(Long syncKey) {
        this.syncKey = syncKey;
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

    @Override
    public String toString() {
        return "NetContent{" +
                "id=" + id +
                ", type=" + type +
                ", title='" + title + '\'' +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                ", updateTime='" + updateTime + '\'' +
                ", syncKey=" + syncKey +
                ", imagePath='" + imagePath + '\'' +
                ", songName='" + songName + '\'' +
                ", singer='" + singer + '\'' +
                '}';
    }
}
