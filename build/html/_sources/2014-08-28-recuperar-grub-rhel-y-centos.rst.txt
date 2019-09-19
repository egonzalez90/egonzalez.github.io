--- layout: post title: Recuperar GRUB RHEL y CentOS date: 2014-08-28
15:34:51.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux tags: - centos - grub -
hd0 - linux - red hat - rescue - rhel - root - setup meta: \_edit_last:
'2' \_login_radius_meta: a:1:{s:7:"sharing";i:0;}
kopa_resolution_total_view: '5' snap_MYURL: '' snapEdIT: '1' snapFB: N;
snap_isAutoPosted: '1' snapTW: N; \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568413934;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:600;}i:1;a:1:{s:2:"id";i:590;}i:2;a:1:{s:2:"id";i:625;}}}}
dsq_thread_id: '6143187018' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/recuperar-grub-rhel-y-centos/" ---

Muchas veces te sueles cargar la configuración del GRUB, o simplemente
cuando instalas Windows en otra partición. Para ello lo tendremos que
recuperar de la siguiente forma:

1º Insertaremos la ISO en el equipo

2º Cuando salga el prompt de arranque, escribiremos

   linux rescue

3º A continuación

   grub

4º Ahora pondremos este comando, donde hd0,0 es el disco donde esta el
grub

   root (hd0,0)

5º Lo configuraremos

   setup (hd0)

6º Ya terminamos

   quit

   ctrl-d
