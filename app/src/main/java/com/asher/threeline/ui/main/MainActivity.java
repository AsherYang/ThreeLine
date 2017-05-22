package com.asher.threeline.ui.main;

import android.content.Intent;
import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.db.bean.DbContent;
import com.asher.threeline.serve.data.content.DbContentServeModule;
import com.asher.threeline.serve.net.content.DaggerNetContentServeComponent;
import com.asher.threeline.serve.net.content.NetContentServeComponent;
import com.asher.threeline.serve.net.content.NetContentServeModule;
import com.asher.threeline.ui.base.BaseActivity;
import com.asher.threeline.ui.setting.SettingActivity;
import com.asher.threeline.ui.theme.Theme;
import com.asher.threeline.ui.theme.ThemeHelper;
import com.asher.threeline.ui.view.TitleBar;
import com.asher.viewflow.ViewFlow;

import java.util.ArrayList;
import java.util.List;

import javax.inject.Inject;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

import static com.asher.threeline.ui.theme.ThemeHelper.getThemeHelper;

public class MainActivity extends BaseActivity implements MainView {

    @BindView(R.id.title_bar)
    TitleBar titleBar;
    @BindView(R.id.view_flow)
    ViewFlow viewFlow;
    @BindView(R.id.iv_star)
    ImageView ivStar;

    @Inject
    MainPresenter mainPresenter;

    private MainAdapter mainAdapter;
    private List<DbContent> dbContents;
    private boolean isStar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.i("TAG", "onCreate");
        setContentView(R.layout.activity_main);
        ButterKnife.bind(this);
        initView();
        initData();
        getDataFromDb();
    }

    private void initView() {
        viewFlow.setAdapter(new ImageAdapter(this));
        titleBar.setRightOnClickListener(mRightMenuOnClickListener);
    }

    private void initData() {
//        mainPresenter.prepareContentToDb();
        dbContents = new ArrayList<>();
        mainAdapter = new MainAdapter(this, dbContents);
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

    @OnClick({R.id.iv_star, R.id.iv_share})
    void onClick(View view) {
        switch (view.getId()) {
            case R.id.iv_star:
//                mainPresenter.onBtnClick();
//                Intent intent = new Intent(MainActivity.this, GithubActivity.class);
//                startActivity(intent);
//                mainPresenter.getDataFromNet();
                changeStarImage(isStar);
                isStar = !isStar;
                break;
            case R.id.iv_share:
                // 为了验证改变主题对其他页面的影响,这里延迟5S用于测试
//                changeThemeDelay();
//                Intent intent2 = new Intent(MainActivity.this, SettingActivity.class);
//                startActivity(intent2);
//                getThemeHelper(this).changeTheme(exchangeTheme());
                break;
            default:
                break;
        }
    }

    private void changeStarImage(boolean isStared) {
        if (isStared) {
            ivStar.setImageResource(R.drawable.star_press);
        } else {
            ivStar.setImageResource(R.drawable.star_normal);
        }
    }

    private View.OnClickListener mRightMenuOnClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            Intent intent2 = new Intent(MainActivity.this, SettingActivity.class);
            startActivity(intent2);
        }
    };

    public Theme exchangeTheme() {
        ThemeHelper helper = getThemeHelper(this);
        if (helper.getBaseTheme() == Theme.LIGHT) {
            return Theme.DARK;
        }
        return Theme.LIGHT;
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
