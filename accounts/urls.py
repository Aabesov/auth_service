from django.urls import path
from . import views
from .views import UserLoginAPIView

urlpatterns = [
    path("register/", views.RegisterUserAPIView.as_view()),
    path("activate/<str:activation_code>/", views.ActivateAccountView.as_view(), name="activate_account"),
    # path("login/", UserLoginAPIView.as_view()),
    path("users/", views.AllUsersAPIView.as_view()),
    path("login/", views.UserTokenLoginAPIView.as_view()),
    path("logout/", views.UserTokenLogoutAPIView.as_view()),
]
