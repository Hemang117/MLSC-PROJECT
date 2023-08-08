"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('home/login.html',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logoout/',views.LogoutPage,name='logout'),
    path('home/e.html',views.EventsPage,name='events'),
    path('home/f.html',views.FeesPage,name='Fees'),
    path('home/hc.html',views.HcPage,name='HostelContacts'),
    path('home/index.html',views.indexPage,name='index'),
    path('home/la.html',views.LaPage,name='Leave Application'),
    path('home/lf.html',views.lfpage,name='Lost and found'),
    path('home/n.html',views.Noticepage,name='Notice'),
    path('home/p.html',views.profilepage,name='Profile'),
    path('home/q.html',views.Querypage,name='Queries'),
    path('home/tm.html',views.TMpage,name='Todays Menu'),


]
