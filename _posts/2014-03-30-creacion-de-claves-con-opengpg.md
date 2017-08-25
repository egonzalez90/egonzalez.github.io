---
id: 393
title: Creación de claves con OpenPGP
date: 2014-03-30T15:21:07+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=393
permalink: /creacion-de-claves-con-opengpg/
nxs_snap_sh_FB0_1396189273:
  - 'a:32:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";i:0;s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:42:"(%TITLE%) has been published on %SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:18:"fbAppPageAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:13:"fbAppAuthUser";s:10:"1161837279";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:8:"urlToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1396189273;}'
snap_isAutoPosted:
  - "1"
nxs_snap_sh_TW0_1396189278:
  - 'a:36:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:29:"https://twitter.com/zombies3c";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";s:1:"0";s:7:"rpstHrs";s:1:"0";s:8:"rpstMins";s:1:"0";s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:15:"%TITLE% - %URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1396189278;}'
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
image: /wp-content/uploads/2014/03/131.png
categories:
  - Linux
tags:
  - asimetrico
  - cifrado
  - clave
  - linux
  - opengpg
  - openpgp
  - Seguridad
  - simetrico
---
<strong>En esta entrada mostrare el proceso para la creación de claves simétricas y asimétricas con openpgp en Linux</strong>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png"><!--more--></a>
<p style="text-align: center;"><span style="color: #ff0000;"><em><strong>Clave Simétrica </strong></em></span></p>
<b>En Linux por defecto te viene instalado openpgp.</b>

&nbsp;

<b>Para crear una clave simétrica, deberemos escribir gpg con el modificador –c y el nombre del archivo creado que se quiera encriptar</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png"><img class="aligncenter size-full wp-image-394" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png" alt="1" width="477" height="24" /></a>

&nbsp;

<b>Esto nos solicitara la clave que queramos asignarla dos veces, la rellenamos y ya tenemos el archivo encriptado de forma simétrica.</b>

<b>Para desencriptar usaremos el comando gpg con el modificado –d y el archivo que queramos desencriptar, que tiene que acabar en .gpg</b>

<b>Esto nos solicitara la clave que le habíamos puesto, y a continuación nos creara el archivo desencriptado</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/2.png"><img class="aligncenter size-full wp-image-395" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/2.png" alt="2" width="523" height="80" /></a>
<p style="text-align: center;"><strong><span style="color: #ff0000;">Clave asimétrica </span></strong></p>
<strong>Para crear la clave asimétrica, pondremos el comando gpg –gen-key</strong>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/3.png"><img class="aligncenter size-full wp-image-396" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/3.png" alt="3" width="403" height="21" /></a>

<b>Esto nos solicitara que le indiquemos el algoritmo de cifrado que deseemos utilizar, nosotros usaremos la opción 1 default RSA</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/4.png"><img class="aligncenter size-full wp-image-397" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/4.png" alt="4" width="372" height="111" /></a>

<b>Ahora nos pide que indiquemos la longitud de bits de las claves RSA, nosotros pondremos un término medio y el que nos aconseja, esta longitud es 2048</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/5.png"><img class="aligncenter size-full wp-image-398" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/5.png" alt="5" width="414" height="49" /></a>

<b>Ahora indicaremos el tiempo que queremos que tenga de vida la clave, nosotros usaremos 1y, para indicar 1 año</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/6.png"><img class="aligncenter size-full wp-image-399" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/6.png" alt="6" width="402" height="132" /></a>

<b>Nos indicara el día y hora de la expiración de la clave y preguntara si es correcto, damos y avanzamos</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/7.png"><img class="aligncenter size-full wp-image-400" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/7.png" alt="7" width="392" height="37" /></a>

<b>Ahora nos preguntara el nombre real del que crea la clave, yo pongo el nombre de usuario</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/8.png"><img class="aligncenter size-full wp-image-401" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/8.png" alt="8" width="626" height="98" /></a>

<b>Seguidamente, nos preguntara el email,  le ponemos, y avanzamos a lo siguiente</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/9.png"><img class="aligncenter size-full wp-image-402" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/9.png" alt="9" width="322" height="23" /></a>

<b>Después nos dirá si todo es correcto y nos mostrara el nombre e email del usuario, damos O y pasamos al siguiente paso</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/10.png"><img class="aligncenter size-full wp-image-403" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/10.png" alt="10" width="469" height="73" /></a>

<b>Lo siguiente sería crear la clave, para ello la indicamos la clave que queramos usar, la repetimos dos veces</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/12.png"><img class="aligncenter size-full wp-image-404" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/12.png" alt="12" width="427" height="30" /></a>

<b>Ahora generara el proceso de creación de la clave, esto nos puede solicitar que utilicemos recursos del sistema, abrimos ventanas, navegadores, etc para que complete la creación de la clave asimétrica.</b>

<b>Después nos dará un mensaje con la información del proceso, deberías ser que se ha creado correctamente todo.</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/131.png"><img class="aligncenter size-full wp-image-409" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/131.png" alt="13" width="610" height="241" /></a>

<b>Ahora iremos a comprobar que se han creado las claves correctamente, para ello utilizaremos el comando gpg –k, que nos mostrara las claves que tenemos creadas.</b>

<b>Aquí vemos la clave pública y la privada, y en el medio de ambas, el nombre de usuario de la clave.</b>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/141.png"><img class="aligncenter size-full wp-image-410" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/141.png" alt="14" width="488" height="140" /></a>