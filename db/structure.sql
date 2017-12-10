drop table if exists t_packets;
drop table if exists t_address;

create table t_packets (
	pkt_id Integer not null primary key auto_increment,
    pkt_ip_src varchar(15) not null,
    pkt_port_src Integer(5) not null,
    pkt_prtcl_hl varchar(5) not null,
    pkt_prtcl_tl varchar(5),
    pkt_ip_dst varchar(15) not null,
    pkt_port_dst Integer(5) not null
) engine=innodb character set utf8 collate utf8_unicode_ci;

create table t_address (
	ip varchar(15) not null primary key
) engine=innodb character set utf8 collate utf8_unicode_ci;