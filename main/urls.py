from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views



urlpatterns = [
    # Регистрируем страницы
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    
    # Основные страницы
    path('', views.main_page, name='main_page'),
    path('poems/', views.poems_page, name='poems_page'),
    path('letters/', views.letters_page, name='letters_page'),
    path('map/', views.map_page, name='map_page'),
    
]