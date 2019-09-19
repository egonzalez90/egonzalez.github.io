--- layout: post title: Configuración de Image Service Glance date:
2015-01-29 17:36:59.000000000 +01:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - configuracion - glance - glance-api - image service -
instalacion - openstack meta: \_edit_last: '2'
\_publicize_facebook_user: https://www.facebook.com/dudu.gonzalez90
\_publicize_twitter_user: "@hidanstillalive" \_wpas_done_all: '1'
\_wpas_skip_5226565: '1' \_wpas_skip_8706018: '1' \_wpas_skip_10228321:
'1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1566777052;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:879;}i:1;a:1:{s:2:"id";i:816;}i:2;a:1:{s:2:"id";i:898;}}}}
dsq_thread_id: '6177884447' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/configuracion-de-image-service-glance/" ---

Lo primero que debemos instalar son los paquetes de Glance en Controller
Node.

   # yum install openstack-glance python-glanceclient

Después configuraremos en enlace con la base de datos en los ficheros de
configuración de Glance:

   # openstack-config --set /etc/glance/glance-api.conf

   database connection mysql://glance:PASSWD@controller/glance

   # openstack-config --set /etc/glance/glance-registry.conf

   database connection mysql://glance:PASSWD@controller/glance

A continuación crearemos el usuario y la base de datos de Glance

   mysql -u root -p

   # CREATE DATABASE glance;

   #GRANT ALL PRIVILEGES ON glance.\* TO 'glance'@'localhost' IDENTIFIED
   BY 'PASSWD'

   #GRANT ALL PRIVILEGES ON glance.\* TO 'glance'@'%' IDENTIFIED BY
   'PASSWD'

Crearemos las tablas en la base de datos

   # su -s /bin/sh -c "glance-manage db_sync" glance

Creamos el usuario Glance en keystone con tenant "service" y rol "admin"

   # keystone user-create --name=glance --pass=PASSWD
   --email=email@mail.com

   # keystone user-role-add --user=glance --tenant-service --role=admin

A continuación modificaremos los ficheros de configuración de Glance

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken auth_uri http://controller:5000

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken  auth_host controller

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken auth_port 35357

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken auth_protocol http

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken admin_tenant_name service

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken admin_user glance

   # openstack-config --set /etc/glance/glance-api.conf
   keystone_authtoken admin_password PASSWD

   # openstack-config --set /etc/glance/glance-api.conf paste_deploy
   flavor keystone

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken auth_uri http://controller:5000

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken auth_host controller

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken auth_port 35357

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken auth_protocol http

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken admin_tenant_name service

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken admin_user glance

   # openstack-config --set /etc/glance/glance-registry.conf
   keystone_authtoken admin_password PASSWD

   # openstack-config --set /etc/glance/glance-registry.conf
   paste_deploy flavor keystone

Después de configurar los ficheros anteriores, registraremos el servicio
y creamos el endpoint

   # keystone service-create --name=glance --type=image
   --description="Image Service"

   # keystone endpoint-create --service-id=<ID>

   --publicurl=http://controller:9292

   --internalurl=http://controller:9292

   --adminurl=http://controller:9292

Iniciamos el servicio y habilitamos la ejecución en el arranque

   # service openstack-glance-api start

   # service openstack-glance-registry start

   #chkconfig openstack-glance-api on

   # chkconfig openstack-glance-registry on
