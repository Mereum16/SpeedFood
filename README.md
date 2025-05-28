# Django-CRUD-SQLite3

CRUD completo con Python, Django y una base de datos SQLite3, usando el patrón de arquitectura MTV (Modelo - Plantilla - Vista), el ORM de Django, el framework CSS Bootstrap y control de eventos con JavaScript.

# Iniciar Proyecto

python manage.py runserver desde cmd

# agregar productos 

python manage.py shell

from Aplicaciones.Academico.models import Producto

# Ejemplo de producto : 

Producto.objects.create(nombre="Pizza", precio=1300, imagen_url="https://www.ocu.org/-/media/ocu/images/home/alimentacion/alimentos/pizzas_selector_1600x900.jpg?rev=6a81e278-07fc-4e95-9ba1-361063f35adf&hash=B8B1264AB6FC3F4B1AE140EB390208CD")

# Si realizas cambios en los modelos o vistas recargalos con

python manage.py makemigrations

python manage.py migrate

# Cambios en la database

Si se realizan cambios en la database se deben eliminar todas las carpetas de migrations excepto init.py

# instalacion de requerimientos

pip install txt.requeriments
