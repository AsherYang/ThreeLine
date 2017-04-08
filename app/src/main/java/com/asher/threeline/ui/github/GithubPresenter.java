package com.asher.threeline.ui.github;

/**
 * Created by ouyangfan on 2017/4/8.
 * <p>
 * github presenter
 */
public interface GithubPresenter {

    void onSearchBtnClick(String userName);

    /**
     * 获取github user
     *
     * @param userName userName
     */
    void getGitHubUser(String userName);
}
