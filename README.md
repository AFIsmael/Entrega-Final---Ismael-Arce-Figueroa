# Instrucciones para ejecutar este proyecto

### Clonar el proyecto
```bash
git clone https://github.com/AFIsmael/Entrega-Intermedia---Ismael-Arce-Figueroa

cd Entrega-Intermedia---Ismael-Arce-Figueroa

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

### Activar entorno virtual
(Windows)
```bash
.\venv\Scripts\activate
```

(Linux)
```bash
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

# Funcionalidades de la pagina

## Buscar un curso 

- En home encontraremos un buscardor del listado de cursos disponibles, solo hace falta ingresar alguno de los datos solicitados.

[![search.png](https://i.postimg.cc/T3Fk4Cxy/search.png)](https://postimg.cc/w15ct57H) 


## visualizar la lista completa de cursos o crear uno nuevo.

- navegar a la pagina  "Courses" en la barra de navegacion del blog  
- ahi encontraras la lista completa de cursos, y trendras la posibilidad de crear uno nuevo simplemente clickeando en el boton "NEW COURSE"


[![course.png](https://i.postimg.cc/sD9Q8XR5/course.png)](https://postimg.cc/JG0zHR0h)




## crear un nuevo Profesor/Entrenador

- navegar a la pagina  "Trainers" en la barra de navegacion del blog.  
- veras a los Trainers registrados y tendras la posibilidad de registrar un nuevo, simplemente clickeando en el boton "TRAINER REGISTRATION"


[![trainers.png](https://i.postimg.cc/fRmH1YRB/trainers.png)](https://postimg.cc/ZWYFdB3d)



## crear un nuevo Estudiante

- navegar a la pagina  "Students" en la barra de navegacion del blog.  
- tendras la posibilidad de registrar un nuevo estudiante, simplemente clickeando en el boton "STUDENT REGISTRATION"

[![student.png](https://i.postimg.cc/YCHVrdVJ/student.png)](https://postimg.cc/7fKXXnqV)





