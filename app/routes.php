<?php

use Symfony\Component\HttpFoundation\Request;
use NMP\Domain\Packet;
use NMP\Domain\Machine;
use NMP\Form\Type\MachineType;
use NMP\Form\Group\MachineGroup;

// Home page
$app->get('/', function () use ($app) {
	$localIP = $_SERVER['REMOTE_ADDR'];
    return $app['twig']->render('index.html.twig', array('localIP' => $localIP));
})->bind('home');

// Graph page
$app->match('/graph', function(Request $request) use ($app) {
	$localIP = $_SERVER['REMOTE_ADDR'];

	#Statistics
	$nbIP = $app['dao.machine']->NumberOfMachines()['COUNT(ip)'];

	$nbPackets = $app['dao.packet']->NumberOfPackets()['COUNT(*)'];

	$nbTCPPackets = $app['dao.packet']->NumberOfTCPPackets()['COUNT(prtcl_tl)'];

	$nbUDPPackets = $app['dao.packet']->NumberOfUDPPackets()['COUNT(prtcl_tl)'];

	$totalLength = $app['dao.packet']->TotalLength()['SUM(length)'];

	if((int)$nbPackets != 0) {
		$percentage = ((int)$nbUDPPackets / (int)$nbPackets)*100;
	}else{
		$percentage = 0;
	}

	$first_date = $app['dao.packet']->FirstDate()['_date'];

	$last_date = $app['dao.packet']->LastDate()['_date'];

	$nbGroups = $app['dao.machine']->NumberOfGroups()['COUNT(DISTINCT groupe)'];

	#Graph
	$file = fopen('cap\cap.json', 'w+');
	$json = '{"nodes": ';
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />";
	}

	$data = $app['dao.machine']->findAll();
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
	if (fwrite($file, ', "info": ') === false) { 
		echo "Cannot write to text file. <br />"; 
	}

	$data = $app['dao.packet']->getInfo();
	$json = json_encode($data, JSON_NUMERIC_CHECK);
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	if (fwrite($file, '}') === false) { 
		echo "Cannot write to text file. <br />"; 
	}

	#Customize
	$machine = new Machine();
	$machineForm = $app['form.factory']->create(MachineType::class, $machine);
	$machineForm->handleRequest($request);
	if ($machineForm->isSubmitted() && $machineForm->isValid()) {
		$app['dao.machine']->save($machine);
		$app['session']->getFlashBag()->add('success', 'Parameters successfully submitted.');
	}

	$machineForm2 = $app['form.factory']->create(MachineGroup::class, $machine);
	$machineForm2->handleRequest($request);
	if ($machineForm2->isSubmitted() && $machineForm2->isValid()) {
		$app['dao.machine']->save2($machine);
		$app['session']->getFlashBag()->add('success', 'Parameters successfully submitted.');
	}

    return $app['twig']->render('graph.html.twig', array('localIP' => $localIP, 'nbIP' => $nbIP, 'nbPackets' => $nbPackets, 'nbTCPPackets' => $nbTCPPackets, 'nbUDPPackets' => $nbUDPPackets, 'percentage' => $percentage, 'first_date' => $first_date, 'last_date' => $last_date, 'totalLength' => $totalLength, 'nbGroups' => $nbGroups, 'machineForm' => $machineForm->createView(), 'machineForm2' => $machineForm2->createView()));
})->bind('graph');

// Data page
$app->get('/data', function () use ($app) {

	$localIP = $_SERVER['REMOTE_ADDR'];

	#Statistics
	$nbIP = $app['dao.machine']->NumberOfMachines()['COUNT(ip)'];

	$nbPackets = $app['dao.packet']->NumberOfPackets()['COUNT(*)'];

	$nbTCPPackets = $app['dao.packet']->NumberOfTCPPackets()['COUNT(prtcl_tl)'];

	$nbUDPPackets = $app['dao.packet']->NumberOfUDPPackets()['COUNT(prtcl_tl)'];

	$totalLength = $app['dao.packet']->TotalLength()['SUM(length)'];

	if((int)$nbPackets != 0) {
		$percentage = ((int)$nbUDPPackets / (int)$nbPackets)*100;
	}else{
		$percentage = 0;
	}

	$first_date = $app['dao.packet']->FirstDate()['_date'];

	$last_date = $app['dao.packet']->LastDate()['_date'];

	$nbGroups = $app['dao.machine']->NumberOfGroups()['COUNT(DISTINCT groupe)'];

	#Graph
	$file = fopen('cap\cap.json', 'w+');
	$json = '{"nodes": ';
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />";
	}
	$test = $json;

	$data = $app['dao.machine']->findAll();
	$json = json_encode($data);
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	$test = $test . $json;
	if (fwrite($file, ', "links": ') === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	$test = $test . ', "links": ';
	
	$data = $app['dao.packet']->findAll();
	$json = json_encode($data, JSON_NUMERIC_CHECK);
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	$test = $test . $json;
	if (fwrite($file, ', "info": ') === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	$test = $test . ', "info": ';

	$data = $app['dao.packet']->getInfo();
	$json = json_encode($data, JSON_NUMERIC_CHECK);
	if (fwrite($file, $json) === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	$test = $test . $json;
	if (fwrite($file, '}') === false) { 
		echo "Cannot write to text file. <br />"; 
	}
	$test = $test . '}';

	return $test;
})->bind('data');