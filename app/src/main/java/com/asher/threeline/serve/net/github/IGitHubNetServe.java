package com.asher.threeline.serve.net.github;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 获取github 数据网络接口
 */
public interface IGitHubNetServe {

    /**
     * 获取user 数据
     *
     * @param user         user参数
     * @param userCallBack 回调
     */
    void getUser(String user, OnGetGitUserCallBack userCallBack);
}
