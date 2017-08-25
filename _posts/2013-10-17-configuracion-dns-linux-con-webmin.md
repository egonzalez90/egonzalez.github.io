---
id: 186
title: Configuración DNS Linux con Webmin
date: 2013-10-17T15:09:55+00:00
author: Editor
layout: post
guid: http://openmindinside.wordpress.com/?p=186
permalink: /configuracion-dns-linux-con-webmin/
publicize_facebook_url:
  - https://facebook.com/1161837279_10201428757818506
  - https://facebook.com/1161837279_10201428757818506
  - https://facebook.com/1161837279_10201428757818506
  - https://facebook.com/1161837279_10201428757818506
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
kopa_resolution_total_view:
  - "1"
image: /wp-content/uploads/2013/10/13.png
categories:
  - Linux
tags:
  - Bind
  - Bind9
  - configuracion
  - Debian
  - DNS
  - linux
  - Server Linux
  - Tutorial
  - Webmin
---
En este tutorial/practica voy a explicar como configurar las DNS en un servidor Linux bajo la aplicacion gráfica Webmin.
Para realizar este tutorial voy a utilizar la distribución cliente de Debian, se puede realizar con cualquier SO Linux este ejercicio, pero podrían variar los pasos a seguir durante la configuración del sistema.
<!--more-->

-Primero se instala el servidor de Linux, en mi caso uso Debian
-Durante la instalación te solicitara que servicios de servidor se quieren instalar, en nuestro caso seleccionamos DNS <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/1.png"><img class="aligncenter size-medium wp-image-187" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/1.png?w=300" alt="1" width="300" height="232" /></a>

-Una vez instalado, se descarga e instala el Webmin desde la pagina oficial.
-Una vez instalado se entra en el navegador y se escribe la dirección http://localhost:10000 , esto podría variar y ser el nombre del dominio si se ha creado, también puede salir una rectificación del enlace, se selecciona ese y se pasa a la pagina de login de Webmin
-Una vez entrado con tu cuenta de usuario,se pincha sobre la pestaña servers y dentro de esa BIND DNS Server.
-Dentro de la pantalla de configuracion de DNS se observa que en la parte de abajo esta la zona donde estan las zona que tenemos creadas de DNS, se da a crear zona maestra y se configura de la siguiente forma.<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/2.png"><img class="aligncenter size-medium wp-image-188" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/2.png?w=300" alt="2" width="300" height="148" /></a>

-Se vuelve a la pantalla principal dándole a module index y una vez allí se da a apply configuración y después a crear otra zona maestra
-Se configura de la siguiente forma <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/3.png"><img class="aligncenter size-medium wp-image-189" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/3.png?w=300" alt="3" width="300" height="169" /></a>

-Se crea, se vuelve a module index y se aplica la configuración como antes.
-Se entra en la zona server y se selecciona address, una vez allí se configura de la siguiente forma y se da a crear <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/4.png"><img class="aligncenter size-medium wp-image-190" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/4.png?w=300" alt="4" width="300" height="92" /></a>

-Índice de modulo y aplicar configuración
-Se accede donde antes y en vez de seleccionar address se selecciona name alias y se configura así
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/5.png"><img class="aligncenter size-medium wp-image-191" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/5.png?w=300" alt="5" width="300" height="53" /></a>

-Índice de modulo, aplicar configuración
-Se accede a la zona server, y a ahí se entra en mail server, se configura <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/6.png"><img class="aligncenter size-medium wp-image-192" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/6.png?w=300" alt="6" width="300" height="99" /></a>

-Ahora se configura el cliente con la Ip necesaria <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/7.png"><img class="aligncenter size-medium wp-image-193" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/7.png?w=229" alt="7" width="229" height="300" /></a>

-Para que el servidor actúe como cliente y resuelva sus propias DNS hay que configurar lo siguiente:
-Entrar en configuración de red, nombre de máquina y DNS y configurar lo siguiente
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/8.png"><img class="aligncenter size-medium wp-image-194" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/8.png?w=300" alt="8" width="300" height="104" /></a>

Después entrar a ruteo y gateways y configurar lo siguiente <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/9.png"><img class="aligncenter size-medium wp-image-195" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/9.png?w=300" alt="9" width="300" height="148" /></a>

-Y por último, entrar a interfaces y configurar de esta forma <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/10.png"><img class="aligncenter size-medium wp-image-196" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/10.png?w=300" alt="10" width="300" height="221" /></a>

-Se crea y aplica y ya estaría configurado el server
Para comprobar que funciona el servicio DNS, desde el cliente se entra en aplicaciones/herramientas del sistema/ herramientas de red
-Dentro de la aplicación se selecciona lookup y se comprueba de la siguiente forma
-De forma directa <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/11.png"><img class="aligncenter size-medium wp-image-197" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/11.png?w=300" alt="11" width="300" height="256" /></a>

-De forma inversa <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/12.png"><img class="aligncenter size-medium wp-image-198" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/12.png?w=300" alt="12" width="300" height="161" /></a>

-Se comprueba que el servicio DNS funciona correctamente en otros/Estado del sistema y servidor y quedaría seleccionado con un check verde el servicio <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/13.png"><img class="aligncenter size-medium wp-image-199" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2013/10/13.png?w=300" alt="13" width="300" height="208" /></a>

Con esto y estaría configurado el servicio DNS localmente.
Puede fallar dependiendo de los nombres que se le asigne, suele dar fallo al ponerlo con mayúsculas