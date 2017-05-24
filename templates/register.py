{% extends "reindexbase.html" %}
{% load staticfiles %}
           <div class="container">
           <form class="form-signin span4" id="login_form" method="post" action="/maiagogo/user_login/">
         
           


{% block body_block %} 
  <h2>Please sign in</h2>
   {% csrf_token %}
           {% if bad_details %}
           <p><strong>Your username and/or password were incorrect!</strong></p>
           {% elif disabled_account %}
           <p><strong>Your Rango account is currently disabled; we can't log you in!</strong></p>
           {% endif %}
           <div class="row control-group">
           <div class="form-group col-xs-12 floating-label-form-group controls">

           Username: <input type="text" class="form-control" placeholder="Username" name="username"/> <br />
           Password: <input type="password" class="form-control" placeholder="Password" name="password" />
            <p class="help-block text-danger"></p>
           <br />
           <button type="submit" class="btn btn-default">REGISTER</button>
           </div>
           </div>
           </form>

{% endblock %}
