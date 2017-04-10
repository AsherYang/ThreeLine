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
    private Long updateTime;

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

    public Long getUpdateTime() {
        return updateTime;
    }

    public void setUpdateTime(Long updateTime) {
        this.updateTime = updateTime;
    }

    @Override
    public String toString() {
        return "NetContent{" +
                "type=" + type +
                ", title='" + title + '\'' +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                ", updateTime=" + updateTime +
                '}';
    }
}
