package com.asher.threeline.util;

import android.content.Context;

import java.io.File;

/**
 * Created by ouyangfan on 2017/3/22.
 *
 * 文件工具类
 */
public class FileUtil {

    // httpCache保存目录
    private static final String httpCacheDir = "netCache";

    /**
     * 获取外部SDCard缓存目录
     * @return 缓存目录
     */
    public static File getExternalCacheDir(Context context) {
        return context.getExternalCacheDir();
    }

    /**
     * 获取Http缓存目录
     * @return Http缓存目录
     */
    public static File getHttpCacheDir(Context context) {
        String cacheDir = getExternalCacheDir(context).getAbsolutePath() + httpCacheDir;
        return new File(cacheDir);
    }

    /**
     * 设置缓存大小
     * @return 10M
     */
    public static int getHttpCacheSize() {
        return 10 * 1024 * 1024;
    }
}
