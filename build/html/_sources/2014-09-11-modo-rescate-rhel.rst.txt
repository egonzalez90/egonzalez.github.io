--- layout: post title: Modo rescate monousuario RHEL date: 2014-09-11
15:50:28.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux tags: - a - centos -
error - grub - inicio - monousuario - red hat - rescate - rescue mode -
rhel - single - sistema - user meta: \_edit_last: '2'
\_login_radius_meta: '0' kopa_resolution_total_view: '2' snap_MYURL: ''
snapEdIT: '1' snapFB: N; snap_isAutoPosted: '1' snapTW: N;
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568834985;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:541;}i:1;a:1:{s:2:"id";i:584;}i:2;a:1:{s:2:"id";i:481;}}}}
dsq_thread_id: '6105057393' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/modo-rescate-rhel/" ---

Cuando en el arranque te da algún error de configuración e impide un
inicio del sistema operativo normal, la solución es iniciar en modo
monousuario son red para arreglar dichos errores. Para ello seguiremos
estos pasos

Cuando aparece el GRUB, pulsar cualquier botón para entrar a la
selección del SO a arrancar,aquí pulsar <a> y a continuación pulsaremos
espacio y escribiremos <single>, de esta forma iniciaremos en modo
monousuario sin red. Con lo que podremos solucionar los errores de
configuración que nos impedían el arranque normal del sistema
