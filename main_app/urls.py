from django.urls import path
from .views import Signup, Home, Profile, Shout

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('accounts/shout/', Shout.as_view(), name="shout"),
    path('accounts/profile/', Profile.as_view(), name="profile"),
    path('accounts/signup/', Signup.as_view(), name="signup")
]