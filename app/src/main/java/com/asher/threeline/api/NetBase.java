package com.asher.threeline.api;

import java.io.Serializable;

/**
 * Created by ouyangfan on 17/4/4.
 * <p>
 * 网络返回数据基类
 * 由三个部分组成，
 * code表示成功还是失败，0为成功，非0为失败;
 * message是提示内容,如:操作成功
 * 而主要的内容都封装在data里面
 */
public class NetBase<T> implements Serializable{

    /**
     * 网络状态返回码
     */
    private int code;

    /**
     * 提示内容
     */
    private String message;

    /**
     * 返回实际内容
     */
    private T data;

    public int getCode() {
        return code;
    }

    public void setCode(int code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    @Override
    public String toString() {
        return "NetBase{" +
                "code=" + code +
                ", message='" + message + '\'' +
                ", data=" + data +
                '}';
    }
}
