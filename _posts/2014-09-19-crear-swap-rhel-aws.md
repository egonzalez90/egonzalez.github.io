---
id: 665
title: Crear Swap AWS en RHEL
date: 2014-09-19T16:28:40+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=665
permalink: /crear-swap-rhel-aws/
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapTW:
  - N;
snapFB:
  - N;
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - Linux
  - OpenStack
tags:
  - /etc/fstab
  - amazon
  - AWS
  - cloud
  - mkswap
  - red hat
  - rhel
  - services
  - swap
  - swapon
  - web
---
Cuando creas una instancia, esta se hace sin swap, el cual es necesario para el uso de determinadas aplicaciones.<!--more-->

Para ello deberemos tener espacio en disco, si no tuvieras suficiente puedes seguir esta entrada pare ver como se hace: <a title="Montar volumen AWS en RHEL" href="http://egonzalez.org/?p=662" target="_blank">http://egonzalez.org/?p=635</a>

A continuación iremos a la consola y ejecutaremos los siguientes comandos:
<blockquote>sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024

sudo /sbin/mkswap /var/swap.1

sudo /sbin/swapon /var/swap.1</blockquote>
Con ello crearemos el archivo swap y lo montaremos.
Con este comando se crea de un tamaño de 1024 MB, si se quisiera mas, abría que cambiar el valor count a el deseado.

Por ultimo abría que añadir esta linea al archivo /etc/fstab , esto permitirá que se monte durante el arranque automáticamente.
<blockquote>/var/swap.1 swap swap defaults 0 0</blockquote>
Espero ser de ayuda, un saludo