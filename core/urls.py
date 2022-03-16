from django.urls import path, include
from .views import LogoutAPIView, RefreshAPIView, RegisterAPIView, LoginAPIView, UserAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
]
