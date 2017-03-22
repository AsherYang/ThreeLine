package com.asher.threeline.ui.main;

/**
 * Created by ouyangfan on 2017/3/22.
 */

public class MainPresenterImpl implements MainPresenter {

    private MainView mainView;

    public MainPresenterImpl(MainView mainView) {
        this.mainView = mainView;
    }

    @Override
    public void onBtnClick() {
        mainView.showClick();
    }
}
