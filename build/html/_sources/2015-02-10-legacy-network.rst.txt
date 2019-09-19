--- layout: post title: Legacy Network date: 2015-02-10
13:11:11.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - configurar
- crear - icehouse - legacy - network - network-create - nova -
openstack - red meta: \_edit_last: '2' \_publicize_twitter_user:
"@egongu90" \_wpas_done_all: '1' \_wpas_mess: Legacy Network
\_wpas_skip_10228321: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567368374;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:879;}i:1;a:1:{s:2:"id";i:898;}i:2;a:1:{s:2:"id";i:871;}}}}
dsq_thread_id: '6177881878' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/legacy-network/" ---

CONTROLLER
==========

En controller node configuraremos nova para el uso de legacy network.

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   network_api_class nova.network.api.API

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   security_group_api nova

Reiniciamos los servicios para que aplique la configuración.

   # service openstack-nova api restart

   # service openstack-nova-scheduler restart

   # service openstack-nova-conductor restart

COMPUTE
=======

Instalamos los paquetes de nova-network en controller node.

   # yum install openstack-nova-network openstack-nova-api

Configuramos varias opciones en nova para el uso de legacy network.

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   network_api_class nova.network.api.API

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   security_group_api nova

   # openstack-config --set /etc/nova/nova.conf DEFAULT network_manager
        nova.network.manager.FlatDHCPManager

   # openstack-config --set /etc/nova/nova.conf DEFAULT firewall_driver
      nova.virt.libvirt.firewall.IptablesFirewallDriver

   # openstack-config --set /etc/nova/nova.conf DEFAULT network_size 254

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   allow_same_net_traffic False

   # openstack-config --set /etc/nova/nova.conf DEFAULT multi_host True

   # openstack-config --set /etc/nova/nova.conf DEFAULT send_arp_for_ha
   True

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   force_dhcp_release True

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   share_dhcp_address True

   # openstack-config --set /etc/nova/nova.conf DEFAULT
   flat_network_bridge br100

   # openstack-config --set /etc/nova/nova.conf DEFAULT flat_interface
   eth1

   # openstack-config --set /etc/nova/nova.conf DEFAULT public_interface
   eth1

Iniciamos los servicios y establecemos el arranque con el host.

   # service openstack-nova-network start

   # service openstack-nova-metadata-api start

   # chkconfig openstack-nova-network on

   # chkconfig openstack-nova-metadata-api on

CREAR REDES
===========

Ahora crearemos la primera red.

   # nova network-create [name] --bridge br100 --multi-host T
   --fixed-range-v4 [IP_RANGE/*]

Ejemplo, teniendo en cuenta que mi NAT usa el rango 192.168.207.0/24:

   # nova network-create demo-net --bridge br100 --multi-host T
   --fixed-range-v4 192.168.207.0/24

Listamos la red.

   # nova net-list

Podemos borrarla de la siguiente forma:

   # nova net-delete [nombre o ID]
