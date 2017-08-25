---
id: 481
title: Instalacion vCenter Appliance
date: 2014-05-04T16:32:47+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=481
permalink: /instalacion-vcenter-appliance/
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
ac_featured_article:
  - ""
ac_show_post_thumbnail:
  - "1"
kopa_resolution_total_view:
  - "1"
image: /wp-content/uploads/2014/05/Captura9-663x372.png
categories:
  - Virtualizacion
tags:
  - appliance
  - configuracion
  - error SSO
  - esxi
  - instalacion
  - vcenter
  - virtualizacion
  - vmware
  - vSphere
---
En esta entrada mostrare como instalar vCenter Appliance, muchos seréis los que os habréis encontrado los errores de SSO al hacer la instalación por defecto de vCenter(yo también fui de esos), por eso estuve investigando y conseguí instalarlo sin los errores.
<!--more-->El error de SSO le solucione configurando antes de iniciar el Wizard de configuracion la red correctamente en modo estatico. Para ello iremos al SO instalado de vCenter y daremos en Login <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura0.png"><img class="aligncenter size-full wp-image-483" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura0.png" alt="Captura0" width="724" height="407" /></a>

Esto nos abrira una consola, en la que nos pide login, el usuario por defecto es root y la password vmware <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura1.png"><img class="aligncenter size-full wp-image-484" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura1.png" alt="Captura1" width="512" height="147" /></a>

Una vez loggeados dentro del sistema, iremos a esta ruta en la que nos abrira un wizard de configuracion basica de la red.

/opt/vmware/share/vami/vami_config_net

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura.png"><img class="aligncenter size-full wp-image-482" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura.png" alt="Captura" width="625" height="208" /></a>Seleccionaremos para empezar la opcion 6, con la que editaremos la configuracion de la tarjeta de red eth0.

Nos preguntara si queremos usar IPv6, le daremos que no.

Nos preguntara si queremos utilizar IPv4, aqui damos yes.

Nos preguntara si queremos usar DHCP, a lo que daremos que no.

A continuacion nos solicitara que pongamos una direccion IP valida y despues una mascara de red

Por ultimo nos mostrara un resumen de la configuracion y daremos a yes si estamos de acuerdo

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura2.png"><img class="aligncenter size-full wp-image-485" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura2.png" alt="Captura2" width="625" height="358" /></a>

A continuacion configuraremos la puerta de enlace(gateway), para ello usaremos la opcion 2 del Main Menu.

Nos pedira que seleccionemos una tarjeta de red para configurar la default gateway, aqui yo uso eth0 por lo que selecciono la opcion 0.

A continuacion tendremos que poner la puerta de enlace correctamente, como veis hay que rellenar con tres cifras, por lo que me dio error cuando solo use 1<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura3.png"><img class="aligncenter size-full wp-image-486" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura3.png" alt="Captura3" width="645" height="214" /></a>

A continuacion configuraremos los servidores DNS de nuestro vCenter, para ello usamos la opcion 4 del Main Menu

Aqui nos pedira dos servidores DNS, el segundo es opcional<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura4.png"><img class="aligncenter size-full wp-image-487" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura4.png" alt="Captura4" width="556" height="195" /></a>

Lo siguiente seria configurar el hostname del vCenter con la opcion 3, pondremos un hostname correcto<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura5.png"><img class="aligncenter size-full wp-image-488" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura5.png" alt="Captura5" width="544" height="172" /></a>

Por ultimo daremos a la opcion 0 del Main Menu para ver la configuracion completa de la red, comprobaremos que este todo correcto y pulsaremos la opcion 1 para salir del wizard<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6.png"><img class="aligncenter size-full wp-image-489" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6.png" alt="Captura6" width="395" height="206" /></a>

A continuacion iremos a un navegador e iremos a la direccion https://IP:5480, nos loggearemos con el usuario root y password vmware<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6_1.png"><img class="aligncenter size-full wp-image-490" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6_1.png" alt="Captura6_1" width="833" height="285" /></a>

Nos saldra este asistente, aceptaremos los terminos de licencia y uso.<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura7.png"><img class="aligncenter size-full wp-image-491" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura7.png" alt="Captura7" width="754" height="702" /></a>

A continuacion marcaremos la opcion Configure whit default settings y daremos a Next para configurarlo por defecto, aqui tambien puedes configurarlo a tu gusto,yo uso la opcion por defecto para este tutorial<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura8.png"><img class="aligncenter size-full wp-image-492" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura8.png" alt="Captura8" width="666" height="460" /></a>

Nos saldra un resumen en el que tendremos que tener estas opciones asi:
<ul>
	<li>Database: Embedded
SSO: Embedded
SSO Database: Embedded
AD Enabled: No</li>
</ul>
Una vez comprobado esto pulsaremos en Start<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura9.png"><img class="aligncenter size-full wp-image-493" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura9.png" alt="Captura9" width="663" height="458" /></a>

Despues de esperar un buen rato, nos deberia aparecer todos los check en verde sin errores, de ser asi pulsaremos en Close

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura10.png"><img class="aligncenter size-full wp-image-494" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura10.png" alt="Captura10" width="663" height="464" /></a>

A continuacion iremos a vSphere Client, pondremos la direcion Ip del vCenter, usuario y contrasena.

Aqui nos pedira que aceptemos el certificado, marcaremos la opcion de Install this certificate y daremos a Ignore<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura11.png"><img class="aligncenter size-full wp-image-495" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura11.png" alt="Captura11" width="528" height="540" /></a>

Por ultimo se nos conectara al vCenter Appliance, con esto ya estaria terminado este tutorial<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura12.png"><img class="aligncenter size-full wp-image-496" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura12.png" alt="Captura12" width="1055" height="487" /></a>

Espero que les sirva de ayuda y puedan conectar sin problemas a vCenter, gracias por visitar este blog.

Un saludo