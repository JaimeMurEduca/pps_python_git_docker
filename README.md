# La bayeta de la fortuna
Aplicación usada para proporcionar un mensaje auspicioso.
## Forma de uso
	1. Utilizar el comando pyhton3 app.py para ejecutarlo
	2. Acceder a la url http://127.0.0.1:5000/frotar/"tu numero a eleccion" para obtener las frases
## Dependencias
Las dependecias se redactan en el fichero requirements.txt
##DOCKER
#Creación de la imagen
Para la creación de la imagen en docker tendras que usar el comando: docker build "nombre de tu imagen".
#Creación del contenedor
Para la creación de tu contenedor docker tendras que primero localizar el nombre de tu imagen con "docker ps -a".
Una vez lo tengas para crearlo tendras que usar el comando "docker run 'nombre de imagen'". Una vez creado, para arrancarlo usaras el comando: "docker start 'nombre de imagen'", y para acceder a el, el comando: "docker exec -it 'nombre de imagen' /bin/bash".
## Desarrollo
Este proyecto esta siendo desarrollado en pyhton, docker y git.
