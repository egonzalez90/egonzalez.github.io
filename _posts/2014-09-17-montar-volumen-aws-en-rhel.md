---
id: 662
title: Montar volumen AWS en RHEL
date: 2014-09-17T17:05:47+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=662
permalink: /montar-volumen-aws-en-rhel/
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
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - Linux
  - OpenStack
tags:
  - amazon
  - añadir
  - AWS
  - cloud
  - computing
  - formatear
  - linux
  - montar
  - red hat
  - rhel
  - services
  - volumen
  - web
  - xvdf
---
Para poder realizar estos pasos es necesario que se haya creado un volumen previamente en EC2 de AWS, nos conectaremos a la maquina por SSH y seguiremos los siguientes pasos<!--more-->

Primero comprobaremos que el volumen que habíamos creado en EC2 le ve el SO, utilizaremos este comando
<blockquote><span class="command" style="color: #000000;">lsblk</span><span style="color: #000000;"> </span></blockquote>
Lo normal es que el primer  volumen que añadas se llame xvdf alojado en /dev/

Ahora lo formatearemos en EXT4
<blockquote>sudo mkfs -t ext4 /dev/xvdf</blockquote>
A continuación crearemos la carpeta en donde montaremos el volumen y después lo montaremos en dicha carpeta
<blockquote>sudo mkdir /mnt/volumen

sudo mount /dev/xvdf /mnt/volumen</blockquote>
Ahora con el comando df -h comprobaremos que el SO ya lo ve montado
<pre></pre>