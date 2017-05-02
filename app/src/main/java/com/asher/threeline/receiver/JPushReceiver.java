package com.asher.threeline.receiver;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

/**
 * Created by ouyangfan on 2017/5/2.
 *
 * 极光推送receiver
 */
public class JPushReceiver extends BroadcastReceiver {

    private static final String ACTION_REGISTRATION = "cn.jpush.android.intent.REGISTRATION";
    // Required 用户接收SDK消息的intent
    private static final String ACTION_MESSAGE_RECEIVED = "cn.jpush.android.intent.MESSAGE_RECEIVED";
    // Required 用户接收SDK通知栏信息的intent
    private static final String ACTION_NOTIFICATION_RECEIVED = "cn.jpush.android.intent.NOTIFICATION_RECEIVED";
    //  Required 用户打开自定义通知栏的intent
    private static final String ACTION_NOTIFICATION_OPENED = "cn.jpush.android.intent.NOTIFICATION_OPENED";
    // 接收网络变化 连接/断开
    private static final String ACTION_CONNECTION = "cn.jpush.android.intent.CONNECTION";

    @Override
    public void onReceive(Context context, Intent intent) {
        String action = intent.getAction();
        if (action == null) {
            return;
        }
        Log.i("TAG", "JPushReceiver action = " + action);
        switch (action) {
            case ACTION_REGISTRATION:
                break;
            case ACTION_MESSAGE_RECEIVED:
                break;
            case ACTION_NOTIFICATION_RECEIVED:
                break;
            case ACTION_NOTIFICATION_OPENED:
                break;
            case ACTION_CONNECTION:
                break;
            default:
                break;
        }
    }
}
