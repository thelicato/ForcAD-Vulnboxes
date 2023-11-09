<html>

<head>

  <title>CodeMaze</title>

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
  Welcome to CodeMaze! There is nothing here.
  <?php
  if (isset($_GET['submit'])) {
    $name = $_GET['name'];
    // include and register Twig auto-loader
    include '../vendor/twig/twig/lib/Twig/Autoloader.php';
    Twig_Autoloader::register();
    try {
      // specify where to look for templates
      $loader = new Twig_Loader_String();

      // initialize Twig environment
      $twig = new Twig_Environment($loader);
      // set template variables
      // render template
      $result = $twig->render($name);
      echo "Hello $result";

    } catch (Exception $e) {
      die('ERROR: ' . $e->getMessage());
    }
  }

  ?>
</body>

</html>