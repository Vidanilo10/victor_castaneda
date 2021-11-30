# Prueba software developer Victor Danilo Castañeda

## Presentación:
Este repositorio contiene el desarrollo de la prueba de la para la empresa Olimpia.
El repositorio cuenta con dos partes:
    1. Prueba teorica: Tiene la solución teorica dentro de un archivo .docx
    2. Prueba Practica: Contiene la solución practica en dos partes compartiendo un mismo entorno virtual
    para los dos puntos:
        - Primer Punto: Es un paquete de Python con un modulo.
        - Segundo Punto: Es un servicio web (API) desarrollado en Django y Django rest framework


## ¿Cómo utilizarlo?

```
$ # Obtener el código
$ git clone https://github.com/Vidanilo10/victor_castaneda.git
$ cd victor_castaneda/prueba_practica
$
$ # Virtualenv (Para sistemas Unix)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv (Para sistemas Windows)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Instalar las dependencias necesarias
$ pip3 install -r requirements.txt
```

Aqui ya se podría probar el primer punto de la siguiente manera:
```
$ cd prueba_practica/primer_punto
$ python main.py "--nombre_archivo.csv" (Opcional)
$ python main.py
```

Para probar el segundo punto, desde la carpeta victor_castaneda:
```
$ cd prueba_practica/segundo_punto
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
Con estos pasos ya podriamos ir a:
[a link](http://localhost:8000/facturas) o [a link](https://127.0.0.1:8000) 


## Estructura de carpetas  
|-- prueba_practica/
|    |-- env/
|    |-- primer_punto/
|        |-- input.csv
|        |-- main.py
|    |-- segundo_punto/
|        |-- facturas_electronicas/
|        |-- web_project/
|    |-- .gitignore
|    |-- Prueba Practica Software Developer.docx
|-- prueba_teorica/
|    |-- Prueba Teorica Software Developer.docx
|   |