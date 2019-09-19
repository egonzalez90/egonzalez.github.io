--- layout: post title: Configuracion basica red RHEL y centOS date:
2014-08-30 15:49:25.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Linux tags: -
basica - centos - configuracion - eth0 - interfaces - internet - linux -
network - network-scripts - red - red hat - rhel - sysconfig meta:
\_edit_last: '2' \_login_radius_meta: a:1:{s:7:"sharing";i:0;}
kopa_resolution_total_view: '7' \_thumbnail_id: '595' snap_MYURL: ''
snapEdIT: '1' snapFB: N; snap_isAutoPosted: '1' snapTW: N;
post_views_count: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568471978;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:790;}i:1;a:1:{s:2:"id";i:541;}i:2;a:1:{s:2:"id";i:481;}}}}
dsq_thread_id: '6102990367' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/configuracion-basica-red-rhel-y-centos/" ---

En esta entrada aprenderás la configuración de red básica de un servidor
Red Hat Enterprise Linux o un CentOS, ambos versiones 6

Primero editaremos este archivo de configuración

   vi /etc/sysconfig/network

Este archivo lo rellenaremos de la siguiente forma

   NETWORKING=yes

   HOSTNAME=nombreservidor #nombredns

   GATEWAY=192.168.1.1 #IP puerta de enlace

Una vez acabemos guardaremos y editaremos el archivo de configuración de
las interfaces de red, cambiando el nombre según la interfaz que sea

   vi /etc/sysconfig/network-scripts/ifcfg-eth0

Este es un ejemplo de configuración de una IP estática (si tu RHEL es
anterior a la versión 6 deberas incluir la linea GATEWAY en este
archivo, en vez de en /etc/sysconfig/network)

   DEVICE=eth0

   BOOTPROTO=none #IP estatica

   ONBOOT=yes

   IPADDR=192.168.1.40 #IP

   NETMASK=255.255.255.0 #Mascara de red

Este es un ejemplo de configuración de red por dhcp

   DEVICE=eth0

   BOOTPROTO=dhcp

   ONBOOT=yes

A continuación configuraremos el archivo del DNS

   vi /etc/resolv.conf

Aqui rellenaremos nameserver y la IP o hostname de nuestros servidores
DNS

   nameserver 8.8.8.8 #IP o hostname servidor DNS

   nameserver 4.4.4.4 #IP o hostname servidor DNS2

Ahora estableceremos el hostname a el servidor

   hostname nombreservidor

Por ultimo reiniciaremos el servicio de red para que coja los cambios

   service network restart

Esta seria una configuración básica de red en un servidor Red Hat
Enterprise Linux o CentOS
