<!DOCTYPE html>
<html> 
<head>
</head> 
<body> 
<?php
// Affiche le nom d'utilisateur qui fait tourner le processus php/http
// (sur un système ayant "whoami" dans le chemin d'exécutables)
echo exec('python PysharkCapturer.py');
?> 
</body> 

</html> 
