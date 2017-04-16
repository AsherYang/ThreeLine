package com.asher.threeline.serve.net.bean;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 网络数据
 */
public class NetContent {
    /**
     * type：music|sentence|article
     * {@link com.asher.threeline.db.IType}
     */
    private int type;

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

    public int getType() {
        return type;
    }

    public void setType(int type) {
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

    @Override
    public String toString() {
        return "NetContent{" +
                "type=" + type +
                ", title='" + title + '\'' +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                ", updateTime='" + updateTime + '\'' +
                ", syncKey=" + syncKey +
                ", imagePath='" + imagePath + '\'' +
                '}';
    }
}
