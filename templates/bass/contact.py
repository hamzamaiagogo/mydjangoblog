{% extends "Contactbase.html" %}
{% load staticfiles %}

{% block body_block %} 
<p>Want
 to get in touch with me? Fill out the form below to send me a message 
and I will try to get back to you within 24 hours!</p>
<div class="row control-group">
   <div class="form-group col-xs-12 floating-label-form-group controls">
 <form  method="POST"  > 
<input type="text" class="form-control" placeholder="Type anything here, and then proceed" id="Type anything here, and then proceed" >
            <p class="help-block text-danger"></p>
  {% csrf_token %} 
  {{ form.as_p }}
</div>
</div>
<br>
<div id="success"></div>
<div class="row">
<div class="form-group col-xs-12">
    <button type="submit" class="btn btn-default">Send</button>
</div>
</div>
</form>
{% endblock %}
