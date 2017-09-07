Title: Servidor de mensajes Qpid
Date: 2014-11-16 17:47
Author: egongu90
Category: OpenStack
Tags: configuracion, guia, instalacion, openstack, qpid, servidor de mensaje
Slug: servidor-de-mensajes-qpid
Status: published

En nuestro entorno, necesitaremos un servidor de mensajes con el que se
comunicaran los diferentes nodos y complementos de Openstack. Openstack
soporta algunos servidores de mensajes, nosotros utilizaremos Qpid,
siendo fácil su instalación y configuración básica sin autenticacion

Instalar Qpid

> yum install qpid-cpp-server

Deshabilitar el uso de la autenticación en los mensajes, asi no
necesitaremos configurar mas cosas

> vi /etc/qpidd.conf
>
> auth=no

Iniciar servicios y establecer el nivel de ejecución durante el arranque

> service qpidd start
>
> chkconfig qpidd on

Con esto ya tendríamos instalado y configurado Qpid en nuestro entorno,
en la próxima entrada ya empezaremos a configurar lo que de verdad es
Openstack. Estas entradas serán mas largas e interesantes.
