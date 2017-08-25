---
id: 809
title: Servidor de mensajes Qpid
date: 2014-11-16T17:47:34+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=809
permalink: /servidor-de-mensajes-qpid/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - configuracion
  - guia
  - instalacion
  - openstack
  - qpid
  - servidor de mensaje
---
En nuestro entorno, necesitaremos un servidor de mensajes con el que se comunicaran los diferentes nodos y complementos de Openstack. Openstack soporta algunos servidores de mensajes, nosotros utilizaremos Qpid, siendo fácil su instalación y configuración básica sin autenticacion

Instalar Qpid
<blockquote>yum install qpid-cpp-server</blockquote>
Deshabilitar el uso de la autenticación en los mensajes, asi no necesitaremos configurar mas cosas
<blockquote>vi /etc/qpidd.conf

auth=no</blockquote>
Iniciar servicios y establecer el nivel de ejecución durante el arranque
<blockquote>service qpidd start

chkconfig qpidd on</blockquote>
Con esto ya tendríamos instalado y configurado Qpid en nuestro entorno, en la próxima entrada ya empezaremos a configurar lo que de verdad es Openstack. Estas entradas serán mas largas e interesantes.