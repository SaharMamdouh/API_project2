from django.urls import path
from .views import create_user , logout
from rest_framework.authtoken.views import obtain_auth_token

app_name='account'
urlpatterns = [
    path('login/',obtain_auth_token,name='authentication'),
    path('profile/', create_user , name='create-user'),
    path('logout/', logout , name='delete-token'),
]