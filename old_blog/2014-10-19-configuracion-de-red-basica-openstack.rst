--- layout: post title: Configuracion de red basica Openstack date:
2014-10-19 16:46:16.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - 3 nodos - basica - centos - compute - controller - eth0 -
network - openstack - red - redhat - rhel meta: \_edit_last: '2'
\_publicize_facebook_user: https://www.facebook.com/dudu.gonzalez90
\_publicize_twitter_user: "@hidanstillalive" \_thumbnail_id: '615'
\_wpas_mess: Configuracion de red basica Openstack
http://wp.me/p55Jx1-cK \_wpas_done_all: '1' \_wpas_skip_5226565: '1'
\_wpas_skip_4949654: '1' \_wpas_skip_8706018: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567496511;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:590;}i:1;a:1:{s:2:"id";i:788;}i:2;a:1:{s:2:"id";i:802;}}}}
dsq_thread_id: '6115511029' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/configuracion-de-red-basica-openstack/" ---

En la siguiente entrada tienes como configurar las tarjetas de red para
realizar esta instalación de Openstack: `Configuración básica de red
RHEL <http://egonzalez.org/configuracion-basica-red-rhel-y-centos/>`__

Aquí mostrare el esquema conceptual de como ira configurada cada tarjeta
de los distintos nodos.

 CONTROLLER
===========

   hostname controller

eth0:
-----

-  IP 192.168.1.11
-  GATEWAY 192.168.1.1

NETWORK
=======

   hostname network

.. _eth0-1:

eth0
----

-  IP 192.168.1.21
-  GATEWAY 192.168.1.1

eth1
----

-  IP 10.0.1.21

External network (eth2)
-----------------------

-  En el archivo de configuración dejaremos BOOTPROTO=none, sin
   configurar IP ni Netmask

COMPUTE
=======

   hostname compute1

.. _eth0-2:

eth0
----

-  IP 192.168.1.31
-  GATEWAY 192.168.1.1

.. _eth1-1:

eth1
----

-  IP 10.0.1.31

\*Los siguientes nodos de cómputo se pueden utilizar las siguientes IP

 

En todos los nodos, se ha de configurar el archivo host de la siguiente
manera

   vi /etc/hosts

..

   192.168.1.11      controller

   192.168.1.21      network

   192.168.1.31      compute1
