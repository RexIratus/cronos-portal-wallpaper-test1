# Documentación de cURL para el Portal de Fondos de Pantalla

## Obtener la lista de fondos de pantalla

Para obtener la lista de fondos de pantalla, puedes usar el siguiente comando cURL:

```
curl -X GET http://localhost:8000/
```

## Obtener detalles de un fondo de pantalla específico

Reemplaza 1 con el ID del fondo de pantalla que deseas obtener:

curl -X GET http://localhost:8000/wallpaper/1/

## Descargar una imagen

Reemplaza http://localhost:8000/media/download/montana.jpg con la URL de la imagen que deseas descargar:

```
curl -O http://localhost:8000/media/download/montana.jpg
```

#### Notas

- Asegurarse de que el servidor esté en ejecución antes de realizar las solicitudes cURL.
- Puedes usar herramientas como Postman para probar las API de manera más visual.