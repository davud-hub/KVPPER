DROP DATABASE kappersapp;
DROP USER 'kapper'@'localhost';

CREATE DATABASE kappersapp;

USE kappersapp;

CREATE user 'kapper'@'localhost' IDENTIFIED BY 'macvoet';
GRANT ALL PRIVILEGES ON *.* TO 'kapper'@'localhost';

CREATE TABLE afspraak (
    id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
    naam VARCHAR(256) NOT NULL,
    email VARCHAR(256) NOT NULL,
    tijdstip DATETIME NOT NULL
);