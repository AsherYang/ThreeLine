package com.asher.threeline.util;

import android.content.Context;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkInfo;
import android.support.annotation.NonNull;

/**
 * Created by ouyangfan on 17/4/4.
 * <p>
 * 网络相关工具类
 * <p>
 * 1. 网络是否可用
 * 2. 网络类型: 2G,3G,4G, WIFI
 */
public class NetWorkUtil {

    /**
     * 网络是否可用
     *
     * @return true:可用
     * false:不可用
     */
    public static boolean isAvailable(@NonNull Context context) {
        ConnectivityManager manager = (ConnectivityManager)
                context.getSystemService(Context.CONNECTIVITY_SERVICE);
        if (manager == null ) {
            return false;
        }

        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
            Network[] networks = manager.getAllNetworks();
            if (networks == null) {
                return isAvailableByDep(manager);
            }
            NetworkInfo networkInfo;
            for (Network network : networks) {
                networkInfo = manager.getNetworkInfo(network);
                if (networkInfo.getState().equals(NetworkInfo.State.CONNECTED)) {
                    return true;
                }
            }
        } else {
            return isAvailableByDep(manager);
        }
        return false;
    }

    private static boolean isAvailableByDep(ConnectivityManager manager) {
        NetworkInfo[] networkInfos = manager.getAllNetworkInfo();
        if (networkInfos != null) {
            for (NetworkInfo info : networkInfos) {
                if (info.getState().equals(NetworkInfo.State.CONNECTED)) {
                    return true;
                }
            }
        }
        return false;
    }

}
