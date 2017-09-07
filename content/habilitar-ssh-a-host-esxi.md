Title: Habilitar SSH a host ESXi
Date: 2014-05-05 22:20
Author: egongu90
Category: Virtualizacion
Tags: connection refused, error, esxi, host, putty, ssh, vcenter, virtualizacion, vmware, vSphere
Slug: habilitar-ssh-a-host-esxi
Status: published

 

Cuando instalas un host ESXi, lo normal es acceder a el a través de
vSphere Client, web client o por un vCenter por alguno de los modos
anteriores. El problema es que hasta que no lo necesitas, no te acuerdas
de que existe el SSH, y el día que lo necesites no podrás utilizarlo...
Es la Ley de Murphy.<!--more-->

Lo mas normal es acceder por SSH con un cliente como PUTTY, pues bien,
una vez pones la direccion IP o el FQDN del host ESXi y das a
conectar(esto tambien pasa desde una consola de Linux), te sale este
mensaje de conexion rechazada.
[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura13.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura13.png)

Esto se debe a que por defecto, los host ESXi tienen deshabilitado el
acceso por SSH. Para habilitarlo, tenemos dos métodos: Desde vSphere
Client al ESXi o vCenter, o desde el propio host ESXi

<span style="color: #ff0000;">***vSphere Client***</span>

Una vez hemos accedido al VSphere Client, pulsaremos sobre el host al
que queramos habilitar SSH, aquí iremos a la pestaña superior de
Configuration.[![Captura1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura14.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura14.png)

Una vez dentro de la pestaña de Configuration, buscaremos por la barra
lateral izquierda Security Profile, dentro de Software, nos mostrara
esta ventana en la que iremos a el botón de Properties de la parte
superior
derecha[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura21.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura21.png)

Esto nos abrirá esta ventana en la que buscaremos SSH, veremos que esta
en estado Stoped, pulsaremos sobre el botón Options

[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura31.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura31.png)

Aqui marcaremos la segunda opción para que inicie el servicio con el
arranque y parada del host ESXi, ademas también pulsaremos sobre el
botón Start para iniciar el servicio en estos momentos y finalizaremos
pulsando sobre el botón OK

[![Capturá que aceptemos la clave del host, esto lo haremos pulsando
sobre Si\<a
href=](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura41.png)![Captura5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura51.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura41.png)

Se nos abrirá una consola de comandos en la que introduciremos el
usuario y contraseña del host ESXi.

Ya estaríamos conectados por
SSH[![Captura6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura61.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura61.png)

***<span style="color: #ff0000;">Host ESXi</span>***

Ahora haremos lo mismo que anteriormente pero a través del propio host.

Para entrar en el menú de configuración, pulsaremos F2, esto nos pedirá
usuario y contraseña. Una vez loggeados, veremos esta pantalla, aquí
iremos a la opción Troubleshootin Options y pulsaremos
Enter[![Captura7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura71.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura71.png)

Nos abrira esta otra pantalla en la que observamos que tenemos SSH
deshabilitado, nos ponemos sobre Enable SSH y pulsamos
Enter[![Captura8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura81.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura81.png)

Como vemos ahora tenemos SSH habilitado y tendríamos acceso remoto desde
PuTTY

Esta forma es mas sencilla que la anterior, pero deberemos de tener
algún tipo de acceso hacia nuestro host para poder
configurarlo[![Captura9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura91.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura91.png)

Espero les sirva de ayuda.

Un saludo.
