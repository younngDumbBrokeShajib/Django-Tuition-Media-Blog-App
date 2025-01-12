from django.urls import path, include
from .views import loginUser,logoutuser
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('login/',loginUser,name="login"),
    path('logout/',logoutuser,name='logout'),
    #path('firstproject/', include(('firstproject.urls', 'firstproject'), namespace='firstproject')),
]