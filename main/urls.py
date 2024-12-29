from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('poems/', views.poems_page, name='poems_page'),
    path('letters/', views.letters_page, name='letters_page'),
    path('map/', views.map_page, name='map_page'),
]