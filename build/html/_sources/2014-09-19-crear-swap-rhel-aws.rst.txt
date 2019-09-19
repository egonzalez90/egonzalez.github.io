--- layout: post title: Crear Swap AWS en RHEL date: 2014-09-19
16:28:40.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux - OpenStack tags: -
"/etc/fstab" - amazon - AWS - cloud - mkswap - red hat - rhel - services
- swap - swapon - web meta: \_edit_last: '2' \_thumbnail_id: '631'
\_nxs_snap_sh_FB0_1411165303:
a:38:{s:4:"doFB";i:1;s:5:"nName";s:8:"Facebook";s:7:"fbAppID";s:15:"545659862207806";s:8:"fbAppSec";s:32:"15477463b8c7d194394cc5dba87a27f1";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:8:"postType";s:1:"A";s:7:"fbAttch";s:1:"2";s:12:"fbAttchAsVid";i:0;s:6:"imgUpl";s:1:"1";s:11:"fbMsgFormat";s:42:"(%TITLE%)
has been published on
%SITENAME%";s:10:"fbMsgAFrmt";s:0:"";s:13:"useFBGURLInfo";s:1:"1";s:10:"riComments";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:5:"fbURL";s:40:"https://www.facebook.com/dudu.gonzalez90";s:6:"fbPgID";s:15:"dudu.gonzalez90";s:14:"fbAppAuthToken";s:194:"CAAHwRlZABTT4BADSJc2zyzQF1btojYn7YvO1zdAG0OEtoUuHmiI8leQgNfzt8I8JXzhECO1ZBQfG3QwywOPbMibSKfa0jxIKxvgdPMxVBZBj44aXMTiad1pLeDF1aTrtjLhFD6jqldqlQSNo52RrmhXhsIYZAfDAgnwpjDSehoz9v5LHjyu25mJUQkkUUUgZD";s:18:"fbAppPageAuthToken";s:194:"CAAHwRlZABTT4BADSJc2zyzQF1btojYn7YvO1zdAG0OEtoUuHmiI8leQgNfzt8I8JXzhECO1ZBQfG3QwywOPbMibSKfa0jxIKxvgdPMxVBZBj44aXMTiad1pLeDF1aTrtjLhFD6jqldqlQSNo52RrmhXhsIYZAfDAgnwpjDSehoz9v5LHjyu25mJUQkkUUUgZD";s:13:"fbAppAuthUser";s:10:"1161837279";s:17:"fbAppAuthUserName";s:31:"Dudu
Gonzalez
(dudu.gonzalez90)";s:6:"atpKey";s:0:"";s:8:"rpstStop";s:1:"O";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"destType";s:2:"pr";s:8:"isPosted";s:0:"";s:8:"imgToUse";b:0;s:8:"urlToUse";b:0;s:2:"ii";i:0;s:9:"timeToRun";i:1411165303;}
snap_isAutoPosted: '1' \_nxs_snap_sh_TW0_1411165297:
a:37:{s:4:"doTW";i:1;s:5:"nName";s:7:"Twitter";s:5:"twURL";s:34:"https://twitter.com/DuduGonzalez90";s:9:"twConsKey";s:21:"QTmaTFDqowEzbyzkicvgg";s:9:"twConsSec";s:43:"9EWEc5dEufuzc3wjm0fZAD8yJdxhFiHcFR06IgsHPb4";s:10:"twAccToken";s:50:"767702022-PedOOiQm697uAVksTggg5Am0W2eiUlXcF1u1kkJ6";s:6:"catSel";s:1:"0";s:8:"catSelEd";s:0:"";s:10:"riComments";i:0;s:11:"riCommentsM";i:0;s:12:"riCommentsAA";i:0;s:8:"rpstDays";i:0;s:7:"rpstHrs";i:0;s:8:"rpstMins";i:0;s:6:"rpstOn";i:0;s:11:"rpstOnlyPUP";i:0;s:7:"fltrsOn";i:0;s:11:"rpstBtwDays";a:0:{}s:13:"twAccTokenSec";s:45:"Bumkti9owi1FxQgY8jOMyRJ6LznMXzcUUWwY0Qmvd0k6N";s:11:"twMsgFormat";s:15:"%TITLE%
-
%URL%";s:8:"attchImg";i:1;s:4:"twOK";i:1;s:11:"rpstRndMins";i:0;s:12:"rpstPostIncl";s:1:"0";s:8:"rpstType";s:1:"2";s:12:"rpstTimeType";s:1:"A";s:12:"rpstFromTime";s:0:"";s:10:"rpstToTime";s:0:"";s:10:"rpstOLDays";s:2:"30";s:10:"rpstNWDays";s:3:"365";s:7:"tagsSel";s:0:"";s:8:"tagsSelX";s:0:"";s:8:"rpstStop";s:1:"O";s:8:"isPosted";s:0:"";s:8:"imgToUse";b:0;s:2:"ii";i:0;s:9:"timeToRun";i:1411165297;}
snap_MYURL: '' snapEdIT: '1' snapTW: N; snapFB: N;
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567104015;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:731;}i:1;a:1:{s:2:"id";i:662;}i:2;a:1:{s:2:"id";i:705;}}}}
dsq_thread_id: '6421019958' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/crear-swap-rhel-aws/" ---

Cuando creas una instancia, esta se hace sin swap, el cual es necesario
para el uso de determinadas aplicaciones.

Para ello deberemos tener espacio en disco, si no tuvieras suficiente
puedes seguir esta entrada pare ver como se
hace: \ `http://egonzalez.org/?p=635 <http://egonzalez.org/?p=662>`__

A continuación iremos a la consola y ejecutaremos los siguientes
comandos:

   sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024

   sudo /sbin/mkswap /var/swap.1

   sudo /sbin/swapon /var/swap.1

| Con ello crearemos el archivo swap y lo montaremos.
| Con este comando se crea de un tamaño de 1024 MB, si se quisiera mas,
  abría que cambiar el valor count a el deseado.

Por ultimo abría que añadir esta linea al archivo /etc/fstab , esto
permitirá que se monte durante el arranque automáticamente.

   /var/swap.1 swap swap defaults 0 0

Espero ser de ayuda, un saludo
