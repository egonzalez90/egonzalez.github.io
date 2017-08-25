---
id: 263
title: Crear Raid 1 en Linux
date: 2014-02-14T00:34:24+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=263
permalink: /crear-raid-1-en-linux/
nxs_snap_sh_FB0_1392338069:
  - 'a:32:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";i:0;s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:52:"Re-subido (%TITLE%) has been published on %SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:18:"fbAppPageAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:13:"fbAppAuthUser";s:10:"1161837279";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:8:"urlToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1392338069;}'
snap_isAutoPosted:
  - "1"
nxs_snap_sh_TW0_1392338074:
  - 'a:36:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:29:"https://twitter.com/zombies3c";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";s:1:"0";s:7:"rpstHrs";s:1:"0";s:8:"rpstMins";s:1:"0";s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:25:"Re-subido %TITLE% - %URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1392338074;}'
ac_featured_article:
  - ""
ac_show_post_thumbnail:
  - ""
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
dsq_thread_id:
  - "6094297017"
image: /wp-content/uploads/2014/02/2.jpg
categories:
  - Linux
tags:
  - configuracion
  - Debian
  - disco duro
  - linux
  - mdadm
  - raid
---
&nbsp;

<strong>En esta entrada, voy a mostrar como se crea un raid de nivel 1 bajo Linux, también simulare como cambiar un disco en caso de que uno falle.<!--more--></strong>

<strong> Empecemos:</strong>

<b>Cuando iniciamos la consola de Linux, comprobaremos que discos duros tenemos disponibles, en esta pantalla vemos que están sda, sdb</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/1.jpg"><img class="aligncenter size-full wp-image-264" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/1.jpg" alt="1" width="628" height="353" /></a>

<b>En esta otra esta sdc, vemos que tanto sdb como sdc están sin formato alguno</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/2.jpg"><img class="aligncenter size-full wp-image-265" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/2.jpg" alt="2" width="502" height="143" /></a>

<b>Ahora instalaremos el paquete mdadm, que será el que nos permita configurar un raid en el sistema </b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/3.jpg"><img class="aligncenter size-full wp-image-266" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/3.jpg" alt="3" width="469" height="24" /></a>

<b>Ahora crearemos un nuevo dispositivo llamado md0, con un raid de nivel 1, añadiendo los dispositivos sdb y sdc a este</b>

&nbsp;

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/4.jpg"><img class="aligncenter size-full wp-image-267" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/4.jpg" alt="4" width="643" height="37" /></a>

<b>Ahora configuraremos este dispositivo que hemos creado previamente</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/5.jpg"><img class="aligncenter size-full wp-image-268" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/5.jpg" alt="5" width="428" height="22" /></a>

<b>Utilizaremos la opción N para crear una nueva partición</b>

<b>Seleccionaremos P para hacerla primaria</b>

<b>Estableceremos que la partición es la numero 1</b>

<b>Pondremos el cilindro número 1 como primero, y el último de los que tengamos disponibles como final</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/6.jpg"><img class="aligncenter size-full wp-image-269" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/6.jpg" alt="6" width="635" height="184" /></a>

<b>Después utilizaremos la opción W para escribir los cambios al disco</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/7.jpg"><img class="aligncenter size-full wp-image-270" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/7.jpg" alt="7" width="391" height="91" /></a>

<b>Ahora crearemos el sistema de fichero mediante el comando mkfs y el dispositivo que habíamos creado</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/8.jpg"><img class="aligncenter size-full wp-image-271" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/8.jpg" alt="8" width="555" height="338" /></a>

<b>Ahora crearemos una carpeta de montaje de nuestro dispositivo mediante mkdir</b>

<b>Después montaremos el dispositivo a dicha carpeta mediante el comando mount</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/9.jpg"><img class="aligncenter size-full wp-image-272" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/9.jpg" alt="9" width="536" height="38" /></a>

<b>Ahora crearemos un fichero de un tamaño determinado que se especifica en la opción bs </b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/10.jpg"><img class="aligncenter size-full wp-image-273" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/10.jpg" alt="10" width="594" height="87" /></a>

<b>Ahora comprobamos esta carpeta, y vemos que los tamaños están bien configurados</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/11.jpg"><img class="aligncenter size-full wp-image-274" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/11.jpg" alt="11" width="460" height="83" /></a>

<b>Ahora comprobaremos en este archivo que el raid está activo, y tiene los dispositivos sdb y sdc</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/12.jpg"><img class="aligncenter size-full wp-image-275" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/12.jpg" alt="12" width="437" height="104" /></a>

<b>Ahora haremos como que el disco sdb ha fallado, para poder quitarle del raid para remplazarle primero hay que marcarle como disco fallido mediante este comando</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/13.jpg"><img class="aligncenter size-full wp-image-276" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/13.jpg" alt="13" width="563" height="37" /></a>

<b>Ahora le quitaremos del raid el disco sdb</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/14.jpg"><img class="aligncenter size-full wp-image-277" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/14.jpg" alt="14" width="560" height="37" /></a>

<b>Iremos al archivo del raid y comprobamos que no está el disco sdb dentro de el</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/15.jpg"><img class="aligncenter size-full wp-image-278" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/15.jpg" alt="15" width="459" height="102" /></a>

<b>Ahora borraremos los datos de configuración anterior del disco sdb mediante el primer comando.</b>

<b>Después añadimos el disco sdb al disco raid, esto si tiene datos tardara un tiempo en sincronizar</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/16.jpg"><img class="aligncenter size-full wp-image-279" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/16.jpg" alt="16" width="573" height="52" /></a>

<b>Ahora desactivaremos el raid mediante este comando</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/17.jpg"><img class="aligncenter size-full wp-image-280" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/17.jpg" alt="17" width="484" height="19" /></a>

<b>Si queremos volver a activarle, lo haremos mediante este otro comando</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/18.jpg"><img class="aligncenter size-full wp-image-281" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/18.jpg" alt="18" width="490" height="24" /></a>