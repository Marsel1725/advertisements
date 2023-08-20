from django.urls import path
from .views import my_login


urlpatterns = [
    path("myauth/", my_login, name="login"),
]