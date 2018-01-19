<?php

namespace NMP\DAO;

use NMP\Domain\Packet;

class PacketDAO extends DAO
{
    public function ListAllIp(){
        $sql = "SELECT DISTINCT ip FROM t_address ORDER BY ip ASC";
        $result = $this->getDb()->fetchAll($sql);

        return $result;
    }

    public function findAll() {
        $sql = "SELECT source,mac_src,port_src,prtcl_hl,prtcl_tl,target,mac_dst,port_dst,value FROM t_packets";
        $result = $this->getDb()->fetchAll($sql);

        // Convert query result to an array of domain objects
        // $packets = array();
        // foreach ($result as $row) {
        //     $packetId = $row['id'];
        //     $packets[$packetId] = $this->buildDomainObject($row);
        // }
        return $result;
    }
	
    public function find($ip) {
        $sql = "SELECT * FROM t_packets WHERE source=?";
        $row = $this->getDb()->fetchAssoc($sql, array($ip));

        if ($row)
            return $this->buildDomainObject($row);
        else
            throw new \Exception("No packet matching ip " . $ip);
    }

    public function NumberOfIp(){
        $sql = "SELECT DISTINCT COUNT(ip) FROM t_address";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function NumberOfPackets(){
        $sql = "SELECT COUNT(*) FROM t_packets";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function NumberOfTCPPackets(){
        $sql = "SELECT COUNT(prtcl_tl) FROM t_packets WHERE prtcl_tl='TCP'";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function NumberOfUDPPackets(){
        $sql = "SELECT COUNT(prtcl_tl) FROM t_packets WHERE prtcl_tl='UDP'";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function FirstDate(){
        $sql = "SELECT date FROM t_packets LIMIT 1";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function LastDate(){
        $sql = "SELECT date FROM t_packets ORDER BY id DESC LIMIT 1";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    protected function buildDomainObject(array $row) {
        $packet = new Packet();
        $packet->setId($row['id']);
        $packet->setIpSrc($row['source']);
        $packet->setPortSrc($row['port_src']);
        $packet->setProtocolHl($row['prtcl_hl']);
        $packet->setProtocolTl($row['prtcl_tl']);
        $packet->setIpDst($row['target']);
        $packet->setPortDst($row['port_dst']);
        return $packet;
    }
}