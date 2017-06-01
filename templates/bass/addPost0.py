{% extends "indexbase.html" %}
{% load staticfiles %}

{% block body_block %}      
<div class="row control-group">
   <div class="form-group col-xs-12 floating-label-form-group controls">
<h1>New Post</h1>
    <br/>
 <form  method="POST"  > 
<input type="text" class="form-control" placeholder="Type anything here, and then complete the form" id="Type anything here, and then complete the forms" >
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
