"""
URL configuration for firstproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

#here the from the views to call the function we need to import first
#then call the function
#to create a url use path() the path takes the url then the views functions name
#then name='url name' this name is used to use this in future like laravel

#--------------part 15--------------
#image uploading
#to show the uploaded images add static

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path,include
from .views import home,homeView
from django.conf.urls.static import static
from django.conf import settings 
from django.views.generic import TemplateView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',homeView.as_view(),name='homepage'),
    path('home2/',TemplateView.as_view(template_name='home.html'),name='homepage3'),
    #path("home/",home,name="home"),
    path('tuition/',include('tuition.urls')),
    path('session/',include('session.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
