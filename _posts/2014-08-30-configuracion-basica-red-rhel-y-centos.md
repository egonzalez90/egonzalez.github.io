---
id: 590
title: Configuracion basica red RHEL y centOS
date: 2014-08-30T15:49:25+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=590
permalink: /configuracion-basica-red-rhel-y-centos/
kopa_resolution_total_view:
  - "7"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snap_isAutoPosted:
  - "1"
snapTW:
  - N;
post_views_count:
  - "1"
image: /wp-content/uploads/2014/08/redbasica.png
categories:
  - Linux
tags:
  - basica
  - centos
  - configuracion
  - eth0
  - interfaces
  - internet
  - linux
  - network
  - network-scripts
  - red
  - red hat
  - rhel
  - sysconfig
---
En esta entrada aprenderás la configuración de red básica de un servidor Red Hat Enterprise Linux o un CentOS, ambos versiones 6<!--more-->

Primero editaremos este archivo de configuración
<blockquote>vi /etc/sysconfig/network</blockquote>
Este archivo lo rellenaremos de la siguiente forma
<blockquote>NETWORKING=yes

HOSTNAME=nombreservidor #nombredns

GATEWAY=192.168.1.1 #IP puerta de enlace</blockquote>
Una vez acabemos guardaremos y editaremos el archivo de configuración de las interfaces de red, cambiando el nombre según la interfaz que sea
<blockquote>vi /etc/sysconfig/network-scripts/ifcfg-eth0</blockquote>
Este es un ejemplo de configuración de una IP estática (si tu RHEL es anterior a la versión 6 deberas incluir la linea GATEWAY en este archivo, en vez de en /etc/sysconfig/network)
<blockquote>DEVICE=eth0

BOOTPROTO=none #IP estatica

ONBOOT=yes

IPADDR=192.168.1.40 #IP

NETMASK=255.255.255.0 #Mascara de red</blockquote>
Este es un ejemplo de configuración de red por dhcp
<blockquote>DEVICE=eth0

BOOTPROTO=dhcp

ONBOOT=yes</blockquote>
A continuación configuraremos el archivo del DNS
<blockquote>vi /etc/resolv.conf</blockquote>
Aqui rellenaremos nameserver y la IP o hostname de nuestros servidores DNS
<blockquote>nameserver 8.8.8.8 #IP o hostname servidor DNS

nameserver 4.4.4.4 #IP o hostname servidor DNS2</blockquote>
Ahora estableceremos el hostname a el servidor
<blockquote>hostname nombreservidor</blockquote>
Por ultimo reiniciaremos el servicio de red para que coja los cambios
<blockquote>service network restart</blockquote>
Esta seria una configuración básica de red en un servidor Red Hat Enterprise Linux o CentOS