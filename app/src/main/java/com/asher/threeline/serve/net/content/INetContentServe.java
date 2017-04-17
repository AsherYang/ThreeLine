package com.asher.threeline.serve.net.content;

import com.asher.threeline.db.bean.DbContent;
import com.asher.threeline.serve.net.base.OnNetCallBack;

import java.util.List;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 获取服务器数据网络接口
 */
public interface INetContentServe {

    /**
     * 获取最新内容数据
     *
     * @param callBack 回调
     */
    void getLastData(OnNetCallBack<List<DbContent>> callBack);
}
