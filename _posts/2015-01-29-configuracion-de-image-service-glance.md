---
id: 871
title: Configuración de Image Service Glance
date: 2015-01-29T17:36:59+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=871
permalink: /configuracion-de-image-service-glance/
categories:
  - OpenStack
tags:
  - configuracion
  - glance
  - glance-api
  - image service
  - instalacion
  - openstack
---
Lo primero que debemos instalar son los paquetes de Glance en Controller Node.
<blockquote># yum install openstack-glance python-glanceclient</blockquote>
Después configuraremos en enlace con la base de datos en los ficheros de configuración de Glance:
<blockquote># openstack-config --set /etc/glance/glance-api.conf 

database connection mysql://glance:PASSWD@controller/glance

# openstack-config --set /etc/glance/glance-registry.conf 

database connection mysql://glance:PASSWD@controller/glance</blockquote>
A continuación crearemos el usuario y la base de datos de Glance
<blockquote>mysql -u root -p

# CREATE DATABASE glance;

#GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'localhost' IDENTIFIED BY 'PASSWD'

#GRANT ALL PRIVILEGES ON glance.* TO 'glance'@'%' IDENTIFIED BY 'PASSWD'</blockquote>
Crearemos las tablas en la base de datos
<blockquote># su -s /bin/sh -c "glance-manage db_sync" glance</blockquote>
Creamos el usuario Glance en keystone con tenant "service" y rol "admin"
<blockquote># keystone user-create --name=glance --pass=PASSWD --email=email@mail.com

# keystone user-role-add --user=glance --tenant-service --role=admin</blockquote>
A continuación modificaremos los ficheros de configuración de Glance
<blockquote># openstack-config --set /etc/glance/glance-api.conf keystone_authtoken auth_uri http://controller:5000

# openstack-config --set /etc/glance/glance-api.conf keystone_authtoken  auth_host controller

# openstack-config --set /etc/glance/glance-api.conf keystone_authtoken auth_port 35357

# openstack-config --set /etc/glance/glance-api.conf keystone_authtoken auth_protocol http

# openstack-config --set /etc/glance/glance-api.conf keystone_authtoken admin_tenant_name service

# openstack-config --set /etc/glance/glance-api.conf keystone_authtoken admin_user glance

# openstack-config --set /etc/glance/glance-api.conf keystone_authtoken admin_password PASSWD

# openstack-config --set /etc/glance/glance-api.conf paste_deploy flavor keystone

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken auth_uri http://controller:5000

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken auth_host controller

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken auth_port 35357

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken auth_protocol http

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken admin_tenant_name service

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken admin_user glance

# openstack-config --set /etc/glance/glance-registry.conf keystone_authtoken admin_password PASSWD

# openstack-config --set /etc/glance/glance-registry.conf paste_deploy flavor keystone</blockquote>
Después de configurar los ficheros anteriores, registraremos el servicio y creamos el endpoint
<blockquote># keystone service-create --name=glance --type=image --description="Image Service"

# keystone endpoint-create --service-id=&lt;ID&gt; 

--publicurl=http://controller:9292 

--internalurl=http://controller:9292 

--adminurl=http://controller:9292</blockquote>
Iniciamos el servicio y habilitamos la ejecución en el arranque
<blockquote># service openstack-glance-api start

# service openstack-glance-registry start

#chkconfig openstack-glance-api on

# chkconfig openstack-glance-registry on</blockquote>