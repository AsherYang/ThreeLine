package com.asher.threeline.api;

import com.asher.threeline.serve.net.base.NetBaseResult;
import com.asher.threeline.serve.net.bean.NetContent;
import com.asher.threeline.serve.net.github.NetGitUser;

import java.util.List;

import io.reactivex.Observable;
import retrofit2.http.GET;
import retrofit2.http.Path;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 获取数据API 接口
 * <p>
 * 一般的返回结果我们需要更丰富的一些信息，比如状态码等，和服务器约定后这时候需要使用NetBaseResult封装。
 * 接口如下形式
 * Observable<NetBaseResult<NetGitUser>> getXXX(@Path("user") String user);
 * <p>
 * 调用解析结果时，我们需要使用BaseHttpResultPrep拆包，获取有效信息
 * Observable<NetGitUser> observable = mGetDataHttp.getUser(user);
 * observable.map(new BaseHttpResultPrep<NetGitUser>())
 * .subscribeOn(Schedulers.io())
 */
public interface IGetDataHttp {

    // 测试接口，使用github user 来测试整体网络框架
    @GET("/users/{user}")
    Observable<NetGitUser> getUser(@Path("user") String user);

    // 拿到最新的数据
    @GET("/getlastdata")
    Observable<NetBaseResult<List<NetContent>>> getLastData();
}
