drop table if exists t_packets;
drop table if exists t_address;

create table t_packets (
	id Integer not null primary key auto_increment,
    source varchar(15) not null,
    port_src Integer(5) not null,
    prtcl_hl varchar(5) not null,
    prtcl_tl varchar(5),
    target varchar(15) not null,
    port_dst Integer(5) not null,
    value Integer(11) DEFAULT 1 not null
) engine=innodb character set utf8 collate utf8_unicode_ci;

create table t_address (
	ip varchar(15) not null primary key
) engine=innodb character set utf8 collate utf8_unicode_ci;