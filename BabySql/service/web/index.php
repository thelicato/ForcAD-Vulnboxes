<?php
    error_reporting(0);
    if(isset($_GET['source'])){
        highlight_file(__FILE__); 
        die();
    }
    function do_query($query){

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
          }
        else{
            return false;
        }
    }

    if(isset($_POST['password'])){
        #$password = addslashes($_POST['password']);
        $password = $_POST['password'];

        $query = "SELECT * FROM users WHERE pwd=('$password') AND username=('admin')";

        if (preg_match('/INSERT|UPDATE|DELETE|CREATE|ALTER|DROP/i', $query)) {
            die("Sorry! You cannot do that.");
        }

        $res = do_query($query);
       
        if(isset($res['username'])){
            $name = $res['username'];
        }
        
    }
    
?>

<html>

<head>

<title></title>

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">

<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">

<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
</head>

<body>
<div class="main">
    <div class="container">
    <div class="row">
    <h1>BabySql</h1>
    </div>
    <div class="row">
    <p class="lead">
    Welcome to BabySql! If you want you can view the source code <a href="?source">here</a>. Happy Injection:)
    </p>
    </div>
    </div>
    <div class="container">
        <div class="row">
        <form class="form form-inline" method='POST'>                       
            <input class="form-control" name='password' class='form-control' type='password' value='' placeholder='Password'>
            <input class="form-control btn btn-default" name="submit" value='Go' type='submit'>
        </form>
        </div>
        <div class="row">
        <p class="lead"> 
        <?php
            if($name){?>
            Logged as <?= htmlspecialchars($name) ?>
        <?php }; ?>
        </p>
        </div>
            
    </div>
</div> 

</body>

</html>


