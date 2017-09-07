Title: Instalacion vCenter Appliance
Date: 2014-05-04 16:32
Author: egongu90
Category: Virtualizacion
Tags: appliance, configuracion, error SSO, esxi, instalacion, vcenter, virtualizacion, vmware, vSphere
Slug: instalacion-vcenter-appliance
Status: published

En esta entrada mostrare como instalar vCenter Appliance, muchos seréis
los que os habréis encontrado los errores de SSO al hacer la instalación
por defecto de vCenter(yo también fui de esos), por eso estuve
investigando y conseguí instalarlo sin los errores.  
<!--more-->El error de SSO le solucione configurando antes de iniciar
el Wizard de configuracion la red correctamente en modo estatico. Para
ello iremos al SO instalado de vCenter y daremos en Login
[![Captura0](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura0.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura0.png)

Esto nos abrira una consola, en la que nos pide login, el usuario por
defecto es root y la password vmware
[![Captura1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura1.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura1.png)

Una vez loggeados dentro del sistema, iremos a esta ruta en la que nos
abrira un wizard de configuracion basica de la red.

/opt/vmware/share/vami/vami\_config\_net

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura.png)Seleccionaremos
para empezar la opcion 6, con la que editaremos la configuracion de la
tarjeta de red eth0.

Nos preguntara si queremos usar IPv6, le daremos que no.

Nos preguntara si queremos utilizar IPv4, aqui damos yes.

Nos preguntara si queremos usar DHCP, a lo que daremos que no.

A continuacion nos solicitara que pongamos una direccion IP valida y
despues una mascara de red

Por ultimo nos mostrara un resumen de la configuracion y daremos a yes
si estamos de acuerdo

[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura2.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura2.png)

A continuacion configuraremos la puerta de enlace(gateway), para ello
usaremos la opcion 2 del Main Menu.

Nos pedira que seleccionemos una tarjeta de red para configurar la
default gateway, aqui yo uso eth0 por lo que selecciono la opcion 0.

A continuacion tendremos que poner la puerta de enlace correctamente,
como veis hay que rellenar con tres cifras, por lo que me dio error
cuando solo use
1[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura3.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura3.png)

A continuacion configuraremos los servidores DNS de nuestro vCenter,
para ello usamos la opcion 4 del Main Menu

Aqui nos pedira dos servidores DNS, el segundo es
opcional[![Captura4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura4.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura4.png)

Lo siguiente seria configurar el hostname del vCenter con la opcion 3,
pondremos un hostname
correcto[![Captura5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura5.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura5.png)

Por ultimo daremos a la opcion 0 del Main Menu para ver la configuracion
completa de la red, comprobaremos que este todo correcto y pulsaremos la
opcion 1 para salir del
wizard[![Captura6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6.png)

A continuacion iremos a un navegador e iremos a la direccion
https://IP:5480, nos loggearemos con el usuario root y password
vmware[![Captura6\_1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6_1.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6_1.png)

Nos saldra este asistente, aceptaremos los terminos de licencia y
uso.[![Captura7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura7.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura7.png)

A continuacion marcaremos la opcion Configure whit default settings y
daremos a Next para configurarlo por defecto, aqui tambien puedes
configurarlo a tu gusto,yo uso la opcion por defecto para este
tutorial[![Captura8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura8.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura8.png)

Nos saldra un resumen en el que tendremos que tener estas opciones asi:

-   Database: Embedded  
    SSO: Embedded  
    SSO Database: Embedded  
    AD Enabled: No

Una vez comprobado esto pulsaremos en
Start[![Captura9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura9.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura9.png)

Despues de esperar un buen rato, nos deberia aparecer todos los check en
verde sin errores, de ser asi pulsaremos en Close

[![Captura10](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura10.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura10.png)

A continuacion iremos a vSphere Client, pondremos la direcion Ip del
vCenter, usuario y contrasena.

Aqui nos pedira que aceptemos el certificado, marcaremos la opcion de
Install this certificate y daremos a
Ignore[![Captura11](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura11.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura11.png)

Por ultimo se nos conectara al vCenter Appliance, con esto ya estaria
terminado este
tutorial[![Captura12](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura12.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura12.png)

Espero que les sirva de ayuda y puedan conectar sin problemas a vCenter,
gracias por visitar este blog.

Un saludo
