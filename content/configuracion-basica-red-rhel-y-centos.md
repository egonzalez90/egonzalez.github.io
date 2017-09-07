Title: Configuracion basica red RHEL y centOS
Date: 2014-08-30 15:49
Author: egongu90
Category: Linux
Tags: basica, centos, configuracion, eth0, interfaces, internet, linux, network, network-scripts, red, red hat, rhel, sysconfig
Slug: configuracion-basica-red-rhel-y-centos
Status: published

En esta entrada aprenderás la configuración de red básica de un servidor
Red Hat Enterprise Linux o un CentOS, ambos versiones 6<!--more-->

Primero editaremos este archivo de configuración

> vi /etc/sysconfig/network

Este archivo lo rellenaremos de la siguiente forma

> NETWORKING=yes
>
> HOSTNAME=nombreservidor \#nombredns
>
> GATEWAY=192.168.1.1 \#IP puerta de enlace

Una vez acabemos guardaremos y editaremos el archivo de configuración de
las interfaces de red, cambiando el nombre según la interfaz que sea

> vi /etc/sysconfig/network-scripts/ifcfg-eth0

Este es un ejemplo de configuración de una IP estática (si tu RHEL es
anterior a la versión 6 deberas incluir la linea GATEWAY en este
archivo, en vez de en /etc/sysconfig/network)

> DEVICE=eth0
>
> BOOTPROTO=none \#IP estatica
>
> ONBOOT=yes
>
> IPADDR=192.168.1.40 \#IP
>
> NETMASK=255.255.255.0 \#Mascara de red

Este es un ejemplo de configuración de red por dhcp

> DEVICE=eth0
>
> BOOTPROTO=dhcp
>
> ONBOOT=yes

A continuación configuraremos el archivo del DNS

> vi /etc/resolv.conf

Aqui rellenaremos nameserver y la IP o hostname de nuestros servidores
DNS

> nameserver 8.8.8.8 \#IP o hostname servidor DNS
>
> nameserver 4.4.4.4 \#IP o hostname servidor DNS2

Ahora estableceremos el hostname a el servidor

> hostname nombreservidor

Por ultimo reiniciaremos el servicio de red para que coja los cambios

> service network restart

Esta seria una configuración básica de red en un servidor Red Hat
Enterprise Linux o CentOS
