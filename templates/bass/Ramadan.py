{% extends "Postbase.html" %}
{% load staticfiles %}

{% block body_block %} 
<h2 class="section-heading">Reaching for the Stars</h2>
<p>The 
Sultan of Sokoto, Alhaji Sa’ad Abubakar III, has declared Saturday, May 27, as 1st Ramadan, 1438 AH.
</p>
<a href="#">
<img class="img-responsive" src= "{% static 'style/img/post-sample-image.jpg' %}"  width="100%" height="200" alt="">
</a>
<span class="caption text-muted">This signifies the start of the annual long-month fast by Muslims.</span>

<blockquote>The
dreams of yesterday are the hopes of today and the reality of tomorrow.
Science has not yet mastered prophecy. We predict too much for the next
year and yet far too little for the next ten.</blockquote>

{% endblock %}
