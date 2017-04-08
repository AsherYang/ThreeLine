package com.asher.threeline.serve.net.github;

import android.util.Log;

import com.asher.threeline.api.IGetDataHttp;

import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.schedulers.Schedulers;

import static android.content.ContentValues.TAG;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 网络接口实现类
 */
public class GitHubNetServeImpl implements IGitHubNetServe {

    private IGetDataHttp mGetDataHttp;

    public GitHubNetServeImpl(IGetDataHttp getDataHttp) {
        this.mGetDataHttp = getDataHttp;
    }

    @Override
    public void getUser(final String user, final OnGetGitUserCallBack userCallBack) {
        Observable<NetGitUser> observable = mGetDataHttp.getUser(user);
        observable.subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<NetGitUser>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(NetGitUser gitUser) {
                        if (null != userCallBack) {
                            userCallBack.onSuccess(gitUser);
                        } else {
                            Log.w(TAG, "userCallBack is null");
                        }
                    }

                    @Override
                    public void onError(Throwable e) {
                        if (null != userCallBack) {
                            userCallBack.onFail(e);
                        } else {
                            Log.w(TAG, "userCallBack is null");
                        }
                    }

                    @Override
                    public void onComplete() {

                    }
                });
    }

}
