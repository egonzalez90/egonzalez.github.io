---
id: 674
title: Crear Plantilla AMI en AWS
date: 2014-09-22T09:14:24+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=674
permalink: /crear-plantilla-ami-en-aws/
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - OpenStack
tags:
  - amazon
  - AMI
  - AWS
  - cloud
  - computing
  - crear
  - ejecutar
  - hybrid
  - imagen
  - instancia
  - launch
  - plantilla
  - private
  - public
  - services
  - web
---
El primer paso es estar logeado en AWS, y en la pestaña Instances de EC2.<!--more-->

Una vez aquí pulsaremos con el botón derecho sobre la instancia que queremos convertir en plantilla AMI.

Aquí pulsaremos sobre Create Image<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura.png"><img class="aligncenter size-full wp-image-675" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura.png" alt="Captura" width="884" height="414" />
</a>

Lo siguiente sera ponerle un nombre a la plantilla y una descripcion, para finalizar le daremos a Create Image

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura2.png"><img class="aligncenter size-full wp-image-676" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura2.png" alt="Captura2" width="1005" height="535" /></a>

A continuación nos mostrara un mensage que indica que esta en proceso de creacion, pulsaremos sobre View Pending Image **** para ver el estado de la peticion

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura3.png"><img class="aligncenter size-full wp-image-677" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura3.png" alt="Captura3" width="965" height="141" /> </a>En esta ventana veremos el estado de la peticion, una vez acabada la creacion de la plantilla aparecera en verde Available, estos sencillos pasos nos permitiran tener imagenes personalizadas para ejecutar tantas instancias como queramos sobre esa plantilla

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura4.png"><img class="aligncenter size-full wp-image-678" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura4.png" alt="Captura4" width="1057" height="210" /></a> Para ejecutar la imagen como una instancia, solo tienes que pulsar sobre Launch y crear la instancia como cualquier otra.

Si quieres saber como se crea una instancia puedes hacerlo siguiendo esta entrada del blog: <a title="Crear instancia Amazon Web Services (AWS)" href="http://egonzalez.org/?p=635" target="_blank">http://egonzalez.org/?p=635</a>