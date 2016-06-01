Ejemplo utiizado para la asignatura Desarrollo de Aplicaciones Web II, usando un patron Modelo Vista Controlador (MVC) y el Framework DJango.

Importar los datos de la BD:

    ./manage.py migrate

Ejecutar la aplicacion:

    ./manage.py runserver

    Acceder a la aplicacion a traves de la URL <http://localhost:8000/>

Para que el App Server escuche peticiones por todas las interfaces, ejecutarlo con los siguientes parametros:

  ./manage.py runserver 0.0.0.0:8080

  Acceder a la aplicacion a traves de la URL <http://<IP>:8080/>
