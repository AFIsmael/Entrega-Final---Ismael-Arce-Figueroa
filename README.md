## Este proyecto se encuentra desarrollado integramente por mi, **Ismael Arce Figueroa**.

## Se trata de una pagina web utilizada como un blog de Cursos, como entrega de proyecto final del curso de Python en CoderHouse.
## La misma fue creada a partir de los conocimientos adquiridos en el curso, utilizando varias tecnologias en ella.
## Como ser Python - Django - html y CSS.  


## A continuacion estan las instrucciones para poder clonar el proyecto y poder desplegarlo. Gracias por tu visita. Saludos!!!

# Instrucciones para ejecutar este proyecto

### Clonar el proyecto
```bash
git clone https://github.com/AFIsmael/Entrega-Final---Ismael-Arce-Figueroa.git

cd Entrega-Final---Ismael-Arce-Figueroa

```

### Crear y activar entorno virtual (Windows)
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```

### Instalar las dependencias del proyecto
```bash
pip install -r requirements.txt
```


### Se ejecuta la migración para crear la base de datos con la que trabajará nuestro proyecto de Django
```bash
python manage.py migrate
```

### Se levanta el servidor de Django que expone el servicio por el localhost en el puerto 8000 por defecto `http://127.0.0.1:8000/` 
```bash
python manage.py runserver
```

### Si queremos levantar el servidor de Django en otro puerto lo especificamos de la siguente manera. e.g. `http://127.0.0.1:8001/`
```bash
python manage.py runserver 8001
```


### Se crea el super usuario para nuestro proyecto de Django, **Solo si no se ha creado**
```bash
python manage.py createsuperuser
```
Ingrese `Username`, `Email address` y `Password`  




