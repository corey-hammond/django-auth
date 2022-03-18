from ast import For
from django.urls import path, include
from .views import GoogleAuthAPIView, LogoutAPIView, RefreshAPIView, RegisterAPIView, LoginAPIView, ResetAPIView, TwoFactorAPIView, UserAPIView, ForgotPasswordAPIView

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('two-factor', TwoFactorAPIView.as_view()),
    path('google-auth', GoogleAuthAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('forgot-password', ForgotPasswordAPIView.as_view()),
    path('reset-password', ResetAPIView.as_view()),
]
