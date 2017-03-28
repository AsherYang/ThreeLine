package com.asher.threeline.ui.main;

import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.db.bean.DbMusic;
import com.asher.threeline.serve.music.DbMusicServeModule;
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
    private List<DbMusic> dbMusics;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        ButterKnife.bind(this);
        initData();
        getDataFromDb();
    }

    private void initData() {
        mainPresenter.prepareMusicToDb();
        dbMusics = new ArrayList<>();
        mainAdapter = new MainAdapter(this, dbMusics);
        RecyclerView.LayoutManager layoutManager = new LinearLayoutManager(this);
        rvShow.setLayoutManager(layoutManager);
        rvShow.setAdapter(mainAdapter);
    }

    private void getDataFromDb() {
        List<DbMusic> musics = mainPresenter.getAllMusicsFromDb();
        dbMusics.clear();
        dbMusics.addAll(musics);
        mainAdapter.notifyDataSetChanged();
    }

    /**
     * 每个界面必须的初始化component操作.已经在基类BaseActivity中提供方法.
     */
    @Override
    protected void setupComponent(AppComponent appComponent) {
        // 关键的就是这句话,将appComponent和Module关联起来
        DaggerMainComponent.builder()
                .appComponent(appComponent)
                .mainModule(new MainModule(this))
                .dbMusicServeModule(new DbMusicServeModule())
                .build()
                .inject(this);
    }

    @OnClick(R.id.tv_show)
    void onClick(View view) {
        switch (view.getId()) {
            case R.id.tv_show:
                mainPresenter.onBtnClick();
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
}
