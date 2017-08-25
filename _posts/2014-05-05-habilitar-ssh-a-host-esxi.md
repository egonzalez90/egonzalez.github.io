---
id: 513
title: Habilitar SSH a host ESXi
date: 2014-05-05T22:20:10+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=513
permalink: /habilitar-ssh-a-host-esxi/
snap_isAutoPosted:
  - "1"
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
image: /wp-content/uploads/2014/05/Captura13-672x372.png
categories:
  - Virtualizacion
tags:
  - connection refused
  - error
  - esxi
  - host
  - putty
  - ssh
  - vcenter
  - virtualizacion
  - vmware
  - vSphere
---
&nbsp;

Cuando instalas un host ESXi, lo normal es acceder a el a través de vSphere Client, web client o por un vCenter por alguno de los modos anteriores. El problema es que hasta que no lo necesitas, no te acuerdas de que existe el SSH, y el día que lo necesites no podrás utilizarlo... Es la Ley de Murphy.<!--more-->

Lo mas normal es acceder por SSH con un cliente como PUTTY, pues bien, una vez pones la direccion IP o el FQDN del host ESXi y das a conectar(esto tambien pasa desde una consola de Linux), te sale este mensaje de conexion rechazada. <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura13.png"><img class="aligncenter size-full wp-image-514" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura13.png" alt="Captura" width="672" height="424" /></a>

Esto se debe a que por defecto, los host ESXi tienen deshabilitado el acceso por SSH. Para habilitarlo, tenemos dos métodos: Desde vSphere Client al ESXi o vCenter, o desde el propio host ESXi
<p style="text-align: center;"><span style="color: #ff0000;"><em><strong>vSphere Client</strong></em></span></p>
<p style="text-align: left;">Una vez hemos accedido al VSphere Client, pulsaremos sobre el host al que queramos habilitar SSH, aquí iremos a la pestaña superior de Configuration.<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura14.png"><img class="aligncenter size-full wp-image-515" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura14.png" alt="Captura1" width="986" height="495" /></a></p>
<p style="text-align: left;">Una vez dentro de la pestaña de Configuration, buscaremos por la barra lateral izquierda Security Profile, dentro de Software, nos mostrara esta ventana en la que iremos a el botón de Properties de la parte superior derecha<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura21.png"><img class="aligncenter size-full wp-image-516" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura21.png" alt="Captura2" width="1715" height="495" /></a></p>
<p style="text-align: left;">Esto nos abrirá esta ventana en la que buscaremos SSH, veremos que esta en estado Stoped, pulsaremos sobre el botón Options</p>
<p style="text-align: left;"><a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura31.png"><img class="aligncenter size-full wp-image-517" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura31.png" alt="Captura3" width="657" height="691" /></a></p>
<p style="text-align: left;">Aqui marcaremos la segunda opción para que inicie el servicio con el arranque y parada del host ESXi, ademas también pulsaremos sobre el botón Start para iniciar el servicio en estos momentos y finalizaremos pulsando sobre el botón OK</p>
<p style="text-align: left;"><a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura41.png"><img class="aligncenter size-full wp-image-518" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura41.png" alt="Captura4" width="504" height="337" /></a></p>
<p style="text-align: left;">Ahora nos quedaría comprobar que efectivamente tenemos acceso al host a través de SSH.</p>
<p style="text-align: left;">Una vez pongamos la dirección de nuestro host en PuTTY, en vez de mostrarnos el mensaje de error, nos pedirá que aceptemos la clave del host, esto lo haremos pulsando sobre Si<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura51.png"><img class="aligncenter size-full wp-image-519" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura51.png" alt="Captura5" width="443" height="299" /></a></p>
<p style="text-align: left;">Se nos abrirá una consola de comandos en la que introduciremos el usuario y contraseña del host ESXi.</p>
<p style="text-align: left;">Ya estaríamos conectados por SSH<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura61.png"><img class="aligncenter size-full wp-image-520" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura61.png" alt="Captura6" width="671" height="419" /></a></p>
<p style="text-align: center;"><em><strong><span style="color: #ff0000;">Host ESXi</span></strong></em></p>
<p style="text-align: left;">Ahora haremos lo mismo que anteriormente pero a través del propio host.</p>
<p style="text-align: left;">Para entrar en el menú de configuración, pulsaremos F2, esto nos pedirá usuario y contraseña. Una vez loggeados, veremos esta pantalla, aquí iremos a la opción Troubleshootin Options y pulsaremos Enter<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura71.png"><img class="aligncenter size-full wp-image-521" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura71.png" alt="Captura7" width="1022" height="752" /></a></p>
<p style="text-align: left;">Nos abrira esta otra pantalla en la que observamos que tenemos SSH deshabilitado, nos ponemos sobre Enable SSH y pulsamos Enter<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura81.png"><img class="aligncenter size-full wp-image-522" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura81.png" alt="Captura8" width="849" height="165" /></a></p>
<p style="text-align: left;">Como vemos ahora tenemos SSH habilitado y tendríamos acceso remoto desde PuTTY</p>
<p style="text-align: left;">Esta forma es mas sencilla que la anterior, pero deberemos de tener algún tipo de acceso hacia nuestro host para poder configurarlo<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura91.png"><img class="aligncenter size-full wp-image-523" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura91.png" alt="Captura9" width="1036" height="233" /></a></p>
<p style="text-align: left;">Espero les sirva de ayuda.</p>
<p style="text-align: left;">Un saludo.</p>