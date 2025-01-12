from django.urls import path, include
from .views import loginUser,logoutuser,changePassword
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('login/',loginUser,name="login"),
    path('logout/',logoutuser,name='logout'),
    path('change-pass/',changePassword,name='chanegpass'),
    #path('firstproject/', include(('firstproject.urls', 'firstproject'), namespace='firstproject')),
]