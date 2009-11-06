<?php

/**
  _________      .__       .____   _______
 /   _____/ ____ |__|_____ |    |  \   _  \    ____
 \_____  \ /    \|  \____ \|    |  /  /_\  \  / ___\
 /        \   |  \  |  |_> >    |__\  \_/   \/ /_/  >
/_______  /___|  /__|   __/|_______ \_____  /\___  /
        \/     \/   |__|           \/     \//_____/
http://snippet.c0de.me
slac3dork@gmail.com
*/

/**
* PHP Server and Execution Environment Information
* Coded By slac3dork
* Special Thanks to Myrddin and Jeffwk who are giving me inspiration.
*/
echo '<h2><p align="center">Server And Execution Environment Information</p></h2>';
echo '<table border="3" align="center">';
foreach ($_SERVER as $key => $value) {
	if (!$value) {
		$value = '-';
	}
	echo '<tr>';
	echo '<td>'.$key.'</td>'.'<td>'.$value.'</td>';
	echo '</tr>';
}
echo '</table>';
?>

