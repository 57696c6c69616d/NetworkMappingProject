<?php

// include the prod configuration
require __DIR__.'/prod.php';

// enable the debug mode
$app['debug'] = true;

// Doctrine (db)
$app['db.options'] = array(
    'driver'   => 'pdo_mysql',
    'charset'  => 'utf8',
    'host'     => '127.0.0.1',  // Mandatory for PHPUnit testing
    'port'     => '3306',
    'dbname'   => 'nmpdb',
    'user'     => 'nmp_user',
    'password' => 'nmp_pa55',
);

// define log level
$app['monolog.level'] = 'INFO';