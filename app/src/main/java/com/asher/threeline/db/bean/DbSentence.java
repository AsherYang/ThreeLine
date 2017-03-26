package com.asher.threeline.db.bean;

/**
 * Created by ouyangfan on 17/3/26.
 *
 * 类型为语录(短文)的数据
 *  sentence database
 */
public class DbSentence extends DbBase {

    /**
     * 短文内容
     */
    private String content;

    /**
     * 短文作者
     */
    private String author;

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
                "content='" + content + '\'' +
                ", author='" + author + '\'' +
                '}';
    }
}
