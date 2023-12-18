from django.urls import path

from login_register.views import login, register

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register')
]