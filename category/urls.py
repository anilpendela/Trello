from django.contrib import admin
from django.urls import path, include
from .views import *
from django.contrib.auth import views as auth_views

app_name = "category"

urlpatterns = [
	path('', HomePageView.as_view(), name="home"),
	path('signup/', Signup.as_view(), name='signup'),
]