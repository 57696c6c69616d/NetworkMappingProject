<?php

// Doctrine (db)
$app['db.options'] = array(
    'driver'   => 'pdo_mysql',
    'charset'  => 'utf8',
    'host'     => 'localhost',
    'port'     => '3306',
    'dbname'   => 'nmpdb',
    'user'     => 'nmp_user',
    'password' => 'nmp_pa55',
);

// define log level
$app['monolog.level'] = 'WARNING';