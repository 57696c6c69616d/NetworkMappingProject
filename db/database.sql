create database if not exists nmpdb character set utf8 collate utf8_unicode_ci;
use nmpdb;

grant all privileges on nmpdb.* to 'nmp_user'@'localhost' identified by 'nmp_pa55';