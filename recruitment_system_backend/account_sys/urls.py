from django.urls import path

from account_sys.views import *

urlpatterns = [
    path("register", register),
    path("login", login),
    path("logout", logout),
    path("current", get_current_user)
]