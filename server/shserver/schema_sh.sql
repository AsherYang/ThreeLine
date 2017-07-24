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
