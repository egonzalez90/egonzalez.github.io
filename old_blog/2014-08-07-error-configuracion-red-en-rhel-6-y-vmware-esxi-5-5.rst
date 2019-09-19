--- layout: post title: Error configuración red en RHEL 6 y VMware ESXi
5.5 date: 2014-08-07 16:49:14.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Linux -
Virtualizacion tags: - '5.5' - 70-persistent-net.rules - clon - clondado
- daemon - esxi - eth0 - ifcfg-eth - linux - network - network manager -
nic - nm_controlled - red hat - rhel6 - sysadmin - virtualizacion -
vmware - vmxnet3 meta: \_edit_last: '2' \_login_radius_meta:
a:1:{s:7:"sharing";i:0;} \_layout: inherit \_nxs_snap_sh_FB0_1407426560:
a:33:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";i:0;s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:42:"(%TITLE%)
has been published on
%SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:184:"CAAHwRlZABTT4BAJUZAayCdD8sT9vucqP95dtUZAPJ5bmoC6gIB55tOiHIny4rESJKtch31GgGgKVPKMn22UrmAy0QDSE1A2jeun45RPysZAvHGxiz6KoWknUrezqkRtdThZAgxAYOVgKZC8XQ1gp4MAhyNNbsIjeBVlCAn9h6aZAAmih8x3NFKM";s:18:"fbAppPageAuthToken";s:184:"CAAHwRlZABTT4BAJUZAayCdD8sT9vucqP95dtUZAPJ5bmoC6gIB55tOiHIny4rESJKtch31GgGgKVPKMn22UrmAy0QDSE1A2jeun45RPysZAvHGxiz6KoWknUrezqkRtdThZAgxAYOVgKZC8XQ1gp4MAhyNNbsIjeBVlCAn9h6aZAAmih8x3NFKM";s:13:"fbAppAuthUser";s:10:"1161837279";s:17:"fbAppAuthUserName";s:31:"Dudu
Gonzalez
(dudu.gonzalez90)";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:8:"urlToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1407426560;}
snap_isAutoPosted: '1' \_nxs_snap_sh_TW0_1407426556:
a:37:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:34:"https://twitter.com/DuduGonzalez90";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:15:"%TITLE%
-
%URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"rpstStop";s:1:"O";s:8:"isPosted";s:0:"";s:8:"imgToUse";s:0:"";s:2:"ii";i:0;s:9:"timeToRun";i:1407426556;}
snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW: N;
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568010466;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:559;}i:1;a:1:{s:2:"id";i:590;}i:2;a:1:{s:2:"id";i:790;}}}}
dsq_thread_id: '6121752983' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/error-configuracion-red-en-rhel-6-y-vmware-esxi-5-5/" ---

Ultimamente, desde que hemos empezado a trabajar mas con RHEL 6, nos
dimos cuenta que tras el clonado de las VM, las interfaces de red no se
configuraban bien.

Primero vimos que las MAC de la eth, no se asignaban correctamente, y
despues comprobamos que una vez configuradas al hacer reboot o reinicio
de la red, estas se configuraban como les daba la gana y perdias la
configuracion e internet.

Pues bien, tras un proceso de investigacion llege a la solucion( o al
menos en nuestro sistema), los pasos son los siguientes:

-Quitar las NIC de la antigua configuracion

-Añadir las NIC en vmxnet3 en el vCenter igual que estaban configuradas
anteriormente

-Borrar el archivo /etc/udev/rules.d/70-persistent-net.rules

-Configurar los archivos /etc/sysconfig/network-scripts/ifcfg-eth\*
añadiendo la linea entre su configuracion

**NM_CONTROLLED=no**

-Parar el servicio NetworkManager y deshabilitarlo del arranque

**service NetworkManager stop**

**chkconfig NetworkManager off**

-Habilitar el servicio network en arranque(puede que ya lo esté)

**chkconfig network on**

-Instalar las vmtools

-Reiniciar la maquina y comprobar que no cambia la configuración entre
el inicio del sistema y tras service network restart

 

Bien, el problema que había, es que por algún error, el network manager
se hacia con el control de la red y daba errores con el demonio network,
lo que hacemos para solucionarlo es, borrar el archivo de la
configuración de las tarjetas,configurar las eth deshabilitando el
control por el Network manager y después deshabilitar Network Manager
del sistema.

De este modo nos funciona sin ningun problema la red.

Espero haber ayudado, un saludo
