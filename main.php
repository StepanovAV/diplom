<!DOCTYPE html>
<html>
<head>
<title>Антиплагиат</title>
  <meta charset="utf-8">
  <!--<link rel="stylesheet" href="Style.css"/> -->
</head>
<body>

<!-- форма для входа -->
<div id="loginform">
  <div>SIGN UP</div>
  <input type="text" id="login" name="login" placeholder="username" value="admin">
  <input type="password" id="password" name="password" placeholder="password">
  <input type="submit" id="submit" value="LOGIN"/>
</div>

<!-- Подключаю js и php... -->
<?php include_once "php.php"?>

<div id="exx" style="display: none";>Здесь будет имя пользователя после успешного входа</div>

<img src="" id="icon" style="display: none; width: 200px; border-radius: 10px"/>
</body>
</html>
