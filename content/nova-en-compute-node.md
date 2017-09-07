Title: Nova en Compute Node
Date: 2015-02-05 17:37
Author: egongu90
Category: OpenStack
Tags: compute, configurar, node, nova, openstack, qemu
Slug: nova-en-compute-node
Status: published

Primero instalaremos los paquetes necesarios de nova.

> \# yum install openstack-nova-compute

Configuraremos el uso de la base de datos y de la autenticación en
keystone.

> \# openstack-config --set /etc/nova/nova.conf database connection
> mysql://nova:PASSWD@controller/nova
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT auth\_strategy
> keystone
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken auth\_uri http://controller:5000
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken auth\_host controller
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken auth\_port 35357
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken auth\_protocol http
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken admin\_user nova
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken admin\_tenant\_name service
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> keystone\_authtoken admin\_password PASSWD

Configuramos el uso de QPID.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT rpc\_backend
> qpid
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT qpid\_hostname
> controller

Configuramos VNC.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT my\_ip
> 192.168.1.31
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT vnc\_enabled
> True
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> vncserver\_listen 0.0.0.0
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> vncserver\_proxyclient\_address 192.168.1.31
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> novncproxy\_base\_url http://controller:6080/vnc\_auto.html
>
> Configuramos acceso a Glance Image Service.
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT glance\_host
> controller

Comprobamos si la CPU soporta aceleración por hardware, si es 1 o mas el
resultado si que soporta, si no, configurar libvirt para que utilice
QEMU en vez de KVM.

> \# egrep -c '(vmx|svm)' /proc/cpuinfo

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Configurar libvirt para que use QEMU

> \# openstack-config --set /etc/nova/nova.conf libvirt virt\_type qemu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Iniciar servicios y ejecución en el arranque.

> \# service libvirtd start
>
> \# service messagebus start
>
> \# service openstack-nova-compute start
>
> \# chkconfig libvirt on
>
> \#chkconfig messagebus on
>
> \# chkconfig openstack-nova-compute on
