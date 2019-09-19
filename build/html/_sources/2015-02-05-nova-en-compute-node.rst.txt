--- layout: post title: Nova en Compute Node date: 2015-02-05
17:37:51.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - compute -
configurar - node - nova - openstack - qemu meta: \_edit_last: '2'
\_publicize_twitter_user: "@egongu90" \_wpas_mess: Nova en Compute Node
\_wpas_skip_10228321: '1' \_wpas_done_all: '1' \_wpas_skip_8706018: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568830112;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:927;}i:1;a:1:{s:2:"id";i:879;}i:2;a:1:{s:2:"id";i:859;}}}}
dsq_thread_id: '6269998765' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/nova-en-compute-node/" ---

Primero instalaremos los paquetes necesarios de nova.

   # yum install openstack-nova-compute

Configuraremos el uso de la base de datos y de la autenticación en
keystone.

   # openstack-config --set /etc/nova/nova.conf database connection
   mysql://nova:PASSWD@controller/nova

   # openstack-config --set /etc/nova/nova.conf DEFAULT auth_strategy
   keystone

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken auth_uri http://controller:5000

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken auth_host controller

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken auth_port 35357

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken auth_protocol http

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken admin_user nova

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken admin_tenant_name service

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   keystone_authtoken admin_password PASSWD

Configuramos el uso de QPID.

   # openstack-config --set /etc/nova/nova.conf DEFAULT rpc_backend qpid

   # openstack-config --set /etc/nova/nova.conf DEFAULT qpid_hostname
   controller

Configuramos VNC.

   # openstack-config --set /etc/nova/nova.conf DEFAULT my_ip
   192.168.1.31

   # openstack-config --set /etc/nova/nova.conf DEFAULT vnc_enabled True

   # openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_listen
   0.0.0.0

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   vncserver_proxyclient_address 192.168.1.31

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   novncproxy_base_url http://controller:6080/vnc_auto.html

   Configuramos acceso a Glance Image Service.

   # openstack-config --set /etc/nova/nova.conf DEFAULT glance_host
   controller

Comprobamos si la CPU soporta aceleración por hardware, si es 1 o mas el
resultado si que soporta, si no, configurar libvirt para que utilice
QEMU en vez de KVM.

   # egrep -c '(vmx|svm)' /proc/cpuinfo

\*********************************************\*

Configurar libvirt para que use QEMU

   # openstack-config --set /etc/nova/nova.conf libvirt virt_type qemu

\*********************************************\*

Iniciar servicios y ejecución en el arranque.

   # service libvirtd start

   # service messagebus start

   # service openstack-nova-compute start

   # chkconfig libvirt on

   #chkconfig messagebus on

   # chkconfig openstack-nova-compute on
