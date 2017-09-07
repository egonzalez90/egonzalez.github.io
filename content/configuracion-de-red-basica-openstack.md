Title: Configuracion de red basica Openstack
Date: 2014-10-19 16:46
Author: egongu90
Category: OpenStack
Tags: 3 nodos, basica, centos, compute, controller, eth0, network, openstack, red, redhat, rhel
Slug: configuracion-de-red-basica-openstack
Status: published

En la siguiente entrada tienes como configurar las tarjetas de red para
realizar esta instalación de Openstack: [Configuración básica de red
RHEL](http://egonzalez.org/configuracion-basica-red-rhel-y-centos/ "Configuracion basica red RHEL y centOS")

Aquí mostrare el esquema conceptual de como ira configurada cada tarjeta
de los distintos nodos.<!--more-->

 CONTROLLER
===========

> hostname controller

### eth0:

-   IP 192.168.1.11
-   GATEWAY 192.168.1.1

NETWORK
=======

> hostname network

### eth0

-   IP 192.168.1.21
-   GATEWAY 192.168.1.1

### eth1

-   IP 10.0.1.21

### External network (eth2)

-   En el archivo de configuración dejaremos BOOTPROTO=none, sin
    configurar IP ni Netmask

COMPUTE
=======

> hostname compute1

### eth0

-   IP 192.168.1.31
-   GATEWAY 192.168.1.1

### eth1

-   IP 10.0.1.31

\*Los siguientes nodos de cómputo se pueden utilizar las siguientes IP

 

En todos los nodos, se ha de configurar el archivo host de la siguiente
manera

> vi /etc/hosts

> 192.168.1.11      controller
>
> 192.168.1.21      network
>
> 192.168.1.31      compute1
