package com.asher.threeline.serve.net.github;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 回调接口
 */
public interface OnGetGitUserCallBack {

    /**
     * 获取github user 成功
     * @param gitUser github user
     */
    void onSuccess(NetGitUser gitUser);

    /**
     * 获取数据失败
     * @param throwable 异常信息
     */
    void onFail(Throwable throwable);
}
