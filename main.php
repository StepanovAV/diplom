﻿<!DOCTYPE html>
<html>
<head>
<title>Антиплагіат</title>
  <meta charset="utf-8">
  <!--<link rel="stylesheet" href="Style.css"/> -->
</head>
<body>

<!-- форма для отправки сообщений -->
<div id="loginform">
  <div>SIGN UP</div>
  <input type="text" id="login" name="login" placeholder="username">
  <input type="password" id="password" name="password" placeholder="password">
  <input type="submit" id="submit" value="LOGIN"/>
</div>

<!-- здесь будут что-то... -->
<?php include_once "php.php"?>
<script>
	var log = document.getElementById("login");
	var pass = document.getElementById("password");
	var submit = document.getElementById("submit");
	var a = "admin";
	var b = "1111";
	console.log(log.value);
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


<div id="exx" style="display: none";>Вы успешно залогинились</div>
</body>
</html>