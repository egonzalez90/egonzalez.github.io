--- layout: post title: Reiniciar "quota count" incorrecto Openstack
date: 2014-09-07 15:50:41.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - bbdd - cloud - count - cuenta - cuota - error - ID - incorrecto
- nova - openstack - quota - reinicio - reset - tenant - usage meta:
\_edit_last: '2' \_login_radius_meta: '0' kopa_resolution_total_view:
'5' \_thumbnail_id: '615' snap_MYURL: '' snapEdIT: '1' snapFB: N;
snap_isAutoPosted: '1' snapTW: N; \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567402865;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:563;}i:1;a:1:{s:2:"id";i:934;}i:2;a:1:{s:2:"id";i:769;}}}}
dsq_thread_id: '6313201661' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/reiniciar-quota-count-incorrecto-openstack/" ---

Para reiniciar quota count, deberemos conectarnos a la base de datos y
establecer in_use en "-1"

   mysql -u nova -p<password> nova

   select*from quota_usages;

   update quota_usages set in_use='-1'where project_id='<my project
   id>';

A partir de la versión Icehouse, ya no se usa -1 y se pasa a usar 0

   update quota_usages set in_use='0'where project_id='<my project id>';
