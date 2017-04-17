package com.asher.threeline.serve.data.content;

import com.asher.threeline.db.bean.DbContent;

import java.util.List;

/**
 * Created by ouyangfan on 2017/3/28.
 * <p>
 * 数据库content表的操作
 */
public interface IDbContentServe {

    void addContentList(List<DbContent> contentList);

    void addContent(DbContent content);

    void delContent(DbContent content);

    DbContent getContent(Integer syncKey);

    List<DbContent> getAllContents();
}
