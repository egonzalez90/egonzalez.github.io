---
id: 759
title: 'Fix Bash (ShellShock) en diferentes SO: Debian, RHEL y Solaris'
date: 2014-10-01T17:20:52+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=759
permalink: /fix-bash-shellshock-en-diferentes-so-debian-rhel-y-solaris-shellshock/
image: /wp-content/uploads/2014/05/original-672x372.jpg
categories:
  - Linux
  - OpenStack
  - Various
tags:
  - actualizar
  - bash
  - bug
  - centos
  - Debian
  - fix
  - oracle
  - red hat
  - rhel
  - shellshock
  - solaris
---
Veremos la forma de instalar los parches de Bash en diferentes sistemas Linux<!--more-->
<h1>Debian 6</h1>
Primero deberemos añadir el repositorio LTS. Lo haremos añadiendo esta línea a el archivo siguiente archivo
<blockquote>vi /etc/apt/sources.list/</blockquote>
<blockquote>deb http://ftp.us.debian.org/debian squeeze-lts main non-free contrib</blockquote>
A continuación importaremos la clave del servidor de Debian
<blockquote>gpg --keyserver pgpkeys.mit.edu --recv-key 8B48AD6246925553</blockquote>
La exportaremos y añadiremos para que al actualizar la reconozca, es posible que estos pasos no sean necesarios, pero normalmente suele dar el error de la clave
<blockquote>gpg -a --export 8B48AD6246925553 | apt-key add –</blockquote>
A partir de aquí será lo igual que con Debian 7
<h1>Debian 7</h1>
Actualizaremos la lista de repositorios
<blockquote>apt-get update</blockquote>
Lo siguiente es actualizar solo el paquete bash
<blockquote>apt-get install --only-upgrade bash</blockquote>
<h1>RHEL-CentOS 5, 6 y 7</h1>
Directamente actualizando el paquete bash
<blockquote>yum update bash</blockquote>
O instalándolo desde el paquete .rpm disponible en la página de RHEL, o en los repositorios de CentOS, Scientific Linux, etc
<blockquote>rpm –Uvh paquetebash.rpm</blockquote>
Puedes comprobar que esta la ultima versión instalada viendo la fecha y la versión del paquete mediante
<blockquote>rpm –qi bash</blockquote>
<h1>Oracle Linux 6</h1>
En Oracle Linux primero deberemos añadir los repositorios de paquetes públicos, para ello iremos a la siguiente ruta.
<blockquote>cd /etc/yum.repos.d</blockquote>
A continuación descargaremos el repositorio público dentro de la misma carpeta:
<blockquote> wget http://public-yum.oracle.com/public-yum-ol6.repo</blockquote>
Por ultimo actualizaremos bash a su última versión disponible
<blockquote>yum update bash</blockquote>