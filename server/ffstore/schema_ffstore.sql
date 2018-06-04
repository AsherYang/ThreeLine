SET SESSION default_storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

-- 用户表
DROP TABLE IF EXISTS ffstore_user;
CREATE TABLE ffstore_user (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    user_tel VARCHAR(20) NOT NULL UNIQUE,
    user_address VARCHAR(512),
    buy_times INT,
    cost_count INT
);

-- 商品表，基础表
-- cate_id 对应ffstore_category表cate_id, brand_id 对应ffstore_brand表brand_id
-- market_price: 市场价(一般指原价), current_price: 现价
-- sale_count: 已卖出件数,  goods_code: 唯一，商品编码(代码)、编号如:T18C076
-- goods_logo: 商品logo,  thum_logo: 商品logo小图
DROP TABLE IF EXISTS ffstore_goods;
CREATE TABLE ffstore_goods (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    goods_id VARCHAR(50) NOT NULL UNIQUE,
    cate_id VARCHAR(50),
    brand_id VARCHAR(50),
    goods_name VARCHAR(150),
    market_price INT,
    current_price INT NOT NULL,
    sale_count INT,
    goods_code VARCHAR(20) NOT NULL UNIQUE,
    goods_logo VARCHAR(200),
    thum_logo VARCHAR(200)
);

-- 分类表，根据分类cate_id，去商品表中查询该分类下的所有商品
-- cate_code 唯一，用于标识一个分类的代码(如:022)
-- parent_code 用于二级目录对应一级目录，对应的一级目录cate_code
-- cate_show_type 表示分类展示类型，默认为0:表示一般展示类型，1: 首页展示；
DROP TABLE IF EXISTS ffstore_category;
CREATE TABLE ffstore_category (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cate_id VARCHAR(50) NOT NULL UNIQUE,
    cate_code INT NOT NULL UNIQUE,
    parent_code INT,
    cate_logo VARCHAR(200),
    cate_name VARCHAR(50),
    cate_show_type VARCHAR(3) DEFAULT 0
);

-- 厂家(品牌)表，根据厂家brand_id, 去商品表中查询该厂家的所有商品
DROP TABLE IF EXISTS ffstore_brand;
CREATE TABLE ffstore_brand (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    brand_id VARCHAR(50) NOT NULL UNIQUE,
    brand_name VARCHAR(30),
    brand_logo VARCHAR(200)
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
-- 根据cate_id, 查出属性表中该分类下的属性
-- attr_market_year: 上市年份
-- attr_size：尺码
-- attr_color: 颜色 该尺码对应的颜色(例如: 30码白色,30码黑色是2条数据记录)
DROP TABLE IF EXISTS ffstore_attr;
CREATE TABLE ffstore_attr (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cate_id VARCHAR(50),
    goods_id VARCHAR(50),
    attr_market_year VARCHAR(20),
    attr_size VARCHAR(5),
    attr_color VARCHAR(10)
);

-- 公告栏表, importance, 数字越大重要性越强，展示时越靠前
DROP TABLE IF EXISTS ffstore_notice;
CREATE TABLE ffstore_notice (
    _id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    notice VARCHAR(200),
    importance INT
);