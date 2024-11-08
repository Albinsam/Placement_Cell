from django.urls import path
from . import views
from .views import logout

urlpatterns = [
    path('index/', views.index, name='index'),
    path('jobs/', views.jobs, name='jobs'),
    path('application/', views.app, name='app'),
    path('logout/', logout, name='logout'),
    path('search/', views.search_view, name='search_view'),

]