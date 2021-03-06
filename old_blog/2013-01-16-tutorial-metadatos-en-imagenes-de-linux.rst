Hola buenas  todos, en esta entrada tratare el tema de
la edición y visualización de metadatos en SO linux, para ser mas
exactos en distribuciones de Ubuntu.

Los temas a tratar seran:

-  Que son los metadatos y porque son peligrosos
-  Visualizacion de metadatos en modo consola
-  Edicion de metadatos por consola

Los metadatos y el gran peligro que corremos con ellos
======================================================

Los metadatos es aquella informacion que el ordenador guarda en los
documentos, imagenes, etc y que a traves de ellos se pueden ver mucha
mas informacion de la que se cree sobre la persona que desarrollo el
archivo.

Entre esos datos se pueden ver la IP, el nombre de usuario del equipo
(muy importante para realizar intrusiones) las cordenadas si se realizo
desde un movil con GPS, etc.

Curiosamente a la gran mayoria de hackers o delicuentes informaticos les
han localizado y detenido gracias o por culpa de estos metadatos, al no
tener cuidado y subir un foto al twitter desde el movil. Al lado
contrario muchos hackers han perdido menos tiempo en atacar a un equipo
al conocer el nombre de usuario que creo el documento y la IP.

Precisamente tanto si eres hacker o como si eres un fan de evitar
esparcir tus datos por la web este brebe tutorial introductorio a los
metadatos les servira de gran ayuda en el camino de la seguridad
informatica.

Con esto conprenderan la importancia que tiene el saber borrar estos
datos, que a simple vista no se ven, pero que estan escondidos detras de
los archivos.

Visualizacion de metadatos en modo consola de linux
===================================================

Hay poca variedad de aplicaciones en modo grafico para esta tarea en
linux, algun editor de imagenes te deja modificar estos datos, pero la
mayoria no.

Por suerte en modo texto hay algunas poca mas, como pueden ser mogrify,
jhead o exiftool.

En nuestro caso vamos a utilizar jhead, por lo que deberemos instalarlo
en nuestro equipo con el comando adecuado con permisos de root:

-  sudo apt-get install jhead

Si no lo encontrara mediante el comando   apt    , deberas buscar por
internet el paquete jhead y descargarlo para la arquitectura de vuestro
equipo, con la terminacion en .deb e instalar mediante el comando :

-  cd  /directoriodondesehadescargadoelpaquete
-  dpkg -i ./archivodescargado.deb

Después de esto deberia de tener instalado la apliccion jhead.

Ahora solo quedaria acceder al directorio donde tenga la imagen a
analizar, en mi caso :

-  cd /home/nombredeusuario/Descargas

Se ejecuta el comando

-  jhead ./nombredelarchivo.jpeg

Esto nos mostraria la informacion que tiene almacenada la imagen, que
seria algo como esto:

| File name : 2515947973_883a9fe61c_o.jpg
| File size : 5171920 bytes
| File date : 2013:01:07 02:54:45
| Camera make : NIKON CORPORATION
| Camera model : NIKON D100
| Date/Time : 2008:01:19 14:18:36
| Resolution : 3022 x 2012
| Flash used : No
| Focal length : 16.0mm (35mm equivalent: 24mm)
| Exposure time: 0.625 s
| Aperture : f/11.0
| ISO equiv. : 200
| Whitebalance : Auto
| Exposure : Manual
| Exposure Mode: Manual

Esto dependiendo la imagen podra tener mas o menos datos, con las fotos
tomadas desde moviles suelen tener varios datos mas

Editado y borrado de los metadatos
==================================

Jhead nos da varias opciones que estan disponibles realizando el comando
man

-  man jhead

Esto nos daria una breve descripcion en ingles sobre la aplicacion asi
como de sus opciones y posibilidades.

Para borrar los metadatos de la foto anterior lo que deberiamos hacer es
recurrir a este comando

-  jhead -de nombredearchivo.jpeg

Y al hacer otra vez uso de jhead para comprobar el estado de los
metadatos deberia de quedar algo asi:

| File name : 2515947973_883a9fe61c_o.jpg
| File size : 5157332 bytes
| File date : 2013:01:07 02:54:45
| Resolution : 3022 x 2012

Para mas opciones debera sustituir   -de  por la opcion que explique  
 man   y que mas concuerde con nuestros deseos.

Un saludo y gracias por leer
