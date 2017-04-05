package com.asher.threeline.serve.net.base;

/**
 * Created by ouyangfan on 2017/4/5.
 * <p>
 * 网络接口返回异常
 */
public class HttpResultException extends RuntimeException {

    private final String serverCode;

    public HttpResultException(String serverCode) {
        super(serverCode);
        this.serverCode = serverCode;
    }

    @Override
    public String toString() {
        return "HttpResultException{" +
                "serverCode='" + serverCode + '\'' +
                '}';
    }
}
