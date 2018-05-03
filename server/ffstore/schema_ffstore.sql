SET SESSION default_storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

-- 用户表
DROP TABLE IF EXISTS ffstore_user;
CREATE TABLE ffstore_user (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    user_tel VARCHAR(20),
    user_address VARCHAR(512)
);

-- 商品表，基础表
DROP TABLE IF EXISTS ffstore_goods;
CREATE TABLE ffstore_goods (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goods_id VARCHAR(50),
    cate_id VARCHAR(50),
    business_id VARCHAR(50),
    goods_name VARCHAR(150),
    market_price INT,
    current_price INT NOT NULL,
    sale_count INT,
    goods_code VARCHAR(20),
    goods_logo VARCHAR(200),
    thum_logo VARCHAR(200)
);

-- 分类表，根据分类cate_id，去商品表中查询该分类下的所有商品
DROP TABLE IF EXISTS ffstore_category;
CREATE TABLE ffstore_category (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cate_id VARCHAR(50),
    cate_code INT,
    cate_logo VARCHAR(200),
    cate_name VARCHAR(50)
);

-- 厂家表，根据厂家business_id, 去商品表中查询该厂家的所有商品
DROP TABLE IF EXISTS ffstore_brand;
CREATE TABLE ffstore_brand (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    brand_name VARCHAR(30),
    business_id VARCHAR(50),
    business_name VARCHAR(100),
    business_logo VARCHAR(200)
);

-- 图片表，根据goods_id，查出图片表中该商品对应的所有图片
DROP TABLE IF EXISTS ffstore_photo;
CREATE TABLE ffstore_photo (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goods_id VARCHAR(50),
    photo VARCHAR(200),
    thum_photo VARCHAR(200)
);

-- 属性表，存储描述分类或者商品的属性，分类或者商品可1对多个属性
-- 根据goods_id, 查出属性表中该商品对应的所有属性
DROP TABLE IF EXISTS ffstore_attribute;
CREATE TABLE ffstore_attribute (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    attr_name VARCHAR(50),
    attr_val VARCHAR(150),
    cate_id VARCHAR(50),
    goods_id VARCHAR(50)
);