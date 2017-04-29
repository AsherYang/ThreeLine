package com.asher.threeline.ui.github;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.asher.threeline.AppComponent;
import com.asher.threeline.R;
import com.asher.threeline.serve.net.github.DaggerGitUserNetServeComponent;
import com.asher.threeline.serve.net.github.GitUserNetServeComponent;
import com.asher.threeline.serve.net.github.GitUserNetServeModule;
import com.asher.threeline.ui.base.BaseActivity;

import javax.inject.Inject;

import butterknife.BindView;
import butterknife.ButterKnife;
import butterknife.OnClick;

/**
 * Created by ouyangfan on 2017/4/8.
 * <p>
 * github activity
 */
public class GithubActivity extends BaseActivity implements GithubView {

    @BindView(R.id.et_name)
    EditText etName;
    @BindView(R.id.tv_msg)
    TextView tvMsg;
    @BindView(R.id.btn_search)
    Button btnSearch;

    @Inject
    GithubPresenter githubPresenter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_github);
        ButterKnife.bind(this);
    }

    @Override
    protected void setupComponent(AppComponent appComponent) {
        GitUserNetServeComponent gitUserNetServeComponent = DaggerGitUserNetServeComponent.builder()
                .appComponent(appComponent)
                .gitUserNetServeModule(new GitUserNetServeModule())
                .build();
        DaggerGithubComponent.builder()
                .gitUserNetServeComponent(gitUserNetServeComponent)
                .githubModule(new GithubModule(this))
                .build()
                .inject(this);
    }

    @OnClick({R.id.btn_search})
    void onClick(View view) {
        switch (view.getId()) {
            case R.id.btn_search:
                String userName = etName.getText().toString();
                githubPresenter.onSearchBtnClick(userName);
                break;
            default:
                break;
        }
    }

    @Override
    public void showGitHubUser(String msg) {
        tvMsg.setText(msg);
    }
}
