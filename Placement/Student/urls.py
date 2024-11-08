from django.urls import path
from . import views
from .views import logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home,name='home'), 
    path('login/', views.signin,name='login'), 
    # path('register/', views.register,name='register'), 
    # path('reg/', views.reg,name='reg'), 
    path('register/', views.reg1,name='reg1'), 
    path('logout/', logout, name='logout'),

    
]