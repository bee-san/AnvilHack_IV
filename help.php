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
    <h2>Need help?</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse blandit, diam a imperdiet rhoncus, odio tortor accumsan sapien, id scelerisque tortor nibh at est. Morbi placerat, metus vel feugiat lobortis, tortor justo ornare sem, id auctor tellus lacus pharetra orci. Vestibulum sed diam urna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam nibh neque, pharetra vitae mattis id, porttitor eget neque. Duis egestas odio ut mollis maximus. Ut augue ligula, rhoncus vel consectetur sit amet, gravida eu libero. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam id erat bibendum, viverra nunc ac, rhoncus felis. Quisque ac leo porta, hendrerit augue vitae, ultricies ligula. Praesent feugiat rutrum nibh, in fermentum nibh tincidunt at. Suspendisse quis pharetra felis, vitae congue turpis. Donec in placerat dui. Interdum et malesuada fames ac ante ipsum primis in faucibus. </p>
</body>

<!-- Footer bar located in PHP folder -->
<?php
include('PHP/footer.php');
?>

</html>
