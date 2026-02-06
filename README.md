# geometry-volume-app-course
xSimulate a simple geometry volume calculator
---------------------------------
Description
---------------------------------
Este proyecto sirve para calcular el volumen de diferentes cuerpos usando python, siendo las opciones disponibles:
	- Cubo
	- Cilindro
	- Cono
	- Esfera

Ejecutando el código "main.py" podrá escoger entre las 4 cuerpo, tan solo ingresando el número del cuerpo que desee. 
Al ingresar su elección, la terminal preguntará las medidas del cuerpo, donde deberá ingresar dichos datos y presionar enter. 
Después de haber ingresado todas las medidas, se mostrará el resultado. 

		Ex. user@user:~.../geometry-volume-app-course> python3 main.py

Para terminar el programa, ingrese la opción 5. 

--------------------------------
Structure
--------------------------------
geometry-volume-app-course/
│── main.py
│── geometry/
│   ├── cube.py
│   ├── cylinder.py
│   ├── cone.py
│   └── sphere.py
│── tests/
│   ├── test_box.py
│   ├── test_cylinder.py
│   ├── test_cone.py
│   └── test_sphere.py

---------Geometry----------------

Adicional al programa principal, se pueden encontrar los códigos que operan tras main.py

Para esto, es necesario entrar primeramente al directorio geometry/

	Ex. user@user:~.../geometry-volume-app-course> cd geometry/

En este, estaran disponibles distintos codigos para ejecutar con variables predefinidas.
Para ejecutar uno de ellos, es necesario usar el comando de python3 seguido del nombre del nombre del codigo. 

	Ex. user@user:~.../geometry-volume-app-course/geometry> python3 cube.py

---------Tests----------------


Igualmente, se encuentra otro directorio "tests/" en el cual contiene programas para cada uno de los cuerpos geometricos.
En este directorio, se busca confirmar que los calculos efectuados en "geometry/" sean correctos.

Para acceder es necesario regresar al repo con "cd .." sin embargo, no es necesario encontrarse en la carpeta de testeo, puede ejecutarlo en el directorio principal de la siguiente forma:

	user@user:~.../geometry-volume-app-course> pytest

Si esto no funciona, puede probar de la siguiente manera:

	 user@user:~.../geometry-volume-app-course> python3 -m pytest  
Posteriormente, podrá observar si los códigos de geomtry pasaron las pruebas, dando a entender que los resultados son los correctos

-------Dependencies------------

Para ejecutar estos programas de test, es necesario instalar pytest, para esto ingresamos la siguiente
		Ex. user@user:~.../geometry-volume-app-course> python3 -m pip install pytest 
