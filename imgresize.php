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
* PHP Image Resize (PNG, JPG, GIF, WBMP)
* Coded By slac3dork
*/

$newwidth = 0;
$newheight = 0;
$ratio = 0;

// File and new size
$filename = 'example.jpg';

// Get new sizes
list($width, $height) = getimagesize($dest_file);

// Resize condition
if ($width > 600 || $height > 600) {
	$ratio = $width/$height;
	$newwidth = 550;
	$newheight = $newwidth/$ratio;
} else {
	$newwidth = $width;
	$newheight = $height;
}

// Load
$thumb = imagecreatetruecolor($newwidth, $newheight);

// get extension file
$file_ext_array = explode('.', $filename);
$file_ext = strtolower($file_ext_array[1]);

if (($file_ext = 'jpg') || ($file_ext = 'jpeg')) {
	$source = imagecreatefromjpeg($filename);
} elseif ($file_ext = 'gif') {
	$source = imagecreatefromgif($filename);
} elseif ($file_ext = 'png') {
	$source = imagecreatefrompng($filename);
} elseif ($file_ext = 'wbmp') {
	$source = imagecreatefromwbmp($filename);
} else {
	exit(1);
}

// Resize
imagecopyresized($thumb, $source, 0, 0, 0, 0, $newwidth, $newheight, $width, $height);

// Output
if (($file_ext = 'jpg') || ($file_ext = 'jpeg')) {
	imagejpeg($thumb, $filename.'_new.jpg');
} elseif ($file_ext = 'gif') {
	imagegif($thumb, $filename.'_new.gif');
} elseif ($file_ext = 'png') {
	imagepng($thumb, $filename.'_new.png');
} elseif ($file_ext = 'wbmp') {
	imagewbmp($thumb, $filename.'_new.wbmp');
} else {
	exit(1);
}

// delete old file
unlink ($filename);

?>

