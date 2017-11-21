from django.conf.urls import url
from . import views

app_name = 'userModule'

urlpatterns = [
    url(r'^$', views.loginPage, name='loginPage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^provideDetailsUser/$', views.provideDetailsUser, name='provideDetailsUser'),
    url(r'^provideDetailsAdmin/$', views.provideDetailsAdmin, name='provideDetailsAdmin'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^getDetails/$', views.getDetails, name='getDetails'),
    url(r'^addAdminDetails/$',views.addAdminDetails,name='addAdminDetails'),
    url(r'^addUserDetails/$', views.addUserDetails, name='addUserDetails'),
]
