Title: Configuración de Image Service Glance
Date: 2015-01-29 17:36
Author: egongu90
Category: OpenStack
Tags: configuracion, glance, glance-api, image service, instalacion, openstack
Slug: configuracion-de-image-service-glance
Status: published

Lo primero que debemos instalar son los paquetes de Glance en Controller
Node.

> \# yum install openstack-glance python-glanceclient

Después configuraremos en enlace con la base de datos en los ficheros de
configuración de Glance:

> \# openstack-config --set /etc/glance/glance-api.conf
>
> database connection mysql://glance:PASSWD@controller/glance
>
> \# openstack-config --set /etc/glance/glance-registry.conf
>
> database connection mysql://glance:PASSWD@controller/glance

A continuación crearemos el usuario y la base de datos de Glance

> mysql -u root -p
>
> \# CREATE DATABASE glance;
>
> \#GRANT ALL PRIVILEGES ON glance.\* TO 'glance'@'localhost' IDENTIFIED
> BY 'PASSWD'
>
> \#GRANT ALL PRIVILEGES ON glance.\* TO 'glance'@'%' IDENTIFIED BY
> 'PASSWD'

Crearemos las tablas en la base de datos

> \# su -s /bin/sh -c "glance-manage db\_sync" glance

Creamos el usuario Glance en keystone con tenant "service" y rol "admin"

> \# keystone user-create --name=glance --pass=PASSWD
> --email=email@mail.com
>
> \# keystone user-role-add --user=glance --tenant-service --role=admin

A continuación modificaremos los ficheros de configuración de Glance

> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken auth\_uri http://controller:5000
>
> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken  auth\_host controller
>
> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken auth\_port 35357
>
> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken auth\_protocol http
>
> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken admin\_tenant\_name service
>
> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken admin\_user glance
>
> \# openstack-config --set /etc/glance/glance-api.conf
> keystone\_authtoken admin\_password PASSWD
>
> \# openstack-config --set /etc/glance/glance-api.conf paste\_deploy
> flavor keystone
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken auth\_uri http://controller:5000
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken auth\_host controller
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken auth\_port 35357
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken auth\_protocol http
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken admin\_tenant\_name service
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken admin\_user glance
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> keystone\_authtoken admin\_password PASSWD
>
> \# openstack-config --set /etc/glance/glance-registry.conf
> paste\_deploy flavor keystone

Después de configurar los ficheros anteriores, registraremos el servicio
y creamos el endpoint

> \# keystone service-create --name=glance --type=image
> --description="Image Service"
>
> \# keystone endpoint-create --service-id=\<ID\>
>
> --publicurl=http://controller:9292
>
> --internalurl=http://controller:9292
>
> --adminurl=http://controller:9292

Iniciamos el servicio y habilitamos la ejecución en el arranque

> \# service openstack-glance-api start
>
> \# service openstack-glance-registry start
>
> \#chkconfig openstack-glance-api on
>
> \# chkconfig openstack-glance-registry on
