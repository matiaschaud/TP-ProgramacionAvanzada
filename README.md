# Algunas consideraciones de uso:
## Pipenv:
Para la virtualización del proyecto se utilizó Pipenv. Para la instalación y uso del mismo seguir los siguientes pasos:

1. Instalar pipenv: 
```
pip install pipenv
```
2. Luego para levantar el entorno virtual y que se instalen los paquetes configurados en el archivo Pipfile, parandonos en el directorio donde hayamos clonado el repositorio ejecutar:
```
pipenv shell
```

## Django:
Los comandos principales de uso de Django son:
+ **Creamos un proyecto desde cero**: django-admin startproject [nombre proyecto]
+ **Argegamos una app al proyecto**: python manage.py startapp [nombre app]
+ **Incluimos o migramos los modelos como script**: python manage.py makemigrations [nombre app]
+  **Generamos los modelos en la bbdd ya migrados**: python manage.py migrate [nombre app]
+ **Corremos el servidor**: python manage.py runserver
