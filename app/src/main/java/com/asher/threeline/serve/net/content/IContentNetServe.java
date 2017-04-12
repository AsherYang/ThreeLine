package com.asher.threeline.serve.net.content;

import com.asher.threeline.serve.net.base.OnNetCallBack;
import com.asher.threeline.serve.net.bean.NetContent;

import java.util.List;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 获取服务器数据网络接口
 */
public interface IContentNetServe {

    /**
     * 获取最新内容数据
     *
     * @param callBack 回调
     */
    void getLastData(OnNetCallBack<List<NetContent>> callBack);
}
