from django.urls import path
from .views import Signup, Home, Profile

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('accounts/profile/', Profile.as_view(), name="profile"),
    path('accounts/signup/', Signup.as_view(), name="signup")
]