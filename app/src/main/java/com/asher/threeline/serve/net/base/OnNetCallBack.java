package com.asher.threeline.serve.net.base;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 网络回调接口
 */
public interface OnNetCallBack<T> {

    /**
     * 获取数据成功
     */
    void onSuccess(T t);

    /**
     * 获取数据失败
     * @param throwable 异常信息
     */
    void onFail(Throwable throwable);
}
