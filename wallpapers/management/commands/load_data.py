from django.core.management.base import BaseCommand
from wallpapers.models import Wallpaper

class Command(BaseCommand):
    help = 'Carga datos iniciales de fondos de pantalla'

    def handle(self, *args, **kwargs):
        wallpapers = [
            {
                'category': 'Naturaleza',
                'title': 'Montañas',
                'description': 'Fondo de pantalla de montañas.',
                'price': 5.00,
                'tags': 'naturaleza, montañas',
                'image_download': 'download/montana.jpg',
                'image_preview': 'preview/montana.jpg',
                'is_active': True,
            },
            {
                'category': 'Tecnología',
                'title': 'Circuitos',
                'description': 'Fondo de pantalla de circuitos electrónicos.',
                'price': 7.00,
                'tags': 'tecnología, circuitos',
                'image_download': 'download/technology-circuit.jpg',
                'image_preview': 'preview/technology-circuit.jpg',
                'is_active': True,
            },
            {
                'category': 'Mascotas',
                'title': 'Husky',
                'description': 'Fondo de pantalla de perritos.',
                'price': 15.00,
                'tags': 'naturaleza, animales',
                'image_download': 'download/torgal01.png',
                'image_preview': 'preview/torgal01.png',
                'is_active': True,
            },
            {
                'category': 'Mascotas',
                'title': 'Husky',
                'description': 'Fondo de pantalla de perritos.',
                'price': 15.00,
                'tags': 'naturaleza, animales',
                'image_download': 'download/torgal02.jpg',
                'image_preview': 'preview/torgal02.jpg',
                'is_active': True,
            },            
            # Agrega más fondos de pantalla según sea necesario
        ]

        for wallpaper in wallpapers:
            Wallpaper.objects.create(
                category=wallpaper['category'],
                title=wallpaper['title'],
                description=wallpaper['description'],
                price=wallpaper['price'],
                tags=wallpaper['tags'],
                image_download=wallpaper['image_download'],
                image_preview=wallpaper['image_preview'],
                is_active=wallpaper['is_active'],
            )

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente.'))