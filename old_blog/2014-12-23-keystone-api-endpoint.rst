--- layout: post title: Keystone API endpoint date: 2014-12-23
18:14:06.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - api - cloud
- endpoint - identity service - keystone - openstack meta: \_edit_last:
'2' \_publicize_facebook_user: https://www.facebook.com/dudu.gonzalez90
\_publicize_twitter_user: "@hidanstillalive" \_thumbnail_id: '615'
\_wpas_done_all: '1' \_wpas_skip_10228321: '1' \_wpas_skip_8706018: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568513735;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:862;}i:1;a:1:{s:2:"id";i:816;}i:2;a:1:{s:2:"id";i:825;}}}}
dsq_thread_id: '6177886015' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/keystone-api-endpoint/" ---

Una vez configurado Keystone, creados sus usuarios y el servicio,
deberemos de decirle a Identity Service donde debe ir a "buscar" el
servicio. Para ello configuramos los Endpoints, que no son ni mas ni
menos que las direcciones donde están los servicios.Al tener únicamente
a Identity Service configurado solo tenemos que configurar un Endpoint
(de momento)

Antes que nada, debemos tener Identity Service configurado, para ello lo
haremos mediante el siguiente comando:

   keystone service-create --name=keystone --type=identity
   --description="Openstack Identity"

El siguiente paso a realizar es especificar/crear el Endpoint a Keystone
de Identity Service. para ello necesitaremos el ID del servicio creado
en el paso anterior.

   keystone endpoint-create --service-id=<ID>

   --publicurl=http://controller:5000/v2.0

   --internalurl=http://controller:5000/v2.0

   --adminurl=http://controller:35357/v2.0
