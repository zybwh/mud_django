from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='mainCollector'),
    url(r'^login/', views.loginUser, name='loginCollector'),
]

