from django.urls import path
from app.controllers.register import register_user
from app.controllers.home import index



urlpatterns = [
    path('', index, name='home'), 
    path('register/', register_user, name='register-user'),
]


