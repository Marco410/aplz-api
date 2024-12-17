# B2bTakeHomeApp Back

Back para prueba tecnica. Utilizando Django.

Se agregara el archivo .env.dev para que puedan correr más rapido el proyecto con los datos de la base de datos, host y contraseñas para su facilidad.

```bash

# Comando para correr el proyecto
docker-compose -f docker/docker-compose.yml up --build

```

```bash

#crear un super usuario. Este usuario es para iniciar sesión en el proyecto y también para los tests.
docker-compose -f docker/docker-compose.yml exec aplz_dev_app python manage.py createsuperuser

```

```bash

#agregar los datos a la base de datos.
# Importante correr con el proyecto iniciado, para que llene la base de datos con los datos en el archivo fixtures/orders.json
# Estos datos se verán reflejados en el home y el historial
docker-compose -f docker/docker-compose.yml exec aplz_dev_app python manage.py loaddata fixtures/orders.json

```
