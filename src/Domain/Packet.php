<?php

namespace NMP\Domain;

class Packet 
{
    private $id;
    private $ip_src;
    private $port_src;
    private $prtcl_hl;
    private $prtcl_tl;
    private $ip_dst;
    private $port_dst;

    public function getId() {
        return $this->id;
    }

    public function setId($id) {
        $this->id = $id;
        return $this;
    }

    public function getIpSrc() {
        return $this->ip_src;
    }

    public function setIpSrc($ip) {
        $this->ip_src = $ip;
        return $this;
    }

    public function getPortSrc() {
        return $this->port_src;
    }

    public function setPortSrc($port) {
        $this->port_src = $port;
        return $this;
    }

    public function getProtocolHl() {
        return $this->prtcl_hl;
    }

    public function setProtocolHl($prtcl) {
        $this->prtcl_hl = $prtcl;
        return $this;
    }

    public function getProtocolTl() {
        return $this->prtcl_tl;
    }

    public function setProtocolTl($prtcl) {
        $this->prtcl_tl = $prtcl;
        return $this;
    }

    public function getIpDst() {
        return $this->ip_dst;
    }

    public function setIpDst($ip) {
        $this->ip_dst = $ip;
        return $this;
    }

    public function getPortDst() {
        return $this->port_dst;
    }

    public function setPortDst($port) {
        $this->port_dst = $port;
        return $this;
    }
}