package com.asher.threeline.ui.github;

import android.util.Log;

import com.asher.threeline.serve.net.github.IGitHubNetServe;
import com.asher.threeline.serve.net.github.NetGitUser;
import com.asher.threeline.serve.net.github.OnGetGitUserCallBack;

/**
 * Created by ouyangfan on 2017/4/8.
 * <p>
 * github presenter impl
 */
public class GithubPresenterImpl implements GithubPresenter {

    private GithubView githubView;
    private IGitHubNetServe gitHubNetServe;

    public GithubPresenterImpl(GithubView githubView, IGitHubNetServe gitHubNetServe) {
        this.githubView = githubView;
        this.gitHubNetServe = gitHubNetServe;
    }

    @Override
    public void onSearchBtnClick(String userName) {
        getGitHubUser(userName);
    }

    @Override
    public void getGitHubUser(String userName) {
        gitHubNetServe.getUser(userName, mUserCallBack);
    }

    private OnGetGitUserCallBack mUserCallBack = new OnGetGitUserCallBack() {
        @Override
        public void onSuccess(NetGitUser gitUser) {
            Log.i("TAG", "getUser success = " + gitUser);
            if (null != githubView) {
                githubView.showGitHubUser(gitUser.toString());
            }
        }

        @Override
        public void onFail(Throwable throwable) {
            Log.i("TAG", "getUser fail = " + throwable);
        }
    };

}
