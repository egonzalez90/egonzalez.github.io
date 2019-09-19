--- layout: post title: Instalacion vCenter Appliance date: 2014-05-04
16:32:47.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Virtualizacion tags: -
appliance - configuracion - error SSO - esxi - instalacion - vcenter -
virtualizacion - vmware - vSphere meta: \_edit_last: '2'
\_login_radius_meta: a:1:{s:7:"sharing";i:0;}
\_nxs_snap_sh_FB0_1399217571:
a:32:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";i:0;s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:42:"(%TITLE%)
has been published on
%SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:18:"fbAppPageAuthToken";s:183:"CAAHwRlZABTT4BAHa5L1j1rQSgQeHGVLk8rZCb7JuVgkDizv9FqTtDVQCX02ZA5bDr1kqFEppdFuJz3oS79n7z8COso57qcDaVZBWLA3PuOEwxNXd1d4y39DjUfTJkQJAMWw0TnZCnSqeDG6KRJ6zpfUu6Gt0ZBAs7Ym3NvKf4BPSCJ8HzoaQCH";s:13:"fbAppAuthUser";s:10:"1161837279";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:8:"urlToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1399217571;}
snap_isAutoPosted: '1' \_nxs_snap_sh_TW0_1399217572:
a:37:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:34:"https://twitter.com/DuduGonzalez90";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:15:"%TITLE%
-
%URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"rpstStop";s:1:"O";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1399217572;}
\_thumbnail_id: '493' snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW: N;
ac_featured_article: '' ac_show_post_thumbnail: '1'
kopa_resolution_total_view: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568745696;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:541;}i:1;a:1:{s:2:"id";i:527;}i:2;a:1:{s:2:"id";i:513;}}}}
dsq_thread_id: '6165434773' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/instalacion-vcenter-appliance/" ---

| En esta entrada mostrare como instalar vCenter Appliance, muchos
  seréis los que os habréis encontrado los errores de SSO al hacer la
  instalación por defecto de vCenter(yo también fui de esos), por eso
  estuve investigando y conseguí instalarlo sin los errores.
| El error de SSO le solucione configurando antes de iniciar el Wizard
  de configuracion la red correctamente en modo estatico. Para ello
  iremos al SO instalado de vCenter y daremos en Login
  `Captura0 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura0.png>`__

Esto nos abrira una consola, en la que nos pide login, el usuario por
defecto es root y la password vmware
`Captura1 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura1.png>`__

Una vez loggeados dentro del sistema, iremos a esta ruta en la que nos
abrira un wizard de configuracion basica de la red.

/opt/vmware/share/vami/vami_config_net

`Captura <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura.png>`__\ Seleccionaremos
para empezar la opcion 6, con la que editaremos la configuracion de la
tarjeta de red eth0.

Nos preguntara si queremos usar IPv6, le daremos que no.

Nos preguntara si queremos utilizar IPv4, aqui damos yes.

Nos preguntara si queremos usar DHCP, a lo que daremos que no.

A continuacion nos solicitara que pongamos una direccion IP valida y
despues una mascara de red

Por ultimo nos mostrara un resumen de la configuracion y daremos a yes
si estamos de acuerdo

`Captura2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura2.png>`__

A continuacion configuraremos la puerta de enlace(gateway), para ello
usaremos la opcion 2 del Main Menu.

Nos pedira que seleccionemos una tarjeta de red para configurar la
default gateway, aqui yo uso eth0 por lo que selecciono la opcion 0.

A continuacion tendremos que poner la puerta de enlace correctamente,
como veis hay que rellenar con tres cifras, por lo que me dio error
cuando solo use
1\ `Captura3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura3.png>`__

A continuacion configuraremos los servidores DNS de nuestro vCenter,
para ello usamos la opcion 4 del Main Menu

Aqui nos pedira dos servidores DNS, el segundo es
opcional\ `Captura4 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura4.png>`__

Lo siguiente seria configurar el hostname del vCenter con la opcion 3,
pondremos un hostname
correcto\ `Captura5 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura5.png>`__

Por ultimo daremos a la opcion 0 del Main Menu para ver la configuracion
completa de la red, comprobaremos que este todo correcto y pulsaremos la
opcion 1 para salir del
wizard\ `Captura6 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6.png>`__

A continuacion iremos a un navegador e iremos a la direccion
https://IP:5480, nos loggearemos con el usuario root y password
vmware\ `Captura6_1 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura6_1.png>`__

Nos saldra este asistente, aceptaremos los terminos de licencia y
uso.\ `Captura7 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura7.png>`__

A continuacion marcaremos la opcion Configure whit default settings y
daremos a Next para configurarlo por defecto, aqui tambien puedes
configurarlo a tu gusto,yo uso la opcion por defecto para este
tutorial\ `Captura8 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura8.png>`__

Nos saldra un resumen en el que tendremos que tener estas opciones asi:

-  Database: Embedded
   SSO: Embedded
   SSO Database: Embedded
   AD Enabled: No

Una vez comprobado esto pulsaremos en
Start\ `Captura9 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura9.png>`__

Despues de esperar un buen rato, nos deberia aparecer todos los check en
verde sin errores, de ser asi pulsaremos en Close

`Captura10 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura10.png>`__

A continuacion iremos a vSphere Client, pondremos la direcion Ip del
vCenter, usuario y contrasena.

Aqui nos pedira que aceptemos el certificado, marcaremos la opcion de
Install this certificate y daremos a
Ignore\ `Captura11 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura11.png>`__

Por ultimo se nos conectara al vCenter Appliance, con esto ya estaria
terminado este
tutorial\ `Captura12 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura12.png>`__

Espero que les sirva de ayuda y puedan conectar sin problemas a vCenter,
gracias por visitar este blog.

Un saludo
