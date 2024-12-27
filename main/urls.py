from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('poems/', views.poems_page, name='poems_page'),
]