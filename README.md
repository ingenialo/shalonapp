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

example:

``` docker-compose run --rm django python manage.py createsuperuser ```
``` docker-compose run --rm django python manage.py migrate ```

- How to get in to the container by ssh
``` docker-compose exec django /bin/sh ```