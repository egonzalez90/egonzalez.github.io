Title: Nova en Controller Node
Date: 2015-02-04 17:11
Author: egongu90
Category: OpenStack
Tags: cloud, compute, configurar, controller, image-list, nova, openstack, service
Slug: nova-en-controller-node
Status: published

Instalaremos los paquetes de Nova en Controller node.

> \# yum install openstack-nova-api
> openstack-nova-cert openstack-nova-conductor
>
> openstack-nova-console openstack-nova-novncproxy
> openstack-nova-scheduler
>
> openstack-python-novaclient

Configuramos nova para que use nuestra base de datos.

> \# openstack-config --set /etc/nova/nova.conf database connection
> mysql://nova:PASSWD@controller/nova

Configuramos el uso de QPID.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT rpc\_backend
> qpid
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT qpid\_hostname
> controller

Configuramos algunos parámetros como el vnc.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT my\_ip
> 192.168.1.11
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> vncserver\_listen 192.168.1.11
>
> \# openstack-config --set /etc/nova/nova.conf DEFAULT
> vncserver\_proxyclient\_address    192.168.1.11

Creamos el usuario nova en la base de datos.

> \# mysql -u root -p
>
> \# CREATE DATABASE nova;
>
> \# GRANT ALL PRIVILEGES ON nova.\* TO 'nova'@'localhost' IDENTIFIED BY
> 'passwd';
>
> \# GRANT ALL PRIVILEGES ON nova.\* TO 'nova'@'%' IDENTIFIED BY
> 'passwd';

Creamos las tablas de nova en la base de datos.

> \# su -s /bin/sh -c "nova-manage db sync" nova

Creamos el usuario nova en el tenant service con rol de admin.

\# keystone user-create --name=nova --pass=PASSWD --email=nova@mail.com

\# keystone user-role-add --user=nova --tenant=service --role=admin

Configuramos nova para que use keystone.

> \# openstack-config --set /etc/nova/nova.conf DEFAULT auth\_strategy
> keystone
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> auth\_uri http://controller:5000
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> auth\_host controller
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> auth\_protocol http
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> auth\_port 35357
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> admin\_user nova
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> admin\_tenant\_name service
>
> \# openstack-config --set /etc/nova/nova.conf keystone\_authtoken
> admin\_password PASSWD

Registramos el servicio en nova y creamos el endpoint.

> \# keystone service-create --name=nova --type=compute
> --description="Openstack Compute"
>
> \# keystone endpoint-create  
>  --service-id=\$(keystone service-list | awk '/ compute / {print
> \$2}')  
>  --publicurl=http://controller:8774/v2/%(tenant\_id)s  
>  --internalurl=http://controller:8774/v2/%(tenant\_id)s  
>  --adminurl=http://controller:8774/v2/%(tenant\_id)s

Iniciamos los servicios y establecemos la ejecución en el arranque.

> \# service openstack-nova-api start
>
> \# service openstack-nova-cert start
>
> \# service openstack-nova-consoleauth start
>
> \# service openstack-nova-scheduler start
>
> \# service openstack-nova-conductor start
>
> \# service openstack-nova-novncproxy start
>
> \# chkconfig openstack-nova-api on
>
> \# chkconfig openstack-nova-cert on
>
> \# chkconfig openstack-nova-consoleauth on
>
> \# chkconfig openstack-nova-scheduler on
>
> \# chkconfig openstack-nova-conductor on
>
> \# chkconfig openstack-nova-novncproxy on

Comprobamos que esta correctamente configurado

> \# nova image-list

 
