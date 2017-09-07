---
id: 204
title: Solución fallo VirtualBox en Fedora 19
date: 2013-11-13T18:00:14+00:00
author: Editor
layout: post
guid: http://openmindinside.wordpress.com/?p=204
permalink: /solucion-fallo-virtualbox-en-fedora-19/
publicize_facebook_url:
  - https://facebook.com/10201630879271416
  - https://facebook.com/10201630879271416
  - https://facebook.com/10201630879271416
  - https://facebook.com/10201630879271416
publicize_twitter_user:
  - suicidezombiie
  - suicidezombiie
  - suicidezombiie
  - suicidezombiie
publicize_twitter_url:
  - http://t.co/FSbdnIaLv0
  - http://t.co/FSbdnIaLv0
  - http://t.co/FSbdnIaLv0
  - http://t.co/FSbdnIaLv0
publicize_tumblr_url:
  - http://suicidezombiie.tumblr.com.tumblr.com/post/66884427381
  - http://suicidezombiie.tumblr.com.tumblr.com/post/66884427381
  - http://suicidezombiie.tumblr.com.tumblr.com/post/66884427381
  - http://suicidezombiie.tumblr.com.tumblr.com/post/66884427381
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
categories:
  - Linux
tags:
  - error
  - fedora 19
  - linux
  - maquina virtual
  - solucion
  - Virtualbox
  - virtualizacion
  - VM
---
Mucha gente ha tenido problemas a la hora de abrir una maquina virtual en VirtualBox con Fedora 19, suele salir un error de compilación de VBox que por mucho que lo recompiles no se soluciona si no sigues los pasos previos que voy a explicar.
<!--more-->
En primer lugar deberías de desinstalar VirtualBox completamente, doy por hecho de que si lo has instalado también sabrás desinstalarlo.
A continuación deberías de actualizar los paquetes del sistema, esto no es necesario, pero siempre recomendable por motivos de seguridad.Se hace mediante este comando:
<pre># yum -y upate</pre>
<address> </address>Después instalamos datos del kernel
<pre># yum -y install kernel-headers kernel-devel dkms gcc</pre>
<address> </address>Ahora vamos a la carpeta de repositorios de fedora
<pre># cd /etc/yum.repos.d</pre>
<address> </address>Ahora creamos/modificamos este archivo
<pre># vi virtualbox.repo</pre>
<address> </address>Se rellena con la siguiente información:
<pre>               [virtualbox]
name=Fedora$releasever - $basearch - VirtualBox
baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/$releasever/$basearch
enabled=1
gpgcheck=1
gpgkey=http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc</pre>
Guardamos y salimos de este archivo

Ahora instalamos VirtualBox
<pre># yum -y install VirtualBox-4.2</pre>
<address> </address>Ahora ejecutamos este comando para configurar VirtualBox
<pre># /etc/init.d/vboxdrv setup</pre>
<address> </address>Ahora añadimos nuestro usuario al grupo que tiene permisos para usar VirtualBox
<pre># usermod -G vboxusers -a "NombredeUsuario"</pre>
Esto debería permitirnos crear maquinas virtuales y abrirlas ya

<address> </address>