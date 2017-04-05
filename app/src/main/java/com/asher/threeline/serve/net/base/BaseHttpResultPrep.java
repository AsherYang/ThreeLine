package com.asher.threeline.serve.net.base;

import io.reactivex.functions.Function;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 网络返回数据预处理
 */
public class BaseHttpResultPrep<T> implements Function<NetBaseResult<T>, T> {

    @Override
    public T apply(NetBaseResult<T> tNetBaseResult) throws Exception {
        String code = tNetBaseResult.getCode();
        if (!NetBaseResult.SUCCESS.equals(code)) {
            throw new HttpResultException(code);
        }
        return tNetBaseResult.getData();
    }
}
