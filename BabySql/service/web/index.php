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
        $conn = new mysqli($servername, $username, $password, $dbschema);
       
        $result = $conn->query($query);

        if ($result->num_rows > 0) {
           return $result->fetch_assoc();
          }
        else{
            return false;
        }
    }
    function check_security($string){
        # characters allowlist. We allow these characters because they can be used in passwords
        $allowlist = "/[^A-z0-9,.\ =+\-?!\\\\]/";
        
        if(preg_match($allowlist, $string) || is_array($string)){

           return false;
        };
        
        $words = explode(' ', $string);
        
        # It's better remove these dangerous words, we don't want another little bobby tables
        $words_blocklist = [
            "SELECT", "DROP", "FLAG", "OR", "AND", "UNION", "INSERT", "INFORMATION_SCHEMA", "--" 
        ];

        for($i=0; $i < count($words); $i++){
            $w = strtoupper($words[$i]);
            
            if(in_array($w, $words_blocklist)){
                unset($words[$i]);
            }
        }
        
        return implode(' ', $words);
    }
    

    $name = False;
    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = check_security($_POST['username']);
        $password = check_security($_POST['password']);

        if($username === false || $password == false){
            die('You are not allowed to use those characters');
        }
        
        $query = "SELECT username FROM users WHERE username='$username' AND password='/*$password*/' /*'$username' logged in*/"; 
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
            <input class="form-control" name='username' class='form-control' type='text' value='' placeholder='Username'>
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


