SET SESSION default_storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS sh_user;
CREATE TABLE sh_user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userName VARCHAR(512),
    userTel VARCHAR(50),
    userAddress VARCHAR(512)
);

DROP TABLE IF EXISTS sh_token;
CREATE TABLE sh_token (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    access_token VARCHAR(512),
    expire_in VARCHAR(20),
    update_time VARCHAR(60)
);

DROP TABLE IF EXISTS sh_category;
CREATE TABLE sh_category (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cate_id VARCHAR(50),
    cate_name VARCHAR(100),
    parent_id VARCHAR(50),
    parent_cate_name VARCHAR(100),
    sort_num VARCHAR(5),
    cate_item_num VARCHAR(20),
    description VARCHAR(100),
    listUrl VARCHAR(300),
    shopName VARCHAR(20),
    shopLogo VARCHAR(100),
    update_time VARCHAR(60)
);

DROP TABLE IF EXISTS sh_goods;
CREATE TABLE sh_goods (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cate_id VARCHAR(50),
    itemid VARCHAR(100),
    item_desc VARCHAR(150),
    item_name VARCHAR(100),
    imgs VARCHAR(300),
    price VARCHAR(10),
    update_time VARCHAR(60)
);