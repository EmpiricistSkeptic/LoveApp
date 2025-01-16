from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('poems/', views.poems_page, name='poems_page'),
    path('letters/', views.letters_page, name='letters_page'),
    path('map/', views.map_page, name='map_page'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]