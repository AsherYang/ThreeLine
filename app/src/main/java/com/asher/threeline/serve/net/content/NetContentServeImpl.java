package com.asher.threeline.serve.net.content;

import android.util.Log;

import com.asher.threeline.api.IGetDataHttp;
import com.asher.threeline.db.bean.DbContent;
import com.asher.threeline.serve.data.content.IDbContentServe;
import com.asher.threeline.serve.net.base.BaseHttpResultPrep;
import com.asher.threeline.serve.net.base.NetBaseResult;
import com.asher.threeline.serve.net.base.OnNetCallBack;
import com.asher.threeline.serve.net.bean.NetContent;
import com.asher.threeline.serve.net.util.NetConvert2Db;

import java.util.ArrayList;
import java.util.List;

import io.reactivex.Observable;
import io.reactivex.Observer;
import io.reactivex.android.schedulers.AndroidSchedulers;
import io.reactivex.disposables.Disposable;
import io.reactivex.functions.Function;
import io.reactivex.schedulers.Schedulers;

import static android.content.ContentValues.TAG;

/**
 * Created by ouyangfan on 2017/4/6.
 * <p>
 * 网络接口实现类
 */
public class NetContentServeImpl implements INetContentServe {

    private IGetDataHttp mGetDataHttp;
    private IDbContentServe mDbContentServe;

    public NetContentServeImpl(IGetDataHttp getDataHttp, IDbContentServe contentServe) {
        this.mGetDataHttp = getDataHttp;
        this.mDbContentServe = contentServe;
    }

    @Override
    public void getLastData(final OnNetCallBack<List<DbContent>> callBack) {
        Observable<NetBaseResult<List<NetContent>>> observable = mGetDataHttp.getLastData();
        observable.map(new BaseHttpResultPrep<List<NetContent>>())
                .map(updateDbFuc())
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Observer<List<DbContent>>() {
                    @Override
                    public void onSubscribe(Disposable d) {

                    }

                    @Override
                    public void onNext(List<DbContent> contents) {
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

    private Function<List<NetContent>, List<DbContent>> updateDbFuc() {
        return new Function<List<NetContent>, List<DbContent>>() {
            @Override
            public List<DbContent> apply(List<NetContent> netContents) throws Exception {
                List<DbContent> dbContents = new ArrayList<>();
                if (null == netContents || netContents.isEmpty()) {
                    return dbContents;
                }
                dbContents = NetConvert2Db.toDbContents(netContents);
                if (dbContents.isEmpty()) {
                    return dbContents;
                }
                mDbContentServe.addContentList(dbContents);
                return dbContents;
            }
        };
    }
}
