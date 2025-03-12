from django.shortcuts import render, get_object_or_404
from .models import Wallpaper

def wallpaper_list(request):
    wallpapers = Wallpaper.objects.filter(is_active=True)
    return render(request, 'wallpapers/wallpaper_list.html', {'wallpapers': wallpapers})

def wallpaper_detail(request, pk):
    wallpaper = get_object_or_404(Wallpaper, pk=pk)
    return render(request, 'wallpapers/wallpaper_detail.html', {'wallpaper': wallpaper})