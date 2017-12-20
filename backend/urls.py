from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='mainCollector'),
    url(r'^login/', views.loginUser, name='loginCollector'),
    url(r'^reg/', views.regUser, name='regCollector'),
    url(r'^checkUsername/', views.checkUsername, name='checkUsername'),
    url(r'^firstTimeLogin/', views.firstTimeLogin, name='firstTimeLogin'),
    url(r'^nickNameCheck/', views.nickNameCheck, name='nickNameCheck'),
]

