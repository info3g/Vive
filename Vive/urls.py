"""Vive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from live import views 

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/',views.signup_page, name='signup'),
    url(r'^signin/',views.login_user, name='signin'),
    url(r'^logout/',views.user_logout, name='user_logout'),
    url(r'^home/', views.home, name="home"),
    url(r'^schedule/', views.schedule, name="schedule"),
    url(r'^$', views.index, name="index"),
    url(r'^multiSchedule/', views.multiSchedule, name="multiSchedule"),
    url(r'^download/',views.download, name='download'),
]
  
 