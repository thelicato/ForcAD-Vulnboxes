<?php

# You should not tamper with this script!

function check_authorization_header()
{
  $flag_manager_secret = getenv('FLAG_MANAGER_SECRET');
  $headers = getallheaders();

  $expectedValue = "Bearer $flag_manager_secret";

  if (!isset($headers['Authorization']) || $headers['Authorization'] !== $expectedValue) {
    return false;
  }

  return true;
}
function put_flag()
{
  $isAllowed = check_authorization_header();
  if (!$isAllowed) {
    header('HTTP/1.1 401 Unauthorized');
    header('Content-Type: application/json');
    echo json_encode(array('message' => 'Unauthorized'));
    exit;
  }

  $servername = getenv('DBHOST');
  $username = getenv('DBUSER');
  $password = getenv('DBPASS');
  $dbschema = getenv('DBSCHEMA');

  $conn = new mysqli($servername, $username, $password, $dbschema, 3306);

  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
  }

  $flag_id = $_POST["id"];
  $flag_vuln = $_POST["vuln"];
  $flag_value = $_POST["flag"];

  # Insert query in flags table
  $insertQuery = "INSERT INTO flags VALUES ('$flag_id', '$flag_vuln', '$flag_value')";
  $conn->query($insertQuery)->fetch_assoc();

  # Add new flag
  $updateTable = "UPDATE users SET pwd=('$flag_value') WHERE username=('admin')";
  $conn->query($updateTable)->fetch_assoc();

  header('Content-Type: application/json; charset=utf-8');
  $data = ['message' => 'Flag correctly set'];
  echo json_encode($data);
}

function get_flag()
{
  $isAllowed = check_authorization_header();
  if (!$isAllowed) {
    header('HTTP/1.1 401 Unauthorized');
    header('Content-Type: application/json');
    echo json_encode(array('message' => 'Unauthorized'));
    exit;
  }

  $servername = getenv('DBHOST');
  $username = getenv('DBUSER');
  $password = getenv('DBPASS');
  $dbschema = getenv('DBSCHEMA');

  $conn = new mysqli($servername, $username, $password, $dbschema, 3306);

  $flag_id = $_GET["id"];
  $flag_vuln = $_GET["vuln"];

  # Insert query in flags table
  $query = "SELECT * FROM flags WHERE id=('$flag_id') AND vuln=('$flag_vuln')";
  $result = $conn->query($query)->fetch_assoc();

  $data = ['flag' => $result['flag']];
  header('Content-Type: application/json; charset=utf-8');
  echo json_encode($data);
}

switch ($_SERVER['REQUEST_METHOD']) {
  case 'GET':
    get_flag();
    break;
  case 'POST':
    put_flag();
    break;
  default:
    break;
}
?>