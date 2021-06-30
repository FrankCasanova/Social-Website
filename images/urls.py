from django.urls import path
from . import views

app_name = 'images'  # 5-9

urlpatterns = [
    path('create/', views.image_create, name='create'),
    path('detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),
    path('like/', views.image_like, name='like'),
    path('', views.image_list, name='list'),  # 182
    path('ranking/', views.image_ranking, name='ranking'),  # 222
]
