from django.urls import path
from . import views

urlpatterns = [
    # post vies
    path('login/', views.user_login, name='login')
]
