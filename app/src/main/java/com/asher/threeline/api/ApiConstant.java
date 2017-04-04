package com.asher.threeline.api;

/**
 * Created by ouyangfan on 2017/3/22.
 * <p>
 * 定义服务器接口API常量
 */
public class ApiConstant {
    /**
     * BASE_URL
     */
    public static final String BASE_URL = "https://api.github.com";

    /**
     * 连接超时时间
     * 15s
     */
    public static final int CONNECT_TIMEOUT = 15;

    /**
     * 读取超时时间
     * 20s
     */
    public static final int READ_TIMEOUT = 20;

    /**
     * 写超时时间
     * 20s
     */
    public static final int WRITE_TIMEOUT = 20;
}
