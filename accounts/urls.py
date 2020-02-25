from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.indexView, name= "home"),
    url(r'^login/', views.loginView, name="login"),
    url(r'^dashboard/', views.dashboardView, name="dashboard"),
    url(r'^register/', views.registerView, name="register"),
    url(r'^logout/', views.logoutView, name= "logout"),
]