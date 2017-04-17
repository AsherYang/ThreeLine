package com.asher.threeline.serve.net.util;

import android.support.annotation.NonNull;

import com.asher.threeline.db.bean.DbContent;
import com.asher.threeline.serve.net.bean.NetContent;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ouyangfan on 2017/4/17.
 * <p>
 * 网络数据转换为数据库存储数据
 */
public class NetConvert2Db {

    /**
     * netContent to dbContent
     * @param netContent netContent
     * @return dbContent
     */
    public static DbContent toDbContent(@NonNull NetContent netContent) {
        DbContent dbContent = new DbContent();
        dbContent.setServerId(String.valueOf(netContent.getId()));
        dbContent.setType(netContent.getType());
        dbContent.setSyncKey(netContent.getSyncKey());
        dbContent.setUpdateTime(netContent.getUpdateTime());
        dbContent.setTitle(netContent.getTitle());
        dbContent.setContent(netContent.getContent());
        dbContent.setAuthor(netContent.getAuthor());
        dbContent.setImagePath(netContent.getImagePath());
        dbContent.setSongName(netContent.getSongName());
        dbContent.setSinger(netContent.getSinger());
        return dbContent;
    }

    public static List<DbContent> toDbContents(@NonNull List<NetContent> netContents) {
        List<DbContent> dbContents = new ArrayList<>();
        if (netContents.isEmpty()) {
            return dbContents;
        }
        for (NetContent netContent : netContents) {
            dbContents.add(toDbContent(netContent));
        }
        return dbContents;
    }
}
