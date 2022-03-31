<?php

    $username = $_POST['username'];
    $password = $_POST['password'];

    $conn = new mysqli('localhost', 'root', '', 'sql_injection');

    if($conn->connect_error){
        die('connection Failed : ' .$conn->connect_error);
    }else{
        $stmt = $conn->prepare("insert into sql_injection(username, password)");

        $stmt->bind_param("ss",$username, $password);
        $stmt->execute();
        $stmt->close();
        $conn->close();
    }
?>