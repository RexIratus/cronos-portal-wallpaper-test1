from django.urls import path
from .views import wallpaper_list, wallpaper_detail

urlpatterns = [
    path('', wallpaper_list, name='wallpaper_list'),
    path('wallpaper/<int:pk>/', wallpaper_detail, name='wallpaper_detail'),
]