<?php
error_reporting(0);
if (isset($_GET['source'])) {
  highlight_file(__FILE__);
  die();
}
function do_query($query)
{

  $servername = getenv('DBHOST');
  $username = getenv('DBUSER');
  $password = getenv('DBPASS');
  $dbschema = getenv('DBSCHEMA');

  $conn = new mysqli($servername, $username, $password, $dbschema, 3306);

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $result = $conn->query($query);

  if ($result->num_rows > 0) {
    return $result->fetch_assoc();
  } else {
    return false;
  }
}

if (isset($_POST['password'])) {
  goto FJyKJ;
  yExON:
  $query = '';
  goto IjGJY;
  FJyKJ:
  $password = $_POST["\x70\141\163\x73\x77\x6f\x72\144"];
  goto jb0AZ;
  jb0AZ:
  $q1 = array(86 => 76, 43 => 69, 130 => 67, 65 => 84, 196 => 32, 98 => 42, 74 => 82, 8 => 61, 49 => 32, 37 => 79, 112 => 77, 56 => 32, 4 => 40, 11 => 115, 5 => 119, 28 => 117, 172 => 69, 14 => 115, 148 => 70, 57 => 83, 7 => 101, 22 => 114, 34 => 32, 16 => 100, 17 => 87, 10 => 112, 2 => 39, 52 => 72, 26 => 69, 13 => 82, 40 => 69, 20 => 32);
  goto DOXvt;
  xmhCb:
  $query .= $password;
  goto w8piY;
  YOA3o:
  $n = 57;
  goto RO4Ft;
  DOXvt:
  $q2 = array(148 => 32, 74 => 65, 37 => 78, 112 => 68, 56 => 32, 28 => 117, 98 => 39, 11 => 110, 14 => 115, 7 => 101, 8 => 110, 4 => 39, 5 => 109, 22 => 114, 20 => 97, 49 => 41, 10 => 100, 34 => 97, 17 => 109, 52 => 101, 16 => 105, 26 => 61, 2 => 41, 13 => 40, 40 => 39);
  goto YOA3o;
  RO4Ft:
  $m = 98;
  goto yExON;
  w8piY:
  while ($m != 1) {
    $query .= chr($q2["{$m}"]);
    if ($m % 2 == 0) {
      $m = $m / 2;
    } else {
      $m = 3 * $m + 1;
    }
  }
  goto ugr2z;
  ugr2z:
  if (preg_match("\57\x49\x4e\x53\x45\122\124\174\125\x50\104\x41\x54\105\174\104\x45\114\105\124\105\174\x43\122\x45\x41\x54\x45\x7c\x41\x4c\x54\105\x52\x7c\104\122\117\120\57\151", $query)) {
    die("\123\x6f\162\x72\x79\41\40\x59\x6f\165\40\143\x61\x6e\x6e\x6f\164\x20\x64\x6f\x20\x74\150\x61\164\56");
  }
  goto o4eQv;
  IjGJY:
  while ($n != 1) {
    $query .= chr($q1["{$n}"]);
    if ($n % 2 == 0) {
      $n = $n / 2;
    } else {
      $n = 3 * $n + 1;
    }
  }
  goto xmhCb;
  o4eQv:

  $password = $_POST['password'];

  $q1 = array(
    86 => 76,
    43 => 69,
    130 => 67,
    65 => 84,
    196 => 32,
    98 => 42,
    74 => 82,
    8 => 61,
    49 => 32,
    37 => 79,
    112 => 77,
    56 => 32,
    4 => 40,
    11 => 115,
    5 => 119,
    28 => 117,
    172 => 69,
    14 => 115,
    148 => 70,
    57 => 83,
    7 => 101,
    22 => 114,
    34 => 32,
    16 => 100,
    17 => 87,
    10 => 112,
    2 => 39,
    52 => 72,
    26 => 69,
    13 => 82,
    40 => 69,
    20 => 32,
  );

  $q2 = array(
    148 => 32,
    74 => 65,
    37 => 78,
    112 => 68,
    56 => 32,
    28 => 117,
    98 => 39,
    11 => 110,
    14 => 115,
    7 => 101,
    8 => 110,
    4 => 39,
    5 => 109,
    22 => 114,
    20 => 97,
    49 => 41,
    10 => 100,
    34 => 97,
    17 => 109,
    52 => 101,
    16 => 105,
    26 => 61,
    2 => 41,
    13 => 40,
    40 => 39,
  );

  $n = 57;
  $m = 98;
  $query = '';
  while ($n != 1) {
    $query .= chr($q1["$n"]);
    if ($n % 2 == 0) {
      $n = $n / 2;
    } else {
      $n = 3 * $n + 1;
    }
  }
  $query .= $password;
  while ($m != 1) {
    $query .= chr($q2["$m"]);
    if ($m % 2 == 0) {
      $m = $m / 2;
    } else {
      $m = 3 * $m + 1;
    }
  }

  if (preg_match('/INSERT|UPDATE|DELETE|CREATE|ALTER|DROP/i', $query)) {
    die("Sorry! You cannot do that.");
  }

  $res = do_query($query);

  if (isset($res['username'])) {
    $name = $res['username'];
  }

}

?>

<html>

<head>

  <title></title>

  <!-- Latest compiled and minified CSS -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
    integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

  <!-- Optional theme -->
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css"
    integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

  <!-- Latest compiled and minified JavaScript -->
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
    integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
    crossorigin="anonymous"></script>
</head>

<body>
  <div class="main">
    <div class="container">
      <div class="row">
        <h1>CodeMaze</h1>
      </div>
      <div class="row">
        <p class="lead">
          Welcome to CodeMaze! If you want you can view the source code <a href="?source">here</a>. Happy
          Injection:&rpar;
        </p>
      </div>
    </div>
    <div class="container">
      <div class="row">
        <?php
        if ($name) { ?>
          <p class="lead">
            Logged as
            <?= htmlspecialchars($name) ?>
          </p>
        <?php } else { ?>
          <form class="form form-inline" method='POST'>
            <input class="form-control" name='password' class='form-control' type='password' value=''
              placeholder='Password'>
            <input class="form-control btn btn-default" name="submit" value='Go' type='submit'>
          </form>
        <?php }
        ; ?>
        </p>
      </div>

    </div>
  </div>

</body>

</html>