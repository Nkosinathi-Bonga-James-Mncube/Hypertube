"""Hypertube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pages.views import home_view,login_view,library_view,video_view,update_view
from input_data.views import regist_view
from email_send.views import email_view 
urlpatterns = [
    path('', login_view, name='home'),
    path('home/',home_view),
    path('library/',library_view),
    path('video/',video_view),
    path('update/',update_view),
    path('email/',email_view),
    path('register/',regist_view),
    path('admin/', admin.site.urls),
]
