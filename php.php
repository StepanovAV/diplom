<?php
	//Настройки соединения с базой
	$host = "localhost";
	$base = "diplom_db";
	$username = "root";
	$password = "";
	
	$mysqli = new mysqli($host, $username, $password, $base);

	/* проверяем соединение */
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}

	/* возвращаем имя текущей базы данных */
	if ($result = $mysqli->query("SELECT DATABASE()")) {
		$row = $result->fetch_row();
		printf("Default database is %s.\n", $row[0]);
		$result->close();
	}
	
	$mysqli->close();

?>