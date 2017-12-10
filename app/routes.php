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

	$file = fopen('..\cap\cap.json', 'w+');
	$json = '{"nodes": ';
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}

	$data = $app['dao.packet']->ListAllIp();
	$json = json_encode($data);
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	if (fwrite($file, ', "links": ') === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	
	$data = $app['dao.packet']->findAll();
	$json = json_encode($data, JSON_NUMERIC_CHECK);
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	if (fwrite($file, '}') === false) { 
		echo "Cannot write to text file. <br />"; 
	}

    return $app['twig']->render('graph.html.twig', array('localIP' => $localIP));
})->bind('graph');