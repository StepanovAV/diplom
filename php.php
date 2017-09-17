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
	else echo '<script>var buf ="'.$base.'"; console.log("Успешно подключились к " + buf);</script>';
	
	echo("<br>");
	
	if ($result = mysqli_query($mysqli, 'SELECT login, password FROM login')) { 

	/* Передаем логин и пароль с пхп в джаваскрипт переменные*/ 
		while( $row = mysqli_fetch_assoc($result) ){ 
			echo '<script>var a = "'.$row['login'].'";</script>';
			echo '<script>var b = "'.$row['password'].'";</script>';

		} 

	} 
	
	if ($result = mysqli_query($mysqli, 'SELECT name, surname FROM users')) { 

	/* Передаем имя, фамилию с пхп в джаваскрипт переменные*/ 
		while( $row = mysqli_fetch_assoc($result) ){ 
			echo '<script>var name = "'.$row['name'].'";</script>';
			echo '<script>var surname = "'.$row['surname'].'";</script>';
		} 

	} 
	
	/* Освобождаем используемую память */ 
	mysqli_free_result($result); 
	
	$mysqli->close();

?>
<script>
	var log = document.getElementById("login");
	var pass = document.getElementById("password");
	var submit = document.getElementById("submit");
	//alert(a + "  " + b);
	submit.onclick = function () {
			if (log.value == a && pass.value == b) {
				alert(name + " Вы успешно войшли");
					var exx = document.getElementById("exx");
					exx.style.display = "";
					exx.style.color = "green";
					exx.innerHTML = "Это ваш аккаунт, " + name +" "+ surname;
					document.getElementById('loginform').style.display = 'none';

				}
				else alert ("Я вас не знаю!");
	}
</script>