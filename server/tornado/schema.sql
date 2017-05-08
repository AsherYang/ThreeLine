SET SESSION default_storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS devices;
CREATE TABLE devices (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    deviceType VARCHAR(2) NOT NULL,
    deviceName VARCHAR(30),
    deviceId VARCHAR(10),
    phoneBrand VARCHAR(10),
    androidBuildVersion VARCHAR(5),
    androidBuildLevel VARCHAR(5),
    firstRegisterTime VARCHAR(60),
    lastOnlineTime VARCHAR(60)
);

DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    syncKey VARCHAR(100) NOT NULL,
    updateTime VARCHAR(60),
    title VARCHAR(100),
    content VARCHAR(512),
    author VARCHAR(100),
    imagePath VARCHAR(100)
);

DROP TABLE IF EXISTS contents;
CREATE TABLE contents (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    syncKey VARCHAR(100) NOT NULL,
    updateTime VARCHAR(60),
    title VARCHAR(100),
    content VARCHAR(512),
    author VARCHAR(100),
    imagePath VARCHAR(100),
    songName VARCHAR(100),
    singer VARCHAR(100)
);