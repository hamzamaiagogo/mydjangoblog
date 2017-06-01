{% extends "Aboutbase.html" %}
{% load staticfiles %}

{% block body_block %} 
   {% if registered %}
   <p>Thank you for registering.</p>
   <p><a href="/maiagogo/user_login/">Login</a> when you are read!.</p>
   {% else %}
   <form  method="post" id="user_form" action="/maiagogo/register/"
   enctype="multipart/form-data">
   {% csrf_token %}
   <h2>Sign up Here</h2>
   <!-- Display each form here -->
{% for field in user_form.visible_fields %} 
     {{field.errors }} 
     {{field.help_text}}</br> 
     {{field }}</br>
  {% endfor %} 
  {% for field in profile_form.visible_fields %} 
     {{field.errors }} 
     {{field.help_text}}</br> 
     {{field }} 
  {% endfor %} 
<br />
<!-- Provide a button to click to submit the form. -->
<button type="submit" class="btn btn-default">REGISTER</button>
</form>
{% endif %}




<p>Want
 to get in touch with me? Fill out the form below to send me a message 
and I will try to get back to you within 24 hours!</p>
<div class="row control-group">
   <div class="form-group col-xs-12 floating-label-form-group controls">
 <form  method="POST"  > 
<input type="text" class="form-control" placeholder="Type anything here to see form" id="Type anything here to see form" required data-validation-required-message="Please enter your title.">
            <p class="help-block text-danger"></p>
  {% csrf_token %} 
  {{ form.as_p }}
</div>
</div>
<br>
<div id="success"></div>
<div class="row">
<div class="form-group col-xs-12">
    <button type="submit" class="btn btn-default">Save</button>
</div>
</div>
</form>
{% endblock %}
