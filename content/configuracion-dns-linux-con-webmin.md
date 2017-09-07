Title: Configuración DNS Linux con Webmin
Date: 2013-10-17 15:09
Author: egongu90
Category: Linux
Tags: Bind, Bind9, configuracion, Debian, DNS, linux, Server Linux, Tutorial, Webmin
Slug: configuracion-dns-linux-con-webmin
Status: published

En este tutorial/practica voy a explicar como configurar las DNS en un
servidor Linux bajo la aplicacion gráfica Webmin.  
Para realizar este tutorial voy a utilizar la distribución cliente de
Debian, se puede realizar con cualquier SO Linux este ejercicio, pero
podrían variar los pasos a seguir durante la configuración del sistema.  
<!--more-->

-Primero se instala el servidor de Linux, en mi caso uso Debian  
-Durante la instalación te solicitara que servicios de servidor se
quieren instalar, en nuestro caso seleccionamos DNS
[![1](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/1.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/1.png)

-Una vez instalado, se descarga e instala el Webmin desde la pagina
oficial.  
-Una vez instalado se entra en el navegador y se escribe la dirección
http://localhost:10000 , esto podría variar y ser el nombre del dominio
si se ha creado, también puede salir una rectificación del enlace, se
selecciona ese y se pasa a la pagina de login de Webmin  
-Una vez entrado con tu cuenta de usuario,se pincha sobre la pestaña
servers y dentro de esa BIND DNS Server.  
-Dentro de la pantalla de configuracion de DNS se observa que en la
parte de abajo esta la zona donde estan las zona que tenemos creadas de
DNS, se da a crear zona maestra y se configura de la siguiente
forma.[![2](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/2.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/2.png)

-Se vuelve a la pantalla principal dándole a module index y una vez allí
se da a apply configuración y después a crear otra zona maestra  
-Se configura de la siguiente forma
[![3](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/3.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/3.png)

-Se crea, se vuelve a module index y se aplica la configuración como
antes.  
-Se entra en la zona server y se selecciona address, una vez allí se
configura de la siguiente forma y se da a crear
[![4](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/4.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/4.png)

-Índice de modulo y aplicar configuración  
-Se accede donde antes y en vez de seleccionar address se selecciona
name alias y se configura así  

[![5](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/5.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/5.png)

-Índice de modulo, aplicar configuración  
-Se accede a la zona server, y a ahí se entra en mail server, se
configura
[![6](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/6.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/6.png)

-Ahora se configura el cliente con la Ip necesaria
[![7](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/7.png?w=229)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/7.png)

-Para que el servidor actúe como cliente y resuelva sus propias DNS hay
que configurar lo siguiente:  
-Entrar en configuración de red, nombre de máquina y DNS y configurar
lo siguiente  

[![8](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/8.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/8.png)

Después entrar a ruteo y gateways y configurar lo siguiente
[![9](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/9.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/9.png)

-Y por último, entrar a interfaces y configurar de esta forma
[![10](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/10.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/10.png)

-Se crea y aplica y ya estaría configurado el server  
Para comprobar que funciona el servicio DNS, desde el cliente se entra
en aplicaciones/herramientas del sistema/ herramientas de red  
-Dentro de la aplicación se selecciona lookup y se comprueba de la
siguiente forma  
-De forma directa
[![11](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/11.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/11.png)

-De forma inversa
[![12](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/12.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/12.png)

-Se comprueba que el servicio DNS funciona correctamente en otros/Estado
del sistema y servidor y quedaría seleccionado con un check verde el
servicio
[![13](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/13.png?w=300)](http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/13.png)

Con esto y estaría configurado el servicio DNS localmente.  
Puede fallar dependiendo de los nombres que se le asigne, suele dar
fallo al ponerlo con mayúsculas
