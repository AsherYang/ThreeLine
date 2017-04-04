package com.asher.threeline.util;

import android.content.Context;

import java.io.File;

/**
 * Created by ouyangfan on 2017/3/22.
 *
 * 文件工具类
 */
public class FileUtil {

    /**
     * 获取外部SDCard缓存目录
     * @return 缓存目录
     */
    public static File getExternalCacheDir(Context context) {
        return context.getExternalCacheDir();
    }

    /**
     * 设置缓存大小
     * @return 10M
     */
    public static int getCacheSize() {
        return 10 * 1024 * 1024;
    }
}
