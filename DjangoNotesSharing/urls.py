"""DjangoNotesSharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from notes.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('about',about,name="about"),
    path('contact',contact,name="contact"),
    path('user_login',user_login,name="user_login"),
    path('admin_login',admin_login,name="admin_login"),
    path('user_signup',user_signup,name="user_signup"),
    path('admin_home',admin_home,name="admin_home"),
    path('persons_logout',persons_logout,name="persons_logout"),
    path('user_profile',user_profile,name="user_profile"),
    path('user_changepassword',user_changepassword,name="user_changepassword"),
    path('user_editprofile',user_editprofile,name="user_editprofile"),
    path('upload_notes',upload_notes,name="upload_notes"),
    path('user_viewnotes',user_viewnotes,name="user_viewnotes"),
    path('delete_notes/<int:id>',delete_notes,name="delete_notes"),
    path('view_allusers',view_allusers,name="view_allusers"),
    path('delete_users/<int:id>',delete_users,name="delete_users"),
    path('pending_notes',pending_notes,name="pending_notes"),
    path('change_notesstatus/<int:id>',change_notesstatus,name="change_notesstatus"),
    path('accepted_notes',accepted_notes,name="accepted_notes"),
    path('rejected_notes',rejected_notes,name="rejected_notes"),
    path('all_notes',all_notes,name="all_notes"),
    path('delete_notesbyadmin/<int:id>',delete_notesbyadmin,name="delete_notesbyadmin"),
    path('user_viewallnotes',user_viewallnotes,name="user_viewallnotes")
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
