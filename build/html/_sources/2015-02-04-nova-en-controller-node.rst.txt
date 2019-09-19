--- layout: post title: Nova en Controller Node date: 2015-02-04
17:11:09.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - cloud -
compute - configurar - controller - image-list - nova - openstack -
service meta: \_edit_last: '2' \_publicize_twitter_user: "@egongu90"
\_wpas_mess: Nova en Controller Node \_wpas_skip_10228321: '1'
\_wpas_done_all: '1' \_wpas_skip_8706018: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1566933424;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:898;}i:1;a:1:{s:2:"id";i:927;}i:2;a:1:{s:2:"id";i:871;}}}}
dsq_thread_id: '6203237768' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/nova-en-controller-node/" ---

Instalaremos los paquetes de Nova en Controller node.

   # yum install openstack-nova-api
   openstack-nova-cert openstack-nova-conductor

   openstack-nova-console openstack-nova-novncproxy
   openstack-nova-scheduler

   openstack-python-novaclient

Configuramos nova para que use nuestra base de datos.

   # openstack-config --set /etc/nova/nova.conf database connection
   mysql://nova:PASSWD@controller/nova

Configuramos el uso de QPID.

   # openstack-config --set /etc/nova/nova.conf DEFAULT rpc_backend qpid

   # openstack-config --set /etc/nova/nova.conf DEFAULT qpid_hostname
   controller

Configuramos algunos parámetros como el vnc.

   # openstack-config --set /etc/nova/nova.conf DEFAULT my_ip
   192.168.1.11

   # openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_listen
   192.168.1.11

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   vncserver_proxyclient_address    192.168.1.11

Creamos el usuario nova en la base de datos.

   # mysql -u root -p

   # CREATE DATABASE nova;

   # GRANT ALL PRIVILEGES ON nova.\* TO 'nova'@'localhost' IDENTIFIED BY
   'passwd';

   # GRANT ALL PRIVILEGES ON nova.\* TO 'nova'@'%' IDENTIFIED BY
   'passwd';

Creamos las tablas de nova en la base de datos.

   # su -s /bin/sh -c "nova-manage db sync" nova

Creamos el usuario nova en el tenant service con rol de admin.

# keystone user-create --name=nova --pass=PASSWD --email=nova@mail.com

# keystone user-role-add --user=nova --tenant=service --role=admin

Configuramos nova para que use keystone.

   # openstack-config --set /etc/nova/nova.conf DEFAULT auth_strategy
   keystone

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   auth_uri http://controller:5000

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   auth_host controller

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   auth_protocol http

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   auth_port 35357

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   admin_user nova

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   admin_tenant_name service

   # openstack-config --set /etc/nova/nova.conf keystone_authtoken
   admin_password PASSWD

Registramos el servicio en nova y creamos el endpoint.

   # keystone service-create --name=nova --type=compute
   --description="Openstack Compute"

   | # keystone endpoint-create
   | --service-id=$(keystone service-list \| awk '/ compute / {print
     $2}')
   | --publicurl=http://controller:8774/v2/%(tenant_id)s
   | --internalurl=http://controller:8774/v2/%(tenant_id)s
   | --adminurl=http://controller:8774/v2/%(tenant_id)s

Iniciamos los servicios y establecemos la ejecución en el arranque.

   # service openstack-nova-api start

   # service openstack-nova-cert start

   # service openstack-nova-consoleauth start

   # service openstack-nova-scheduler start

   # service openstack-nova-conductor start

   # service openstack-nova-novncproxy start

   # chkconfig openstack-nova-api on

   # chkconfig openstack-nova-cert on

   # chkconfig openstack-nova-consoleauth on

   # chkconfig openstack-nova-scheduler on

   # chkconfig openstack-nova-conductor on

   # chkconfig openstack-nova-novncproxy on

Comprobamos que esta correctamente configurado

   # nova image-list
