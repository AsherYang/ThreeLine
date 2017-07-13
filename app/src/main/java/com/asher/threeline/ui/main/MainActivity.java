package com.asher.threeline.ui.main;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.text.TextUtils;
import android.util.Log;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.db.IType;
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

import java.lang.ref.WeakReference;
import java.util.ArrayList;
import java.util.List;

import javax.inject.Inject;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

import static com.asher.threeline.ui.theme.ThemeHelper.getThemeHelper;

public class MainActivity extends BaseActivity implements MainView {

    private static final String TAG = "MainActivity";

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
    // app 控制常量
    public static final int MSG_PLAY_MUSIC = 0x01;
    public static final int MSG_PAUSE_MUSIC = 0x02;
    private MyHandler mHandler;

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
        titleBar.setRightOnClickListener(mRightMenuOnClickListener);
    }

    private void initData() {
//        mainPresenter.prepareContentToDb();
        dbContents = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            DbContent dbContent = new DbContent();
            dbContent.setAuthor("author = " + i);
            dbContent.setTitle("title = " + i);
            dbContent.setContent("《山月》席慕容 \n\n曾踏月而来,\n只因您在山中,\n山风拂发,\n拂颈,拂裸露的肩膀\n而月光衣我以华裳。\n我\n你\n他\n哈哈");
            if (i == 0) {
                dbContent.setType(IType.TYPE_ARTICLE);
            } else if (i == 1) {
                dbContent.setType(IType.TYPE_MUSIC);
            } else if (i == 2) {
                dbContent.setType(IType.TYPE_SENTENCE);
            } else {
                dbContent.setType(IType.TYPE_IMAGE);
            }
            dbContents.add(dbContent);
        }
        Log.i(TAG, "dbContents size = " + dbContents.size());
        mHandler = new MyHandler(this);
        mainAdapter = new MainAdapter(this, mHandler, dbContents);
        titleBar.setTitleTxt(mainAdapter.getTitle(0));
        viewFlow.setAdapter(mainAdapter);
        viewFlow.setOnViewSwitchListener(new ViewFlow.ViewSwitchListener() {
            @Override
            public void onSwitched(View view, int position) {
                titleBar.setTitleTxt(mainAdapter.getTitle(position));
            }
        });
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
//        refreshAdapter(mainPresenter.getAllContentsFromDb());
    }

    private static class MyHandler extends Handler {
        WeakReference<Context> context;

        MyHandler(Context context) {
            this.context = new WeakReference<>(context);
        }

        @Override
        public void handleMessage(Message msg) {
            switch (msg.what) {
                case MSG_PLAY_MUSIC:
                    Log.i(TAG, "handleMessage: play music ");
                    break;
                case MSG_PAUSE_MUSIC:
                    Log.i(TAG, "handleMessage: pause music ");
                    break;
                default:
                    break;
            }
        }
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
