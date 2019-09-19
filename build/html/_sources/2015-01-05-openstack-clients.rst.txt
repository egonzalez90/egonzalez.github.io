--- layout: post title: Openstack Clients date: 2015-01-05
16:23:16.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - clients -
openstack - pip - setuptools meta: \_edit_last: '2' \_thumbnail_id:
'615' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_wpas_skip_10228321: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567602031;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:731;}i:1;a:1:{s:2:"id";i:806;}i:2;a:1:{s:2:"id";i:932;}}}}
dsq_thread_id: '6663698121' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/openstack-clients/" ---

En esta entrada instalaremos las tools de openstack que facilitaran la
configuración de los diferentes módulos que compondrán nuestro entorno.

Primero instalaremos setuptools

   wget https://bootstrap.pypa.io/ez_setup.py -O \| python

A continuacion instalamos PIP

   yum install python-pip

Instalaremos los clientes de los diferentes módulos que vamos a instalar
en el entorno

   pip install python-novaclient

   pip install python-swiftclient

   pip install python-keystoneclient

   pip install python-glanceclient

   pip install python-neutronclient

   pip install python-cinderclient
