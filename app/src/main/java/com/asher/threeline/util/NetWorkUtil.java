package com.asher.threeline.util;

import android.annotation.TargetApi;
import android.content.Context;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkInfo;
import android.os.Build;
import android.support.annotation.NonNull;

/**
 * Created by ouyangfan on 17/4/4.
 * <p>
 * 网络相关工具类
 * <p>
 * 1. 网络是否可用
 * 2. 网络类型: 数据流量 | WIFI
 */
public class NetWorkUtil {

    /**
     * 网络是否可用
     *
     * @return true:可用
     * false:不可用
     */
    public static boolean isAvailable(@NonNull Context context) {
        ConnectivityManager connMgr = (ConnectivityManager)
                context.getSystemService(Context.CONNECTIVITY_SERVICE);
        if (connMgr == null) {
            return false;
        }

        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
            Network[] networks = connMgr.getAllNetworks();
            if (networks == null) {
                return isAvailableByDep(connMgr);
            }
            NetworkInfo networkInfo;
            for (Network network : networks) {
                networkInfo = connMgr.getNetworkInfo(network);
                if (networkInfo.getState().equals(NetworkInfo.State.CONNECTED)) {
                    return true;
                }
            }
        } else {
            return isAvailableByDep(connMgr);
        }
        return false;
    }

    private static boolean isAvailableByDep(@NonNull ConnectivityManager connMgr) {
        NetworkInfo[] networkInfos = connMgr.getAllNetworkInfo();
        if (networkInfos != null) {
            for (NetworkInfo info : networkInfos) {
                if (info.getState().equals(NetworkInfo.State.CONNECTED)) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * 判断当前网络是否是WIFI网络
     *
     * @param context context
     * @return true: 当前在WIFI网络环境下; false: 非WIFI网络
     */
    public static boolean isWifiConnected(@NonNull Context context) {
        return isConnected(context, ConnectivityManager.TYPE_WIFI);
    }

    /**
     * 判断当前网络是否是移动数据
     *
     * @param context context
     * @return 当前在移动数据网络环境下; false: 非移动数据
     */
    public static boolean isMobileConnected(@NonNull Context context) {
        return isConnected(context, ConnectivityManager.TYPE_MOBILE);
    }

    /**
     * 根据类型判断是否该类型方式联网
     *
     * @param context context
     * @param type    网络类型
     * @return true, false
     */
    private static boolean isConnected(@NonNull Context context, int type) {
        ConnectivityManager connMgr = (ConnectivityManager)
                context.getSystemService(Context.CONNECTIVITY_SERVICE);
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.LOLLIPOP) {
            return isConnectedByNew(connMgr, type);
        } else {
            return isConnectedByDep(connMgr, type);
        }
    }


    @TargetApi(Build.VERSION_CODES.LOLLIPOP)
    private static boolean isConnectedByNew(@NonNull ConnectivityManager connMgr, int type) {
        Network[] networks = connMgr.getAllNetworks();
        if (networks == null) {
            return isConnectedByDep(connMgr, type);
        } else {
            NetworkInfo networkInfo;
            for (Network network : networks) {
                networkInfo = connMgr.getNetworkInfo(network);
                if (networkInfo != null && networkInfo.getType() == type &&
                        networkInfo.isConnected()) {
                    return true;
                }
            }
        }
        return false;
    }

    private static boolean isConnectedByDep(@NonNull ConnectivityManager connMgr, int type) {
        NetworkInfo networkInfo = connMgr.getNetworkInfo(type);
        return networkInfo != null && networkInfo.isConnected();
    }
}
