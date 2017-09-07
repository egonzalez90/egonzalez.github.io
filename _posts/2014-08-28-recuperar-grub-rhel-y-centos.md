---
id: 584
title: Recuperar GRUB RHEL y CentOS
date: 2014-08-28T15:34:51+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=584
permalink: /recuperar-grub-rhel-y-centos/
kopa_resolution_total_view:
  - "5"
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
categories:
  - Linux
tags:
  - centos
  - grub
  - hd0
  - linux
  - red hat
  - rescue
  - rhel
  - root
  - setup
---
Muchas veces te sueles cargar la configuración del GRUB, o simplemente cuando instalas Windows en otra partición. <!--more-->Para ello lo tendremos que recuperar de la siguiente forma:

1º Insertaremos la ISO en el equipo

2º Cuando salga el prompt de arranque, escribiremos
<blockquote>linux rescue</blockquote>
3º A continuación
<blockquote>grub</blockquote>
4º Ahora pondremos este comando, donde hd0,0 es el disco donde esta el grub
<blockquote>root (hd0,0)</blockquote>
5º Lo configuraremos
<blockquote>setup (hd0)</blockquote>
6º Ya terminamos
<blockquote>quit

ctrl-d</blockquote>