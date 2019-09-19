--- layout: post title: Syslog y coredump vCenter date: 2014-08-08
16:55:09.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Virtualizacion tags: - cloud
- collector - coredump - esxi - log - syslog - vcenter - virtualizacion
- vmware meta: \_edit_last: '2' \_login_radius_meta:
a:1:{s:7:"sharing";i:0;} \_layout: inherit snap_MYURL: '' snapEdIT: '1'
snapFB: N; snap_isAutoPosted: '1' snapTW: N;
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1566959700;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:513;}i:1;a:1:{s:2:"id";i:541;}i:2;a:1:{s:2:"id";i:551;}}}}
dsq_thread_id: '6284386517' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/syslog-y-coredump-vcenter/" ---

Vamos a configurar syslog y coredump de los host ESXi para que un
vCenter recoja los logs de estos host

Primero deberemos tener instaladas y configuradas en el vCenter estas
aplicaciones:

Dump Collector y Syslog collector.

| Para configurar el Syslog
| # esxcli system syslog config set --loghost="IPHOST"
| # esxcli system syslog reload

| Para configurar el Coredump
| # esxcli system coredump network set --interface-name vmk0
  --server-ipv4 "IPHOST"
| # esxcli system coredump network set --enable true
| # esxcli system coredump network get ( para comprobar que todo ok )
| --interface-name vmkX Hay que ver por que vmk ve la red de gestión

Estos comandos habría que ejecutarlos por cada host ESXi que queramos
que envié los logs al vCenter

 

Un saludo y espero que sea de ayuda
