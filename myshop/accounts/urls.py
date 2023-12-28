from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('register', views.sign_up, name='register'),
    path('login', views.sign_in, name='login'),
]