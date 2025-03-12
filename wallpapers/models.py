from django.db import models

class Wallpaper(models.Model):
    category = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.CharField(max_length=200)
    image_download = models.ImageField(upload_to='download/')
    image_preview = models.ImageField(upload_to='preview/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title