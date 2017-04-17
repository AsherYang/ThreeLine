package com.asher.threeline.ui.main;

import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.db.bean.DbContent;
import com.asher.threeline.serve.data.content.DbContentServeModule;
import com.asher.threeline.serve.net.content.DaggerNetContentServeComponent;
import com.asher.threeline.serve.net.content.NetContentServeComponent;
import com.asher.threeline.serve.net.content.NetContentServeModule;
import com.asher.threeline.ui.base.BaseActivity;

import java.util.ArrayList;
import java.util.List;

import javax.inject.Inject;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

public class MainActivity extends BaseActivity implements MainView {

    @BindView(R.id.tv_show)
    TextView tvShow;
    @BindView(R.id.rv_show)
    RecyclerView rvShow;

    @Inject
    MainPresenter mainPresenter;

    private MainAdapter mainAdapter;
    private List<DbContent> dbContents;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.i("TAG", "onCreate");
        setContentView(R.layout.activity_main);
        ButterKnife.bind(this);
        initData();
        getDataFromDb();
    }

    private void initData() {
//        mainPresenter.prepareContentToDb();
        dbContents = new ArrayList<>();
        mainAdapter = new MainAdapter(this, dbContents);
        RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(this);
        rvShow.setLayoutManager(layoutManager);
        rvShow.setAdapter(mainAdapter);
    }

    /**
     * 每个界面必须的初始化component操作.已经在基类BaseActivity中提供方法.
     */
    @Override
    protected void setupComponent(AppComponent appComponent) {
        Log.i("TAG", "setupComponent");
        // 关键的就是这句话,将appComponent和Module关联起来
        NetContentServeComponent netContentServeComponent = DaggerNetContentServeComponent.builder()
                .appComponent(appComponent)
                .netContentServeModule(new NetContentServeModule())
                .dbContentServeModule(new DbContentServeModule())
                .build();
        DaggerMainComponent.builder()
                .mainModule(new MainModule(this))
                .netContentServeComponent(netContentServeComponent)
                .build()
                .inject(this);
    }

    private void getDataFromDb() {
        refreshAdapter(mainPresenter.getAllContentsFromDb());
    }

    @OnClick(R.id.tv_show)
    void onClick(View view) {
        switch (view.getId()) {
            case R.id.tv_show:
                mainPresenter.onBtnClick();
//                Intent intent = new Intent(MainActivity.this, GithubActivity.class);
//                startActivity(intent);
                mainPresenter.getDataFromNet();
                break;
            default:
                break;
        }
    }

    @Override
    public void showClick(String showText) {
        if (TextUtils.isEmpty(showText)) {
            return;
        }
        Toast.makeText(this, showText, Toast.LENGTH_SHORT).show();
    }

    @Override
    public void refreshAdapter(List<DbContent> contents) {
        if (null == contents || contents.isEmpty()) {
            return;
        }
        dbContents.clear();
        dbContents.addAll(contents);
        mainAdapter.notifyDataSetChanged();
    }
}
