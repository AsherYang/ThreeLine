package com.asher.threeline.api;

import com.asher.threeline.serve.net.base.NetBaseResult;
import com.asher.threeline.serve.net.github.NetGitUser;

import io.reactivex.Observable;
import retrofit2.http.GET;
import retrofit2.http.Path;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 获取数据API 接口
 */
public interface IGetDataHttp {

    // TODO: 2017/4/5 定义接口，使用github user 来测试整体网络框架
    @GET("/users/{user}")
    Observable<NetBaseResult<NetGitUser>> getUser(@Path("user") String user);
}
