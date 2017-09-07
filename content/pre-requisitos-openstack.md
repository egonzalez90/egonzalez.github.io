Title: Pre-requisitos Openstack
Date: 2014-10-26 16:43
Author: egongu90
Category: OpenStack
Tags: basico, cloud, firewalld, instalacion, iptables, network, network manager, ntp, openstack, prerequisitos, server
Slug: pre-requisitos-openstack
Status: published

NTP
---

Deberemos tener instalado NTP en todos los nodos.

> yum install ntp

<!--more-->

A continuacion tenemos que configurar los nodos para que usen NTP del
nodo controller

> vi /etc/ntp.conf

Editamos la linea server para que aparezca lo siguiente

> server controller iburst

En el nodo controller borramos las opciones nopeer y noquery de las
lineas restrict

Por ultimo iniciaremos el servicio y el nivel de ejecución en el
arranque del sistema

> service ntpd start
>
> chkconfig ntpd on

Servicios de red
----------------

Deshabilitamos NetworkManager y habilitamos el servicio network, asi
como quitamos y establecemos el nivel de ejecución a cada servicio
respectivamente

> service NetworkManager stop
>
> service network start
>
> chkconfig NetworkManager off
>
> chkconfig network on

Servicios cortafuegos
---------------------

Paramos y deshabilitamos firewalld por defecto y activamos e iniciamos
iptables. Es posible que no tengas instalado firewalld, por lo que no
tendrás que deshabilitarlo

> service firewalld stop
>
> service iptables start
>
> chkconfig firewalld off
>
> chkconfig iptables on

Estos son los prerequisitos necesarios para iniciar la instalación de un
entorno con Openstack

Un saludo
