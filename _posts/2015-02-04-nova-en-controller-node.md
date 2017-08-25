---
id: 879
title: Nova en Controller Node
date: 2015-02-04T17:11:09+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=879
permalink: /nova-en-controller-node/
categories:
  - OpenStack
tags:
  - cloud
  - compute
  - configurar
  - controller
  - image-list
  - nova
  - openstack
  - service
---
Instalaremos los paquetes de Nova en Controller node.
<blockquote># yum install openstack-nova-api openstack-nova-cert openstack-nova-conductor 

openstack-nova-console openstack-nova-novncproxy openstack-nova-scheduler 

openstack-python-novaclient</blockquote>
Configuramos nova para que use nuestra base de datos.
<blockquote># openstack-config --set /etc/nova/nova.conf database connection mysql://nova:PASSWD@controller/nova</blockquote>
Configuramos el uso de QPID.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT rpc_backend qpid

# openstack-config --set /etc/nova/nova.conf DEFAULT qpid_hostname controller</blockquote>
Configuramos algunos parámetros como el vnc.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT my_ip 192.168.1.11

# openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_listen 192.168.1.11

# openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_proxyclient_address    192.168.1.11</blockquote>
Creamos el usuario nova en la base de datos.
<blockquote># mysql -u root -p

# CREATE DATABASE nova;

# GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'localhost' IDENTIFIED BY 'passwd';

# GRANT ALL PRIVILEGES ON nova.* TO 'nova'@'%' IDENTIFIED BY 'passwd';</blockquote>
Creamos las tablas de nova en la base de datos.
<blockquote># su -s /bin/sh -c "nova-manage db sync" nova</blockquote>
Creamos el usuario nova en el tenant service con rol de admin.

# keystone user-create --name=nova --pass=PASSWD --email=nova@mail.com

# keystone user-role-add --user=nova --tenant=service --role=admin

Configuramos nova para que use keystone.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT auth_strategy keystone

# openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_uri http://controller:5000

# openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_host controller

# openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_protocol http

# openstack-config --set /etc/nova/nova.conf keystone_authtoken auth_port 35357

# openstack-config --set /etc/nova/nova.conf keystone_authtoken admin_user nova

# openstack-config --set /etc/nova/nova.conf keystone_authtoken admin_tenant_name service

# openstack-config --set /etc/nova/nova.conf keystone_authtoken admin_password PASSWD</blockquote>
Registramos el servicio en nova y creamos el endpoint.
<blockquote># keystone service-create --name=nova --type=compute --description="Openstack Compute"

# keystone endpoint-create 
--service-id=$(keystone service-list | awk '/ compute / {print $2}') 
--publicurl=http://controller:8774/v2/%(tenant_id)s 
--internalurl=http://controller:8774/v2/%(tenant_id)s 
--adminurl=http://controller:8774/v2/%(tenant_id)s</blockquote>
Iniciamos los servicios y establecemos la ejecución en el arranque.
<blockquote># service openstack-nova-api start

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

# chkconfig openstack-nova-novncproxy on</blockquote>
Comprobamos que esta correctamente configurado
<blockquote># nova image-list</blockquote>
&nbsp;