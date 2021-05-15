# GameOverWeb


Esta pagina web a sido creada con Django, MySql y Bootstrap, ambientada al mundo gaming le permite crear usuarios, perfiles y subir posts acerca de sus video juegos favoritos.

Para usar la aplicación puede seguir estas indicaciones.

- Después de tener el repositorio en su PC debe asegurarse de instalar la base de datos MySql que esta en la carpeta BD.
- La aplicación se esta conectando a través del usuario root , debe modificar la clave en el campo PASSWORD si usted cuenta con una clave root, esta parte del código se encuentra en la carpeta gameoverweb/settings.py en la linea de código numero 79.
- Ahora solo falta poner a andar el server, desde la linea de comandos ingrese

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gameoverdb',
        'USER': 'root',
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT':''
    }
}
```
- Ahora solo falta poner a andar el server, desde la linea de comandos ingrese los siguientes comandos en orden.

```
server\Scripts\activate
```

```
py manage.py runserver
```


Imágenes  obtenidas en:
- https://cdn.statically.io/img/www.itl.cat/pngfile/big/4-42212_animated-gif-wallpaper-paper-use-share-or-download.gif
- https://i.pinimg.com/originals/c5/3f/60/c53f60a4b9b160ffa3e79fbcbfb4e2a4.gif

