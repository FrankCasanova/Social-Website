from django.urls import path
from . import views

app_name = 'images'  # 5-9

urlpatterns = [
    path('create/', views.image_create, name='create')
]
