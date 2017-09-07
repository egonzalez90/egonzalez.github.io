---
id: 684
title: ELB en AWS (Elastic Load Balancers)
date: 2014-09-25T16:43:42+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=684
permalink: /elb-en-aws-elastic-load-balancers/
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
  - automatizar
  - AWS
  - Balancers
  - cloud
  - crear
  - distribuir
  - ELB
  - http
  - instancias
  - Load
  - Services; Elastic
  - trafico
  - virtualizacion
  - web
---
Hoy mostraré como crear Elastic Load Balancer (ELB) en Amazon Web Services el cual nos permitirá distribuir automáticamente el trafico entre las aplicaciones de las distintas instancias y obtener una mejor tolerancia a fallos.<!--more-->

Primero nos logearemos en AWS e iremos a la pestaña EC2, una vez a, aquí pulsaremos sobre Load Balancers del menú izquierdo.

Se nos abrirá esta ventana en la que pulsaremos Create Load Balancer para configurar un ELB nuevo. En esta misa ventana nos mostraría los ELB ya creados

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/011.png"><img class="aligncenter size-full wp-image-685" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/011.png" alt="01" width="1277" height="600" /></a>

Una vez abierto Create Load Balancer, rellenaremos el Nombre del ELB a crear y estableceremos los protocolos que soportara el ELB, por defecto viene activado HTTP por el puerto 80

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/021.png"><img class="aligncenter size-full wp-image-686" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/021.png" alt="02" width="951" height="520" /></a>

En esta próxima pantalla configuraremos los análisis de salud de nuestras instancias, para ello ajustaremos los parámetros inferiores a nuestro gusto

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/031.png"><img class="aligncenter size-full wp-image-687" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/031.png" alt="03" width="947" height="588" /></a>

Aquí asignaremos o crearemos un Security Group, en mi caso utilizare uno ya existente

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/041.png"><img class="aligncenter size-full wp-image-688" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/041.png" alt="04" width="1001" height="384" /></a>

Lo ultimo que configuraremos serán las instancias que harán uso del ELB, seleccionamos las que queramos y pulsaremos en Continue

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/051.png"><img class="aligncenter size-full wp-image-689" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/051.png" alt="05" width="963" height="653" /></a>

Finalizaremos estableciendo una etiqueta a nuestro ELB

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/061.png"><img class="aligncenter size-full wp-image-690" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/061.png" alt="06" width="941" height="394" /></a>

Antes de terminar de crear el ELB, nos mostrara una resumen de la configuración, si estuviéramos de acuerdo pulsaríamos en Create, de lo contrario modificaremos alguna de las partes anteriores

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/071.png"><img class="aligncenter size-full wp-image-691" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/071.png" alt="07" width="939" height="727" /></a>

Esta seria una imagen del ELB creado, tendremos que esperar un rato hasta que este activo, una vez activo veremos In Service el Status de las Instancias, aunque en algunas ocasiones aunque este In Service aun no tenemos conexión a través del ELB

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/081.png"><img class="aligncenter size-full wp-image-692" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/081.png" alt="08" width="1053" height="771" /></a>

Un saludo