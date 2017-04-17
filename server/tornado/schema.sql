SET SESSION default_storage_engine = "InnoDB";
SET SESSION time_zone = "+8:00";
ALTER DATABASE CHARACTER SET "utf8";

DROP TABLE IF EXISTS musics;
CREATE TABLE musics (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    syncKey VARCHAR(100) NOT NULL,
    updateTime VARCHAR(60),
    songName VARCHAR(100),
    singer VARCHAR(100),
    brief VARCHAR(512),
    imagePath VARCHAR(100)
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