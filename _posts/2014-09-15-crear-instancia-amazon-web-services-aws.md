---
id: 635
title: Crear instancia Amazon Web Services (AWS)
date: 2014-09-15T16:10:06+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=635
permalink: /crear-instancia-amazon-web-services-aws/
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
  - computing
  - creacion
  - crear
  - ec2
  - instancia
  - linux
  - pem
  - ppk
  - primera
  - putty
  - services
  - web
---
Buenos días, en esta entrada mostrare como crear una instancia en la plataforma cloud de Amazon Web Services.

<!--more--> Para poder crear las instancias, deberemos tener cuenta de AWS y nos logearemos en la consola.

Lo primero que nos encontraremos sera el dashboard principal, aqui podremos administrar las diferentes secciones de AWS. Nosotros iremos a EC2

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png"><img class="aligncenter size-full wp-image-636" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png" alt="01" width="574" height="369" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png"> </a>Una vez entrado en EC2, nos encontraremos con esta ventana que nos mostrara un resumen de lo que tenemos en nuestro EC2.

A nosotros nos interesa crear una instancia nueva, por lo que pulsaremos sobre Launch Instance

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png"><img class="aligncenter size-full wp-image-637" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png" alt="02" width="767" height="379" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png"> </a>La siguiente pantalla nos mostrara varias instancias disponibles para crear, en nuestro plan free disponemos de alguna, nosotros seleccionaremos Amazon Linux AMI

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png"><img class="aligncenter size-full wp-image-638" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png" alt="03" width="1001" height="473" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png"> </a>Al utilizar el plan free solo podremos usar el tipo t2.micro, por lo que lo dejaremos por defecto y daremos a Configure Instance Details

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png"><img class="aligncenter size-full wp-image-639" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png" alt="04" width="1280" height="670" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png"> </a>En esta pantalla también la dejaremos por defecto, se puede seleccionar alguna opción si se quisiera como por ejemplo Monitoring, nosotros iremos directamente a Add Storage

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png"><img class="aligncenter size-full wp-image-640" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png" alt="05" width="1283" height="773" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png"> </a>En esta otra pantalla lo mismo, lo dejaremos por defecto y pasaremos a Tag Instance

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png"><img class="aligncenter size-full wp-image-641" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png" alt="06" width="1218" height="240" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png">
</a><a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/07.png"><img class="aligncenter size-full wp-image-642" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/07.png" alt="07" width="1261" height="84" /></a>

Aquí si que rellenaremos el Valor con el nombre de la instancia, en este ejemplo instancename, a continuación iremos a Configure Security Group

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/08.png"><img class="aligncenter size-full wp-image-643" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/08.png" alt="08" width="1260" height="200" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png"><img class="aligncenter size-full wp-image-644" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png" alt="09" width="1255" height="80" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png"> </a>Aquí pondremos un nombre para el Grupo de Seguridad y una descripción, como vemos, tenemos creada una regla por defecto que permite el acceso por SSH desde cualquier IP, eso no es muy recomendable, pero al ser una Instancia de pruebas lo dejaremos por defecto

&nbsp;

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png"><img class="aligncenter size-full wp-image-645" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png" alt="10" width="1311" height="415" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png"> </a> <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png"><img class="aligncenter size-full wp-image-646" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png" alt="11" width="1261" height="97" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png"> </a>Ya son pocos los pasos para acabar de crear la instancia, aqui tenemos un resumen de la configuración que hemos realizado, pulsaremos en Launch Instance para pasar al siguiente paso

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png"><img class="aligncenter size-full wp-image-647" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png" alt="12" width="1281" height="771" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png"> </a>Por ultimo crearemos una clave .pem para que podamos acceder a la instancia, para ello marcaremos Create a new key pair y pondremos un nombre para esa clave. Después pulsaremos en Download Key Pair, de esta forma se nos descargara la clave a nuestro equipo y se habilitara la opción de Launch Instances

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png"><img class="aligncenter size-full wp-image-648" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png" alt="13" width="703" height="521" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png"> </a>

Ahora mismo ya se esta creando nuestra instancia, podremos ver el progreso pulsando sobre View Instances

&nbsp;

&nbsp;

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png"><img class="aligncenter size-full wp-image-649" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png" alt="14" width="1268" height="187" /></a>

&nbsp;

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png"> </a>Esta es la ventana en donde podemos ver las instancias, la primera es una que esta en uso y completa, la segunda es la que acabamos de crear, cuando Status Checks este en verde ya la tendremos completamente creada

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png"><img class="aligncenter size-full wp-image-650" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png" alt="15" width="1056" height="204" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png"> </a>Lo ultimo que nos queda es conectarnos por SSH a la instancia creada, para ello copiaremos el Public DNS, que es la dirección a la que nos podremos conectar

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png"><img class="aligncenter size-full wp-image-651" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png" alt="16" width="1031" height="490" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png"> </a>En mi caso me conecto con PuTTy, para ello debes de convertir el formato de la clave .pem a .ppk, para ello tienes una entrada en este mismo blog de como hacerlo: <a title="Convertir claves .pem a .ppk" href="http://egonzalez.org/?p=630" target="_blank">http://egonzalez.org/?p=630</a>

Una vez abierto PuTTy utilizaremos la siguiente direccion: ec2-user@DNSPUBLICO

El usuario ec2-user es creado automaticamente

DNSPUBLICO es la direccion que habiamos copiado previamente

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png"><img class="aligncenter size-full wp-image-652" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png" alt="17" width="470" height="444" /></a>

&nbsp;

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png"> </a>Por ultimo iremos a SSH/Auth y buscaremos la clave privada de nuestra instancia

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png"><img class="aligncenter size-full wp-image-653" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png" alt="18" width="464" height="444" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png"> </a>Despues de aceptar la clave nos veremos logeados en la instancia, con esto ya estaria finalizada la instalacion y comprobacion de nuestra primera instancia en AWS.

Es recomendable realizazar una actualizacion del sistema nada mas arrancar con el comando
<blockquote>sudo yum update

&nbsp;</blockquote>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/19.png"><img class="aligncenter size-full wp-image-654" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/19.png" alt="19" width="673" height="416" /></a>

Espero ser de ayuda y muchas gracias por leer este blog, un saludo