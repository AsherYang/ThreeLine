SET SESSION default_storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS sh_user;
CREATE TABLE sh_user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userName VARCHAR(60),
    userTel VARCHAR(20),
    userAddress VARCHAR(120)
);
