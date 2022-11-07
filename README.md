# shalonapp
## 1. Tools/ Libraries
-   Docker form Python V 3.8. image

## 2.Installation

-   To clone the repository github
-   Install Docker and Docker-compose
-   create a .env file from .env_example file
-   Build docker compose
``` docker-compose build ```

## 3.how to run the project
-   run the container and the app
``` docker-compose up ```


## 5. Ussefull commands
-   Administrative commands
``` docker-compose run --rm django COMAND ```

-   For Debugging
``` docker-compose run --rm --service-ports django ```

example:

``` docker-compose run --rm django python manage.py createsuperuser ```
``` docker-compose run --rm django python manage.py migrate ```

- How to get in to the container by ssh
``` docker-compose exec django /bin/sh ```


Tareas Andres:
- Poner el valor neto incluido el descuento y poner descuento 0 siempre en el campo.
- Actualizar el cliente en siigo si existe cada que descargue la compra.
- Los items facturables deben ser que tengan pagos con tarjeta que tenga al menos sume 189.000.
- Terminar de subir el servidor


Tareas Yina
- Crear metodo de pago bono de regalo en siigo
- Definir los porcentajes de esos descuentos que se aplicaban como metodos de pagos segun estos items 
    - Descuento incentivo Tq
    - Descuento vip
    - canje
- Socializar tabla de porcentajes segun descuento
- Eliminar metodos de pago relacionados con descuento, el descuento se debe poner como un porcentage no como un metodo de pago




recorrer los items, ordenar de mayor a menor y descontar del menor a mayor segun descuento