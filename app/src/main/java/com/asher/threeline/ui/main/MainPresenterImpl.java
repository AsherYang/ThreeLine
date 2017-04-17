package com.asher.threeline.ui.main;

import com.asher.threeline.db.bean.DbContent;
import com.asher.threeline.serve.data.content.IDbContentServe;
import com.asher.threeline.serve.net.base.OnNetCallBack;
import com.asher.threeline.serve.net.content.INetContentServe;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * presenter 实现类
 */
public class MainPresenterImpl implements MainPresenter {

    private MainView mainView;
    private IDbContentServe dbContentServe;
    private INetContentServe contentNetServe;

    public MainPresenterImpl(MainView mainView, IDbContentServe dbContentServe,
                             INetContentServe contentNetServe) {
        this.mainView = mainView;
        this.dbContentServe = dbContentServe;
        this.contentNetServe = contentNetServe;
    }

    @Override
    public void onBtnClick() {
        // TODO: 2017/4/17 do what you want to do.
    }

    @Override
    public void prepareContentToDb() {
        List<DbContent> dbContents = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            DbContent content = new DbContent();
            content.setSongName("song name = " + i);
            content.setSyncKey((long) i);
            dbContents.add(content);
        }
        dbContentServe.addContentList(dbContents);
    }

    @Override
    public DbContent getContentFromDb(Integer syncKey) {
        return dbContentServe.getContent(syncKey);
    }

    @Override
    public List<DbContent> getAllContentsFromDb() {
        return dbContentServe.getAllContents();
    }

    @Override
    public void getDataFromNet() {
        contentNetServe.getLastData(mCallBack);
    }

    private OnNetCallBack<List<DbContent>> mCallBack = new OnNetCallBack<List<DbContent>>() {
        @Override
        public void onSuccess(List<DbContent> contents) {
            if (null == contents || contents.isEmpty()) {
                return;
            }
            mainView.refreshAdapter(contents);
        }

        @Override
        public void onFail(Throwable throwable) {
            mainView.showClick(throwable.getMessage());
        }
    };
}
