<!DOCTYPE html>
<html lang="en">
<?php 
$database = include('../config.php');
//test
//echo $database['host'];
?>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/css?family=Roboto+Condensed" rel="stylesheet"> 
    <link href="main.css" rel="stylesheet">
    <title>Git Gud or Git Flashd</title>
</head>

<!-- Using include header for all other pages bar the index -->
<?php
include('PHP/header.php');
?>

<!-- Nav bar located in PHP folder -->
<?php
include('PHP/nav.php');
?>

<body>
<!-- Using include to improve readability -->
<?php
include('PHP/getstats.php');
?>
</body>

<!-- Footer bar located in PHP folder -->
<?php
include('PHP/footer.php');
?>

</html>