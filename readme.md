# Prueba software developer Victor Danilo Castañeda

## Presentación:
1. Este repositorio contiene el desarrollo de la prueba de la para la empresa Olimpia.
2. El repositorio cuenta con dos partes:
    - Prueba teorica: Tiene la solución teorica dentro de un archivo .docx
    - Prueba Practica: Contiene la solución practica en dos partes compartiendo un mismo entorno virtual
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


[http://localhost:8000/facturas link](http://localhost:8000/facturas)


[https://127.0.0.1:8000/facturas link](https://127.0.0.1:8000) 


## Estructura de carpetas 

.
├── _config.yml
├── _drafts
│   ├── begin-with-the-crazy-ideas.textile
│   └── on-simplicity-in-technology.markdown
├── _includes
│   ├── footer.html
│   └── header.html
├── _layouts
│   ├── default.html
│   └── post.html
├── _posts
│   ├── 2007-10-29-why-every-programmer-should-play-nethack.textile
│   └── 2009-04-26-barcamp-boston-4-roundup.textile
├── _data
│   └── members.yml
├── _site
└── index.html