--- layout: post title: Comprobar Glance Image Service date: 2015-02-04
16:34:08.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - cloud -
comprobar - glance - image - image-create - image-list - openstack -
service meta: \_edit_last: '2' \_wpas_mess: Comprobar Glance Image
Service \_wpas_skip_10228321: '1' \_wpas_done_all: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1566933703;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:934;}i:1;a:1:{s:2:"id";i:777;}i:2;a:1:{s:2:"id";i:577;}}}}
dsq_thread_id: '6177978644' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/comprobar-glance-image-service/" ---

Una vez configurado Image Service, comprobaremos que funciona
correctamente creando una carpeta y añadiendo una imagen de Cirros a
nuestro nuevo entorno.

Lo primero que haremos será crear una carpeta y descargaremos la imagen
de Cirros.

   # mkdir /tmp/images

   # cd /tmp/images

   #
   wget http://download.cirros-cloud.net/0.3.3/cirros-0.3.3-x86_64-disk.img

Crearemos la imagen de Cirros en Glance

   # glance image-create --name=cirros --disk-format=qcow2
   --container-format=bare --is-public=True --      progress
   > cirros-0.3.3-x86_64-disk.img

Listamos las imagenes disponibles

   # glance image-list

Eliminamos el archivo descargado de Cirros

   # rm -rf /tmp/images/cirros-0.3.3-x86_64-disk.img
