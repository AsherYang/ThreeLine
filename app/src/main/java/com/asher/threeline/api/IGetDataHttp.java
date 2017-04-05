package com.asher.threeline.api;

import com.asher.threeline.serve.net.base.NetBaseResult;
import com.asher.threeline.serve.net.bean.NetContent;

import io.reactivex.Observable;
import retrofit2.http.GET;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 获取数据API 接口
 */
public interface IGetDataHttp {

    // TODO: 2017/4/5 定义接口
    @GET("/get/last")
    Observable<NetBaseResult<NetContent>> getData();
}
