from django.conf.urls import patterns, include, url
from feedb import views
from django.contrib import admin
##from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', views.main_page, name='main_page'),
                       
    
    url(r'^feedback_page/(?P<cid>\d+)/$', views.feedback_page, name='feedback_page'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
                       
####                       staff urls
   
    url(r'^user/staff/(\w+)/$', views.staff_page, name='staff_page'),  

####                       logout url
    url(r'^logout/$', views.logout_page, name='logout'),
                       
####                       redirect_url
    url(r'^staff/redir/$', views.staff_redir, name='staff_redir'),


    

)




