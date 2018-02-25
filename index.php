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

<!-- Don't use PHP header as this is a one time thing -->
<header>
<h1 id = "center">Flashcard Revision Game</h1>
</header>

<!-- Nav bar located in PHP folder -->
<?php
include('PHP/nav.php');
?>

<body>
    <h2>Welcome!</h2>
    <p>Please text this number to get started!</p>
    <p>441618502075</p>
</body>

<!-- Footer bar located in PHP folder -->
<?php
include('PHP/footer.php');
?>

</html>
