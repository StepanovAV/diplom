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
	
	if ($result = mysqli_query($mysqli, 'SELECT login, password FROM login')) { 

    /* Выборка результатов запроса */ 
    while( $row = mysqli_fetch_assoc($result) ){ 
        printf("%s (%s)\n", $row['login'], $row['password']); 
		echo '<script language="javascript">var a = "'.$row['login'].'";</script>';
		echo '<script language="javascript">var b = "'.$row['password'].'";</script>';

    } 

    /* Освобождаем используемую память */ 
    mysqli_free_result($result); 
} 
	
	$mysqli->close();


?>
<script>
	var log = document.getElementById("login");
	var pass = document.getElementById("password");
	var submit = document.getElementById("submit");
	alert(a + "  " + b);
	submit.onclick = function () {
			if (log.value == a && pass.value == b) {
				alert("Вы молодец");
					var exx = document.getElementById("exx");
					exx.style.display = "";
					exx.style.color = "green";
					document.getElementById('loginform').style.display = 'none';

				}
				else alert ("Идите нахуй! Я вас не знаю!");
	}
</script>