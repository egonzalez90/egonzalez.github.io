---
id: 630
title: Convertir claves .pem a .ppk PuTTy AWS
date: 2014-09-13T15:40:54+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=630
permalink: /convertir-claves-pem-a-ppk-putty-aws/
kopa_resolution_total_view:
  - "1"
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
  - OpenStack
tags:
  - amazon
  - AWS
  - cloud
  - convertir
  - extension
  - formato
  - pem
  - ppk
  - private key
  - putty
  - puttygen
  - services
  - web
---
Para poder conectarse a Amazon Web Services desde PuTTy, es necesario que la clave .pem que nos proporciona AWS esté en formato .ppk que es el que reconoce PuTTy. Para convertir las .pem a .ppk seguiremos los siguientes pasos: <!--more-->

Debes tener instalado Putty en el equipo con la tool PuTTygen

Una vez abierta la tool PuTTygen, pulsaremos en LOAD

Nos abrirá el explorador de archivos y marcaremos todos los archivos, ya que PuTTY solo mostrara las claves .ppk

Seleccionaremos nuestra clave .pem

Por ultimo daremos a Save Private Key, nos preguntara si la queremos guardar sin contraseña y pulsaremos YES.

Pondremos el mismo nombre que la clave .pem, PuTTY pondrá la extensión .ppk

Ya estaría la clave creada en formato .ppk para poder conectarnos a AWS a través de PuTTy