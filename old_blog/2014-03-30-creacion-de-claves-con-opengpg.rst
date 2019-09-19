--- layout: post title: Creación de claves con OpenPGP date: 2014-03-30
15:21:07.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux tags: - asimetrico -
cifrado - clave - linux - opengpg - openpgp - Seguridad - simetrico
meta: \_edit_last: '2' \_login_radius_meta: a:1:{s:7:"sharing";i:0;}
nxs_snap_sh_FB0_1396189273:
a:32:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";i:0;s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:42:"(%TITLE%)
has been published on
%SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:18:"fbAppPageAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:13:"fbAppAuthUser";s:10:"1161837279";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:8:"urlToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1396189273;}
snap_isAutoPosted: '1' nxs_snap_sh_TW0_1396189278:
a:36:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:29:"https://twitter.com/zombies3c";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";s:1:"0";s:7:"rpstHrs";s:1:"0";s:8:"rpstMins";s:1:"0";s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:15:"%TITLE%
-
%URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1396189278;}
\_thumbnail_id: '409' ac_featured_article: '' ac_show_post_thumbnail: ''
snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW: N;
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567980230;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:635;}i:1;a:1:{s:2:"id";i:263;}i:2;a:1:{s:2:"id";i:759;}}}}
dsq_thread_id: '6238836682' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/creacion-de-claves-con-opengpg/" ---

**En esta entrada mostrare el proceso para la creación de claves
simétricas y asimétricas con openpgp en Linux**

` <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png>`__

Clave Simétrica 

**En Linux por defecto te viene instalado openpgp.**

 

**Para crear una clave simétrica, deberemos escribir gpg con el
modificador –c y el nombre del archivo creado que se quiera encriptar**

`1 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png>`__

 

**Esto nos solicitara la clave que queramos asignarla dos veces, la
rellenamos y ya tenemos el archivo encriptado de forma simétrica.**

**Para desencriptar usaremos el comando gpg con el modificado –d y el
archivo que queramos desencriptar, que tiene que acabar en .gpg**

**Esto nos solicitara la clave que le habíamos puesto, y a continuación
nos creara el archivo desencriptado**

`2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/2.png>`__

**Clave asimétrica **

**Para crear la clave asimétrica, pondremos el comando gpg –gen-key**

`3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/3.png>`__

**Esto nos solicitara que le indiquemos el algoritmo de cifrado que
deseemos utilizar, nosotros usaremos la opción 1 default RSA**

`4 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/4.png>`__

**Ahora nos pide que indiquemos la longitud de bits de las claves RSA,
nosotros pondremos un término medio y el que nos aconseja, esta longitud
es 2048**

`5 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/5.png>`__

**Ahora indicaremos el tiempo que queremos que tenga de vida la clave,
nosotros usaremos 1y, para indicar 1 año**

`6 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/6.png>`__

**Nos indicara el día y hora de la expiración de la clave y preguntara
si es correcto, damos y avanzamos**

`7 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/7.png>`__

**Ahora nos preguntara el nombre real del que crea la clave, yo pongo el
nombre de usuario**

`8 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/8.png>`__

**Seguidamente, nos preguntara el email,  le ponemos, y avanzamos a lo
siguiente**

`9 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/9.png>`__

**Después nos dirá si todo es correcto y nos mostrara el nombre e email
del usuario, damos O y pasamos al siguiente paso**

`10 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/10.png>`__

**Lo siguiente sería crear la clave, para ello la indicamos la clave que
queramos usar, la repetimos dos veces**

`12 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/12.png>`__

**Ahora generara el proceso de creación de la clave, esto nos puede
solicitar que utilicemos recursos del sistema, abrimos ventanas,
navegadores, etc para que complete la creación de la clave asimétrica.**

**Después nos dará un mensaje con la información del proceso, deberías
ser que se ha creado correctamente todo.**

`13 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/131.png>`__

**Ahora iremos a comprobar que se han creado las claves correctamente,
para ello utilizaremos el comando gpg –k, que nos mostrara las claves
que tenemos creadas.**

**Aquí vemos la clave pública y la privada, y en el medio de ambas, el
nombre de usuario de la clave.**

`14 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/141.png>`__
