--- layout: post title: Usuarios, Tenants y Roles date: 2014-11-28
16:22:57.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - add - admin
- create - demo - keystone - openstack - role - service - tenant - user
meta: \_edit_last: '2' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_thumbnail_id: '615'
\_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1' \_wpas_skip_8706018:
'1' \_wpas_skip_10228321: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568438300;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:862;}i:1;a:1:{s:2:"id";i:859;}i:2;a:1:{s:2:"id";i:816;}}}}
dsq_thread_id: '6119826813' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/usuarios-tenants-y-roles/" ---

Una vez tenemos instalado el servicio de Keystone, deberemos crear el
usuario de administración, su rol y su tenant. Para ello seguiremos los
siguientes pasos:

Como aun no tenemos el usuario de administración, utilizaremos
ADMIN_TOKEN para poder utilizar comandos de keystone. Introduciremos
estos comandos para establecer ADMIN_TOKEN y el ENDPOINT del servicio:

   export OS_SERVICE_TOKEN=$ADMIN_TOKEN

   export OS_SERVICE_ENDPOINT=http://controller:35357/v2.0

USUARIO ADMIN
=============

A continuación crearemos el usuario Admin mediante el siguiente comando:

   keystone user-create --name=admin --pass=PASSWORD
   --email=mail@mail.com

Una vez creado el usuario deberemos crear el rol de administración

   keystone role-create --name=admin

El siguiente es crear el tenant de administración

   keystone tenant-create --name=admin --description"Admin Tenant"

Una vez creados el usuario, rol y tenant de administración, deberemos
 asignárselos al usuario Admin

   keystone user-role-add --user=admin --tenant=admin

Ahora asignaremos al usuario Admin el rol de \_member\_

   keystone user-role-add --user=admin --role=_member\_ --tenant=admin

USUARIOS NORMALES
=================

Ya tenemos el usuario de administración, ahora crearemos usuarios
"normales"

Crearemos un usuario llamado demo

   keystone user-create --name=demo --pass=PASSWORD
   --email=demomail@mail.com

Creamos el tenant demo

   keystone tenant-create --name=demo --description="Demo Tenant"

#No volver a crear este mismo tenant cuando se creen otros usuarios que
pertenezcan a el

Asignaremos rol y tenant al usuario demo

   keystone user-role-add --name=demo --role__member\_ tenant=demo

TENANT SERVICE
==============

Crearemos el tenant "Service" para los servicios de nuestra instalación
de Openstack

   keystone tenant-create --name=service --description="Service Tenant"

Con esto ya tendríamos los tenants, roles y usuarios básicos para
nuestro entorno.

Un saludo
