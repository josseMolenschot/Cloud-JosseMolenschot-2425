<?php
    echo "<h1>Welcome to My Web Page</h1>";
    echo "<p>Current Date and Time: " . date("Y-m-d H:i:s") . "</p>";
    echo "<p>Server IP Address: " . $_SERVER['SERVER_ADDR'] . "</p>";
    echo "<p><a href='map.php'>Click here to view the map</a></p>"; // Link to the map page
?>
