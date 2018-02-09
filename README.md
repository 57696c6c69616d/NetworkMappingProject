# NetworkMappingProject

## Installation Guide

### For Windows

First, you will need to install Python2.7. (included in tools.zip)

##### <i>Note: I suggest you to enable the option to add Python as an environment variable.</i>

#### Client

Then, install Microsoft Visual C++ Compiler for Python 2.7. (not included)

After, install tshark and the Wireshark libraries from the Wireshark installer. (not included)

##### <i>Note: You are not obliged to install Wireshark.</i>

Also, you will need to install lxml 32bit. (included in tools.zip)

To finish, unzip and install pyshark (command "python setup.py install" in the decompressed pyshark directory). (included in tools.zip)

#### Server

Requirements :
 - Apache2
 - MySQL
 - PHP

Install mysqlconnector. (included in tools.zip)

### For Linux

First, you will need to install Python2.7. (not included)

#### Client

Then, if you don't already have Wireshark, download and install it.

Unzip and install pyshark. (included in tools.zip)

#### Server

Requirements :
 - Apache2
 - MySQL
 - PHP

Install mysqlconnector. (included in tools.zip)

## Usage

### Configuration files

##### WARNING: if the name of the network interface that you use to capture packets is non ascii, please rename it.

#### Client

You have to set the ip of the server, the network interface you are listening on and the port of the server.

#### Server

You have to set the ip of the server and the port on which you are listening.

##### Note: the parameters have to be between quotes. (ex: ip = '0.0.0.0')
