---
id: 927
title: Legacy Network
date: 2015-02-10T13:11:11+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=927
permalink: /legacy-network/
categories:
  - OpenStack
tags:
  - configurar
  - crear
  - icehouse
  - legacy
  - network
  - network-create
  - nova
  - openstack
  - red
---
<h4>CONTROLLER</h4>
En controller node configuraremos nova para el uso de legacy network.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT network_api_class nova.network.api.API

# openstack-config --set /etc/nova/nova.conf DEFAULT security_group_api nova</blockquote>
Reiniciamos los servicios para que aplique la configuración.
<blockquote># service openstack-nova api restart

# service openstack-nova-scheduler restart

# service openstack-nova-conductor restart</blockquote>
<h4>COMPUTE</h4>
Instalamos los paquetes de nova-network en controller node.
<blockquote># yum install openstack-nova-network openstack-nova-api</blockquote>
Configuramos varias opciones en nova para el uso de legacy network.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT network_api_class nova.network.api.API

# openstack-config --set /etc/nova/nova.conf DEFAULT security_group_api nova

# openstack-config --set /etc/nova/nova.conf DEFAULT network_manager      nova.network.manager.FlatDHCPManager

# openstack-config --set /etc/nova/nova.conf DEFAULT firewall_driver    nova.virt.libvirt.firewall.IptablesFirewallDriver

# openstack-config --set /etc/nova/nova.conf DEFAULT network_size 254

# openstack-config --set /etc/nova/nova.conf DEFAULT allow_same_net_traffic False

# openstack-config --set /etc/nova/nova.conf DEFAULT multi_host True

# openstack-config --set /etc/nova/nova.conf DEFAULT send_arp_for_ha True

# openstack-config --set /etc/nova/nova.conf DEFAULT force_dhcp_release True

# openstack-config --set /etc/nova/nova.conf DEFAULT share_dhcp_address True

# openstack-config --set /etc/nova/nova.conf DEFAULT flat_network_bridge br100

# openstack-config --set /etc/nova/nova.conf DEFAULT flat_interface eth1

# openstack-config --set /etc/nova/nova.conf DEFAULT public_interface eth1</blockquote>
Iniciamos los servicios y establecemos el arranque con el host.
<blockquote># service openstack-nova-network start

# service openstack-nova-metadata-api start

# chkconfig openstack-nova-network on

# chkconfig openstack-nova-metadata-api on</blockquote>
<h4>CREAR REDES</h4>
Ahora crearemos la primera red.
<blockquote># nova network-create [name] --bridge br100 --multi-host T --fixed-range-v4 [IP_RANGE/*]</blockquote>
Ejemplo, teniendo en cuenta que mi NAT usa el rango 192.168.207.0/24:
<blockquote># nova network-create demo-net --bridge br100 --multi-host T --fixed-range-v4 192.168.207.0/24</blockquote>
Listamos la red.
<blockquote># nova net-list</blockquote>
Podemos borrarla de la siguiente forma:
<blockquote># nova net-delete [nombre o ID]</blockquote>