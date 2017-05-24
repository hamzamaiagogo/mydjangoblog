{% extends "indexbase.html" %}
{% load staticfiles %}

{% block body_block %}      
<div class="post-preview">
{% if post.published_date %}
<p class="post-meta"> <span class="glyphicon glyphicon-time"> </span> Posted by <a href="#">{{ post.author }}</a> on {{ post.published_date }}</p>
{% endif %}
{% if user.is_authenticated %} 
<a href={% url 'post_edit' pk=post.pk %} class="post-meta"><span class="glyphicon glyphicon-pencil" > </span></a>
{% endif %}
<h2 class="post-title">{{ post.title }}</h2>
<p>
   {{ post.text|linebreaksbr }}
</p>

</div>
<hr>

{% endblock %}
