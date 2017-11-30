<?php

use Symfony\Component\HttpFoundation\Request;

// Home page
$app->get('/', function () use ($app) {
	$localIP = getHostByName(getHostName());
    return $app['twig']->render('index.html.twig', array('localIP' => $localIP));
})->bind('home');

// Graph page
$app->get('/graph', function () use ($app) {
	$localIP = getHostByName(getHostName());
    return $app['twig']->render('graph.html.twig', array('localIP' => $localIP));
})->bind('graph');