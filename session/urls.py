from django.urls import path, include
from .views import loginUser,logoutuser,changePassword,userRegis,userProfileView,showUserProfileView
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('login/',loginUser,name="login"),
    path('logout/',logoutuser,name='logout'),
    path('change-pass/',changePassword,name='chanegpass'),
    path('signup/',userRegis,name='registration'),
    path('userprofile/',userProfileView,name='userprofile'),
    path('showprofile/',showUserProfileView,name='showprofile'),
    #path('firstproject/', include(('firstproject.urls', 'firstproject'), namespace='firstproject')),
]