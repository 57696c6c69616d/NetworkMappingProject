<?php

namespace NMP\DAO;

use NMP\Domain\Machine;

class MachineDAO extends DAO
{
    public function findAll(){
        $sql = "SELECT DISTINCT ip,type,groupe FROM t_address ORDER BY ip ASC";
        $result = $this->getDb()->fetchAll($sql);

        return $result;
    }
	
    public function find($ip) {
        $sql = "SELECT * FROM t_address WHERE ip=?";
        $row = $this->getDb()->fetchAssoc($sql, array($ip));

        if ($row)
            return $this->buildDomainObject($row);
        else
            throw new \Exception("No machine matching ip " . $ip);
    }

    public function NumberOfMachines(){
        $sql = "SELECT DISTINCT COUNT(ip) FROM t_address";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function NumberOfGroups(){
        $sql = "SELECT COUNT(DISTINCT groupe) FROM t_address";
        $result = $this->getDb()->fetchAll($sql);

        return $result[0];
    }

    public function save(Machine $machine){
        $machineData = array(
            'type' => $machine->getType()
            );
        $this->getDb()->update('t_address', $machineData, array('ip' => $machine->getIp()));
    }

    public function save2(Machine $machine){
        $machineData = array(
            'groupe' => $machine->getGroupe()
            );
        $this->getDb()->update('t_address', $machineData, array('ip' => $machine->getIp()));
    }

    protected function buildDomainObject(array $row) {
        $machine = new Machine();
        $machine->setIp($row['ip']);
        $machine->setType($row['type']);
        $machine->setGroupe($row['groupe']);
        return $machine;
    }
}