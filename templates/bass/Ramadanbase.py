{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>Maiagogo-Ramadan</title>

    <!-- Bootstrap Core CSS -->
    <link href="{% static 'style/vendor/bootstrap/css/bootstrap.min.css' %}" rel="stylesheet" media="screen">

    <!-- Theme CSS -->
    <link href="{% static 'style/css/clean-blog.min.css' %}" rel="stylesheet" media="screen">
    

    <!-- Custom Fonts -->
    <link href="vendor/font-awesome/css/font-awesome.min.css" rel="stylesheet" type="text/css">
    <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <!-- Navigation -->
    <nav class="navbar navbar-default navbar-custom navbar-fixed-top">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header page-scroll">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span>
                    Menu <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="index.html">maiagogo</a>
                <a class="navbar-brand" href="/maiagogo/post/new/"><span class="glyphicon glyphicon-plus"></span></a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav navbar-right">
                   <li>
                        <a href="/maiagogo/">Home</a>
                    </li>
			<li>
                        <a href="/maiagogo/islam/">Islamic</a>
                    </li>
                    <li>
                        <a href="/maiagogo/ramadan/">Ramadan</a>
                    </li>
                    <li>
                        <a href="/maiagogo/aboutMe/">About</a>
                    </li>
                    <li>
                        <a href="/maiagogo/sample/">Sample Post</a>
                    </li>
                    <li>
                        <a href="/maiagogo/contact/">Contact</a>
                    </li>
		{% if user.is_authenticated %} 
                     <li ><a href="#">Welcome, {{ user.username }}!</a></li> 
                     <li ><a href="/maiagogo/user_logout/">Logout</a></li> 
                     {% else %} 
                     <li><a href="/maiagogo/register/">Register</a></li> 
                     <li><a href="/maiagogo/user_login/">Login</a></li>
                     {% endif %} 
                </ul>
            </div>
            <!-- /.navbar-collapse -->
        </div>
        <!-- /.container -->
    </nav>

    <!-- Page Header -->
    <!-- Set your background image for this header on the line below. -->
<header class="intro-header" style="background-image: url({% static 'style/img/Ra2.jpeg' %})">
<div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
 <div class="page-heading">
                        <h1>Ramadan 2017</h1>
                        <hr class="small">
                        <span class="subheading">Ramadan Wishes, Messages and Ramadan Greetings</span>
</div>

                </div>
            </div>
        </div>
</header>

    <!-- Post Content -->
    <article>
    <div class="container">
        <div class="row">
            <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">

                {% block body_block %}
        
               {% endblock %}
               
            </div>
        </div>
    </div>
</article>
<hr>
    <!-- Footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col-lg-8 col-lg-offset-2 col-md-10 col-md-offset-1">
                    <ul class="list-inline text-center">
                        <li>
                            <a href="#">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-circle fa-stack-2x"></i>
                                    <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
                                </span>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-circle fa-stack-2x"></i>
                                    <i class="fa fa-facebook fa-stack-1x fa-inverse"></i>
                                </span>
                            </a>
                        </li>
                        <li>
                            <a href="#">
                                <span class="fa-stack fa-lg">
                                    <i class="fa fa-circle fa-stack-2x"></i>
                                    <i class="fa fa-github fa-stack-1x fa-inverse"></i>
                                </span>
                            </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted">Copyright &copy; My Website 2017</p>
                </div>
            </div>
        </div>
    </footer>

    <!-- jQuery -->
    <script src="{% static 'style/vendor/jquery/jquery.min.js' %}"></script>
    

    <!-- Bootstrap Core JavaScript -->
    <script src="{% static 'style/vendor/bootstrap/js/bootstrap.min.js' %}"></script>


    <!-- Contact Form JavaScript -->
    <script src="{% static 'style/js/jqBootstrapValidation.js' %}"></script>
   <script src="{% static 'style/js/contact_me.js' %}"></script>
   

    <!-- Theme JavaScript -->
      <script src="{% static 'style/js/clean-blog.min.js' %}"></script>
    

</body>

</html>
