<?php 
//takes the content from the .JSON file
//$filecontent = file_get_contents("");
//decodes the .JSON content stored in $filecontent
//$decodedcontent = json_decode($filecontent);
//$map = $decodedcontent -> 
?>
<div id="tableContainer-1">
<div id = "tableContainer-2">
<table id = "myTable">
    <thead>
        <tr>
            <td>User ID</td>
            <td>Answered Questions</td>
            <td>Opponents Score</td>
            <td>Score</td>
        </tr>
    </thead>
    <tbody>
        <?php
        for($i = 0; $i<5; $i++){
        ?>
            <tr>
                <td><?php echo $i?></td>
                <td><?php echo $randomnum = rand(1, 13); ?></td>
                <td><?php echo $randomnum = rand(1, 13); ?></td>
                <td><?php echo $randomnum = rand(1, 13); ?></td>
            </tr>
        <?php 
        }
        ?>
    </tbody>
</table>