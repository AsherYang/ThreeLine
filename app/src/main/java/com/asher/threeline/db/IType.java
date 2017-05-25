package com.asher.threeline.db;

/**
 * Created by ouyangfan on 17/3/26.
 * <p>
 * 类型
 */
public interface IType {

    /**
     * invalid type
     */
    int TYPE_INVALID = -1;

    /**
     * music type
     */
    int TYPE_MUSIC = 0;

    /**
     * sentence type
     */
    int TYPE_SENTENCE = 1;

    /**
     * article type
     */
    int TYPE_ARTICLE = 2;

    /**
     * image type
     * image cover whole page
     */
    int TYPE_IMAGE = 3;
}
