Title: Legacy Network
Date: 2015-02-10 13:11
Author: egongu90
Category: OpenStack
Tags: configurar, crear, icehouse, legacy, network, network-create, nova, openstack, red
Slug: legacy-network
Status: published

#### CONTROLLER

En controller node configuraremos nova para el uso de legacy network.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> network\_api\_class nova.network.api.API
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> security\_group\_api nova

Reiniciamos los servicios para que aplique la configuración.

> \# service openstack-nova api restart
>
> \# service openstack-nova-scheduler restart
>
> \# service openstack-nova-conductor restart

#### COMPUTE

Instalamos los paquetes de nova-network en controller node.

> \# yum install openstack-nova-network openstack-nova-api

Configuramos varias opciones en nova para el uso de legacy network.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> network\_api\_class nova.network.api.API
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> security\_group\_api nova
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT network\_manager
>      nova.network.manager.FlatDHCPManager
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT firewall\_driver
>    nova.virt.libvirt.firewall.IptablesFirewallDriver
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT network\_size
> 254
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> allow\_same\_net\_traffic False
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT multi\_host True
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> send\_arp\_for\_ha True
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> force\_dhcp\_release True
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> share\_dhcp\_address True
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> flat\_network\_bridge br100
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT flat\_interface
> eth1
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> public\_interface eth1

Iniciamos los servicios y establecemos el arranque con el host.

> \# service openstack-nova-network start
>
> \# service openstack-nova-metadata-api start
>
> \# chkconfig openstack-nova-network on
>
> \# chkconfig openstack-nova-metadata-api on

#### CREAR REDES

Ahora crearemos la primera red.

> \# nova network-create [name] --bridge br100 --multi-host T
> --fixed-range-v4 [IP\_RANGE/\*]

Ejemplo, teniendo en cuenta que mi NAT usa el rango 192.168.207.0/24:

> \# nova network-create demo-net --bridge br100 --multi-host T
> --fixed-range-v4 192.168.207.0/24

Listamos la red.

> \# nova net-list

Podemos borrarla de la siguiente forma:

> \# nova net-delete [nombre o ID]
