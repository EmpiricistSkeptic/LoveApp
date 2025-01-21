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
    path('questions/', views.questions_page, name='questions_page'),
    path('link-profile/', views.link_profile, name='link-profile'),
    path('profile/', views.profile_view, name='profile'),
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/', views.question_list, name='question_list'),
    path('questions/<int:questions_id>/', views.answer_question, name='answer_question'),
    
]