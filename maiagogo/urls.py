from django.conf.urls import patterns, include, url
from maiagogo import views

urlpatterns = patterns('',
   
    #url(r'^$', 'maiagogo.views.about', name='about'),
    url(r'^$', 'maiagogo.views.About', name='About'),
    url(r'^post/(?P<pk>\d+)/$', 'maiagogo.views.post_detail', name='post_detail'),
    url(r'^post/new/$', 'maiagogo.views.post_new', name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', 'maiagogo.views.post_edit', name='post_edit'),
    url(r'^contact/$', 'maiagogo.views.contact', name='contact'),
    url(r'^register/$', 'maiagogo.views.register', name='register'),
    url(r'^user_login/$', 'maiagogo.views.user_login', name='user_login'),
    url(r'^user_logout/', 'maiagogo.views.user_logout', name='user_logout'),
    url(r'^aboutMe/$', 'maiagogo.views.aboutMe', name='aboutMe'),
    url(r'^sample/$', 'maiagogo.views.sample', name='sample'),
    url(r'^ramadan/$', 'maiagogo.views.ramadan', name='ramadan'),
    url(r'^islam/$', 'maiagogo.views.islam', name='islam'),
)
