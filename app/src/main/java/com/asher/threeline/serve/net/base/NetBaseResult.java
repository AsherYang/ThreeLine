package com.asher.threeline.serve.net.base;

import java.io.Serializable;

/**
 * Created by ouyangfan on 17/4/4.
 * <p>
 * 网络返回数据基类
 * 由三个部分组成，
 * code表示成功还是失败，000001为成功，非000001为失败;
 * desc是提示内容,如:操作成功
 * 而主要的内容都封装在data里面
 */
public class NetBaseResult<T> implements Serializable {

    /**
     * 返回成功状态码
     */
    public static final String SUCCESS = "000001";

    /**
     * 网络状态返回码
     */
    private String code;

    /**
     * 提示描述内容
     */
    private String desc;

    /**
     * 返回实际内容
     */
    private T data;

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getDesc() {
        return desc;
    }

    public void setDesc(String desc) {
        this.desc = desc;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }

    @Override
    public String toString() {
        return "NetBaseResult{" +
                "code=" + code +
                ", desc='" + desc + '\'' +
                ", data=" + data +
                '}';
    }
}
