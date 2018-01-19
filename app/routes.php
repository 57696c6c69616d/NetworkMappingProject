<?php

use Symfony\Component\HttpFoundation\Request;

// Home page
$app->get('/', function () use ($app) {
	$localIP = getHostByName(getHostName());
    return $app['twig']->render('index.html.twig', array('localIP' => $localIP));
})->bind('home');

// Graph page
$app->get('/graph', function () use ($app) {
	$localIP = $_SERVER['REMOTE_ADDR'];

	$nbIP = $app['dao.packet']->NumberOfIp()['COUNT(ip)'];

	$nbPackets = $app['dao.packet']->NumberOfPackets()['COUNT(*)'];

	$nbTCPPackets = $app['dao.packet']->NumberOfTCPPackets()['COUNT(prtcl_tl)'];

	$nbUDPPackets = $app['dao.packet']->NumberOfUDPPackets()['COUNT(prtcl_tl)'];

	$percentage = ((int)$nbUDPPackets / (int)$nbPackets)*100;

	$first_date = $app['dao.packet']->FirstDate()['date'];

	$last_date = $app['dao.packet']->LastDate()['date'];

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

    return $app['twig']->render('graph.html.twig', array('localIP' => $localIP, 'nbIP' => $nbIP, 'nbPackets' => $nbPackets, 'nbTCPPackets' => $nbTCPPackets, 'nbUDPPackets' => $nbUDPPackets, 'percentage' => $percentage, 'first_date' => $first_date, 'last_date' => $last_date));
})->bind('graph');