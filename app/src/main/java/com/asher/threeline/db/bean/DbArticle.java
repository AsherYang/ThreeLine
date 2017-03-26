package com.asher.threeline.db.bean;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * 类型为长文的数据
 * article database
 */
public class DbArticle extends DbBase {

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
                "title='" + title + '\'' +
                ", content='" + content + '\'' +
                ", author='" + author + '\'' +
                ", imagePath='" + imagePath + '\'' +
                '}';
    }
}
