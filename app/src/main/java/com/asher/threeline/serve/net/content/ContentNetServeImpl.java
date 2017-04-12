package com.asher.threeline.serve.net.content;

import android.util.Log;

import com.asher.threeline.api.IGetDataHttp;
import com.asher.threeline.serve.net.base.BaseHttpResultPrep;
import com.asher.threeline.serve.net.base.NetBaseResult;
import com.asher.threeline.serve.net.base.OnNetCallBack;
import com.asher.threeline.serve.net.bean.NetContent;

import java.util.List;

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
public class ContentNetServeImpl implements IContentNetServe {

    private IGetDataHttp mGetDataHttp;

    public ContentNetServeImpl(IGetDataHttp getDataHttp) {
        this.mGetDataHttp = getDataHttp;
    }

    @Override
    public void getLastData(final OnNetCallBack<List<NetContent>> callBack) {
        Observable<NetBaseResult<List<NetContent>>> observable = mGetDataHttp.getLastData();
        observable.map(new BaseHttpResultPrep<List<NetContent>>())
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<List<NetContent>>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(List<NetContent> contents) {
                        if (null != callBack) {
                            callBack.onSuccess(contents);
                        } else {
                            Log.w(TAG, "userCallBack is null");
                        }
                    }

                    @Override
                    public void onError(Throwable e) {
                        if (null != callBack) {
                            callBack.onFail(e);
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
