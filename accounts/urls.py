from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_Shponr/', views.registerS, name='registerS'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),

    
    
    
    
    
    
    ]