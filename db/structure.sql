drop table if exists t_packets;
drop table if exists t_address;
drop table if exists t_links;
drop trigger if exists trigger_update_links;
drop trigger if exists trigger_update_ip1;
drop trigger if exists trigger_update_ip2;
#drop table if exists t_protocols;

create table t_packets (
	id Integer(11) not null primary key auto_increment,
    source varchar(15) not null,
    mac_src varchar(17) not null,
    port_src varchar(5),
    prtcl_hl varchar(15) not null,
    prtcl_tl varchar(5),
    target varchar(15) not null,
    mac_dst varchar(17) not null,
    port_dst varchar(5),
    length Integer(11) unsigned not null,
    _date datetime DEFAULT CURRENT_TIMESTAMP not null
) engine=innodb character set utf8 collate utf8_unicode_ci;

create table t_address (
	ip varchar(15) not null primary key,
    type varchar(1) DEFAULT 'U' not null,
    groupe Integer(11) DEFAULT 1 not null
) engine=innodb character set utf8 collate utf8_unicode_ci;

create table t_links (
    id Integer(11) not null primary key auto_increment,
    source varchar(15) not null,
    target varchar(15) not null,
    value Integer(11) DEFAULT 1 not null
) engine=innodb character set utf8 collate utf8_unicode_ci;

#A ajouter à la main...
#CREATE TRIGGER trigger_update_links AFTER INSERT ON t_packets FOR EACH ROW BEGIN SET @COUNT=(SELECT COUNT(*) FROM t_links WHERE (source=NEW.source AND target=NEW.target)); IF (@COUNT=0) THEN INSERT INTO t_links (source,target) VALUES(NEW.source,NEW.target); ELSE UPDATE t_links SET value=value+1 WHERE (source=NEW.source AND target=NEW.target); END IF; END;
CREATE TRIGGER trigger_update_ip1 AFTER INSERT ON t_packets FOR EACH ROW INSERT IGNORE INTO t_address (ip) VALUES(NEW.source);
CREATE TRIGGER trigger_update_ip2 AFTER INSERT ON t_packets FOR EACH ROW INSERT IGNORE INTO t_address (ip) VALUES(NEW.target);
#create table t_protocols (
#	code Integer(3) not null primary key,
#	prtcl varchar(15),
#) engine=innodb character set utf8 collate utf8_unicode_ci;