---
id: 284
title: Niveles RAID
date: 2014-02-17T00:05:27+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=284
permalink: /niveles-raid/
nxs_snap_sh_FB0_1392595535:
  - 'a:32:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";i:0;s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:42:"(%TITLE%) has been published on %SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:18:"fbAppPageAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:13:"fbAppAuthUser";s:10:"1161837279";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:8:"urlToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1392595535;}'
snap_isAutoPosted:
  - "1"
nxs_snap_sh_TW0_1392595537:
  - 'a:36:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:29:"https://twitter.com/zombies3c";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";s:1:"0";s:7:"rpstHrs";s:1:"0";s:8:"rpstMins";s:1:"0";s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:15:"%TITLE% - %URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1392595537;}'
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
image: /wp-content/uploads/2014/02/220px-Raid0mas1.png
categories:
  - Various
tags:
  - almacenamiento
  - disponibilidad
  - nivel raid
  - niveles
  - raid
  - redundancia
  - Seguridad
---
<h1>Introducción</h1>
Se conoce a RAID como Tecnología de almacenamiento redundante y distribuido, de sus siglas en inglés Redundant Array of Independent Disks.

Este sistema se basa en la utilización de varios discos duros sobre los cuales se distribuirán los datos y alguna información adicional. Este método tiene como fin el mejorar la tolerancia a fallos y la integridad de la información, así como aumentar la capacidad de almacenamiento e incrementar el rendimiento de la transferencia de archivos y su lectura.<!--more-->

En la versión práctica de esta tecnología, el usuario final y el sistema operativo, verán como si solamente hubiera un disco duro, ya que la configuración de RAID es transparente y solamente se verá como una única unidad lógica.

La tecnología que usa RAID es la técnica de stripping, o lo que es lo mismo a la división del espacio de cada disco en bandas: almacena la información junto a los datos de control que permiten la recuperación de la perdida de datos, siendo esta automática en el remplazo de un disco duro averiado.

Los sistemas RAID se dividen en varios niveles, en función del número de discos, numero de bandas, tamaño de las mismas e información de redundancia almacenada en ellas.

La elección de un nivel RAID u otro dependerá siempre de las necesidades que le puedan surgir al usuario, estas necesidades pueden ser seguridad, velocidad, capacidad, coste, etc. No hay niveles mejores que otros, cada uno es apropiado para unas necesidades diferentes.

Una cosa importante a señalar sobre los RAID, es que no sustituyen en ningún caso a las copias de seguridad, además tampoco podrán proteger los datos frente a modificaciones o borrados de forma accidental, asi como que no simplifica la recuperación ante desastres.

Las principales finalidades de un sistema RAID son:
<ul>
	<li>Mejorar la tolerancia a fallos y errores</li>
	<li>Aumentar la integridad de los datos</li>
	<li>Mejorar el rendimiento de los sistemas</li>
	<li>Ofrecer una alternativa frente a los sistemas SCSI</li>
</ul>
Sus ventajas son:
<ul>
	<li>Mayor fiabilidad</li>
	<li>Mayor rendimiento y tasa de transferencia</li>
	<li>Mayor capacidad de almacenamiento</li>
	<li>Mayor integridad</li>
</ul>
Ahora veremos los diferentes niveles RAID:
<h1>RAID 0 – División -  Stripping</h1>
La implementación de este sistema precisa la utilización de al menos dos discos duros. Los datos se distribuirán en stripes o bandas entre ambos discos con la finalidad de acelerar el acceso a la información.

Este tipo de RAID producirá un aumento del rendimiento, ya que se podrá acceder a ambos discos simultáneamente.

Este tipo de tecnología no producirá pérdida de capacidad de almacenamiento, ya que usara todo el disco sin necesidad de duplicar datos ni stripes de control, como ocurre en otros niveles de RAID.

Tiene como inconveniente la perdida de datos en caso de fallo de uno de los discos, ya que no hay duplicación de información ni tolerancia a fallos.

Sus principales características son:
<ul>
	<li>Mínimo 2 discos</li>
	<li>Gran velocidad en las operaciones de lectura y escritura</li>
	<li>No tolerancia a fallos(perdida de datos en caso de caer un disco)</li>
</ul>
El uso de este nivel se basa en:

Los discos duros estarán divididos en stripes, cuando tenemos un dato que vamos a guardar, este se dividirá en los tamaños que tenga establecido el RAID. Supongamos que este dato se ha dividido en 4 partes, el primer dato o parte ira al disco 1, la segunda parte ira al disco 2, la tercera ira al disco 1 y la cuarta al disco 2.

En la imagen se podrá observar cómo están divididos estos datos<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/Raid0.png"><img class="aligncenter size-medium wp-image-287" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/Raid0-230x300.png" alt="Raid0" width="230" height="300" /></a>
<h1>Raid 1 – Espejo –Mirroring</h1>
Este nivel también requiere de la utilización de como mínimo 2 discos duros para poder implementarse.

La gran diferencia entre este RAID 0 y RAID 1 es que en este nivel la información no se repartirá entre ambos discos, aquí se duplicara en los dos discos por igual, por lo que si falla un disco, no perderemos la información almacenada en este, ya que dispondremos del otro para poder acceder a esta información.

Debido a su característica de duplicación de datos recibe el nombre de espejo, ya que un disco será igual al otro. Esto producirá la perdida de la mitad de la capacidad de almacenamiento que tuviéramos entre los dos discos.

El límite de capacidad de almacenamiento vendrá impuesto por el tamaño del disco duro de menor tamaño, ya que de no ser así, el otro disco no podría almacenar la información guardada en el de mayor capacidad.

A cambio de la perdida de la capacidad, este nivel proporciona máxima seguridad con la menor cantidad de discos.

Este nivel es el más lento de todos en la escritura y lectura de datos, aunque las últimas tecnologías de RAID 1 aprovechan que la información esta copiada en ambos discos para realizar peticiones de lectura en paralelo a ambos discos, con lo que el rendimiento se verá incrementado en la fase de lectura.

Cabe recordar que un RAID de nivel 1, jamás deberá sustituir a las copias de seguridad.

Tampoco sirve para proteger de:
<ul>
	<li>Borrado accidental de información</li>
	<li>Virus o malware</li>
	<li>Robo o daño físico</li>
	<li>Corrupción de datos</li>
</ul>
Las principales características son:
<ul>
	<li>Mínimo 2 discos</li>
	<li>2 discos de similar capacidad</li>
	<li>Se realiza una copia exacta en todo momento de modificación de datos<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/Raid1.png"><img class="aligncenter size-medium wp-image-288" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/Raid1-230x300.png" alt="Raid1" width="230" height="300" /></a></li>
</ul>
<h1>RAID 5</h1>
Esta es sin duda una de las implementaciones más populares debido a su bajo coste y las características que ofrece.

Se puede implementar con un mínimo de 3 discos duros, aunque lo óptimo es hacerlo con 5 discos duros. La información se reparte en stripes entre los 4 discos, igual que en raid 0, salvo que en este nivel, se utilizara el primer stripe del 5* disco para almacenar información de paridad, para que en caso de pérdida de un disco, este sistema pueda calcular que información había almacenada en los otros discos y poder recuperar los datos almacenados en el disco perdido. Este dato de paridad, estará distribuida por los 5 discos duros, en la primera banda de datos estará almacenada en el 5* disco, en la segunda en el 4*, así sucesivamente como se puede observar en la imagen.

Las ventajas de RAID 5 son la mínima perdida de capacidad de almacenamiento, su tolerancia a fallos y su buen rendimiento general.

Los mayores inconvenientes a los que se enfrenta RAID  5 son:
<ul>
	<li>El coste y la complejidad de su configuración</li>
	<li>Pérdida de capacidad de almacenamiento</li>
	<li>Penalización en el tiempo de escritura</li>
</ul>
RAID 5 está diseñado para ofrecer el nivel de rendimiento de un RAID 0 con una redundancia más económica y la posibilidad de recuperar la información, es el nivel RAID más habitual que se implementa en la mayoría de las empresas.<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/Raid5.png"><img class="aligncenter size-medium wp-image-289" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/Raid5-300x186.png" alt="Raid5" width="300" height="186" /></a>
<h1>RAID 0+1</h1>
Este tipo de RAID se basa en la combinación de los niveles RAID anteriores, que proporciona velocidad y tolerancia a fallos simultáneamente. Este nivel divide los datos para aumentar el rendimiento, a la vez que también implementa la duplicación de datos para conseguir seguridad frente a perdida de datos. Este tipo de RAID combina el rendimiento de RAID 0 con la redundancia de RAID 1.

El inconveniente de este tipo de RAID es que necesita mínimo 4 discos duros, de los cuales, únicamente 2 serán utilizados para el almacenamiento de información, los otros dos serán utilizados para ofrecer la duplicación de datos.

RAID 0+1 siempre utilizara un numero par de discos duros, así como el ampliar la capacidad de almacenamiento requerirá del uso de 2 discos, lo que incrementan los costes de este tipo de implementación.

El funcionamiento de este nivel es el siguiente:

Disponemos de 4 discos duros, dos de ellos formaran un RAID 0, y los otros dos se utilizaran como RAID 1, es decir, contendrán exactamente la misma información que el RAID 0. Simplificándolo se entendería como la copia exacta de un RAID 0 realizado  por un RAID 1.

Se podrá observar mejor en esta imagen:

Este tipo de implementación se utiliza en sitios donde se requiera un gran rendimiento, tolerancia a fallos pero no gran capacidad. Habitualmente utilizado en servidores de aplicaciones.

Las principales características de RAID 0+1 son:
<ul>
	<li>Rápida lectura y transferencia de archivos</li>
	<li>Redundancia  de datos</li>
	<li>Muy costoso de implementar<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/220px-Raid0mas1.png"><img class="aligncenter size-full wp-image-286" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/220px-Raid0mas1.png" alt="220px-Raid0mas1" width="220" height="191" /></a></li>
</ul>
<h1>RAID 10</h1>
Este tipo de implementación RAID garantiza la integridad de los datos y mejora el rendimiento, con el inconveniente de necesitar como  mínimo 4 discos duros.

Este tipo de RAID está dividido en dos bloques de discos duros en RAID 1, entre estos dos bloques hay formado un RAID 0. Esto hará que los datos se repartirán entre los dos bloques de RAID, y dentro de estos dos bloques, tendrán implementado un RAID 1, con lo que se duplicaran los datos dentro de estos bloques y la información estará dividida entre los dos bloques de discos duros mediante un RAID 0.

Al igual que pasaba con RAID 0+1, este tipo de RAID se utilizara en sitios donde se requiera un buen rendimiento y tolerancia a fallos, sacrificando el volumen de información que podrán almacenar. Este tipo de RAID se implementara en servidores de aplicaciones

Las principales características son:
<ul>
	<li>Gran velocidad</li>
	<li>Mayor seguridad</li>
	<li>Muy costoso de implementar<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/220px-RAID_10.png"><img class="aligncenter size-full wp-image-285" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/220px-RAID_10.png" alt="220px-RAID_10" width="220" height="236" /></a></li>
</ul>
<h1>Resumen de los niveles RAID híbridos</h1>
<ul>
	<li>RAID 0+1: Un espejo de divisiones (mínimo 4 discos)</li>
	<li>RAID 1+0: Una división de espejos</li>
	<li>RAID 30: Una división de niveles RAID con paridad dedicada</li>
	<li>RAID 100: Una división de una división de espejos</li>
	<li>RAID 10+1: Un Espejo de espejos</li>
</ul>
<h1>Bibliografía</h1>
Gran parte de la información viene de esta entrada en  <a href="http://elhacker.net" target="_blank">elhacker.net</a>, agradecer la ayuda que me ha proporcionado en la creacion de esta entrada

<a href="http://blog.elhacker.net/2013/12/tipos-niveles-raid-hardware-software.html">http://blog.elhacker.net/2013/12/tipos-niveles-raid-hardware-software.html</a>