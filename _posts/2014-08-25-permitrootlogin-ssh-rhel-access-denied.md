---
id: 556
title: PermitRootLogin ssh RHEL (Access Denied)
date: 2014-08-25T11:55:37+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=556
permalink: /permitrootlogin-ssh-rhel-access-denied/
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
kopa_resolution_total_view:
  - "2"
post_views_count:
  - "0"
image: /wp-content/uploads/2014/08/IMG_811278467062542.jpeg
categories:
  - Linux
tags:
  - access
  - denied
  - enable root
  - linux
  - permitrootlogin
  - rhel
  - root
  - servicio
  - ssh
  - sshd
---
En algunos sistemas, el acceso por ssh al usuario root esta deshabilitado por defecto, cuando intentemos logearnos nos mostrara el error Access Denied, para habilitarlo deberemos modificar este archivo
<blockquote>/etc/ssh/sshd/sshd_config</blockquote>
Aquí buscaremos una linea en la que aparezca:
<blockquote>PermitRootLogin no</blockquote>
Lo cambiaremos por:
<blockquote>PermitRootLogin yes</blockquote>
Guardaremos y reiniciamos el servicio sshd
<blockquote>service sshd restart</blockquote>
Ya podriamos acceder con el usuario root por ssh