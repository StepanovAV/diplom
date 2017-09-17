<?php
	//Настройки соединения с базой
	$host = "localhost";
	$base = "diplom_db";
	$username = "root";
	$password = "";
	
	$mysqli = new mysqli($host, $username, $password, $base);
	
	if (!$mysqli) { 
		printf("Невозможно подключиться к базе данных. Код ошибки: %s\n", mysqli_connect_error()); 
		exit; 
	} 
	else printf("ok db");
	
	echo("<br><br>");
	
	if ($result = mysqli_query($mysqli, 'SELECT * FROM login')) { 

    /* Выборка результатов запроса */ 
    while( $row = mysqli_fetch_assoc($result) ){ 
        printf("%s (%s)\n", $row['login'], $row['password'], $row['email']); 
    } 

    /* Освобождаем используемую память */ 
    mysqli_free_result($result); 
} 
	
	$mysqli->close();


?>
	<script>
	alert("ЗАЛУПА!!");
	</script>