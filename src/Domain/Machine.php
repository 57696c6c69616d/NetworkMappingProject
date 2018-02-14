<?php

namespace NMP\Domain;

class Machine 
{
    private $ip;
    private $type;
    private $groupe;

    public function getIp() {
        return $this->ip;
    }

    public function setIp($ip) {
        $this->ip = $ip;
        return $this;
    }

    public function getType() {
        return $this->type;
    }

    public function setType($type) {
        $this->type = $type;
        return $this;
    }

    public function getGroupe() {
        return $this->groupe;
    }

    public function setGroupe($groupe) {
        $this->groupe = $groupe;
        return $this;
    }
}