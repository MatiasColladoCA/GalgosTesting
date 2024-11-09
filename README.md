# GalgosTesting

Se usa Github con todos los archivos excepto la base de datos que se despliega en Render.
El archivo 'requirements.txt' proveerá a Render de los requerimientos para levantar el Backend.
El '.env' contiene la URL de nuestro DDBB desplegado en Render.

Render provee la infraestructura para tener una base de datos PostgreSQL y un servidor para desplegarla

1. Iniciar sesión en Render y vincular el repositorio de github
2. Crear proyecto en Render para almacenar tanto el servidor como la BBDD
3. Crear (New +) Web Service
    1. Selccionar repositorio
    2. Nombrar Web Service
    3. Seleccionar proyecto
    4. Seleccionar Region cercana
    5. Seleccionar rama que contiene el código
    6. Configurar Build ('pip install -r requirements.txt) y Start Command (en este caso se usa 'python app.py' para ejecutar python con Flask)
    7. Seleccionar instancia gratuita
    8. Configurar variable de entorno con 'Add from .env'.
5. Crear (New +) PostgreSQL
    1. Nombrar DDBB
    2. Seleccionar proyecto
    3. Seleccionar Region cercana
    4. Seleccionar intancia gratuita
    5. Pulsar en 'Create Database'
    6. Dentro de las configuraciones de 'info' de nuestra DDBB (projectName/production/DBName) pulsamos Connect para extraer el URL que irá dentro del '.env'.
