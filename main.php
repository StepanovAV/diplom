<!DOCTYPE html>
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

<!-- Подключаю жс и пхп... -->
<?php include_once "php.php"?>

<div id="exx" style="display: none";>Вы успешно залогинились</div>
</body>
</html>
