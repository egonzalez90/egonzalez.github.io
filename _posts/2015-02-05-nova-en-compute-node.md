---
id: 898
title: Nova en Compute Node
date: 2015-02-05T17:37:51+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=898
permalink: /nova-en-compute-node/
categories:
  - OpenStack
tags:
  - compute
  - configurar
  - node
  - nova
  - openstack
  - qemu
---
Primero instalaremos los paquetes necesarios de nova.
<blockquote># yum install openstack-nova-compute</blockquote>
Configuraremos el uso de la base de datos y de la autenticación en keystone.
<blockquote># openstack-config --set /etc/nova/nova.conf database connection mysql://nova:PASSWD@controller/nova

# openstack-config --set /etc/nova/nova.conf DEFAULT auth_strategy keystone

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken auth_uri http://controller:5000

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken auth_host controller

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken auth_port 35357

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken auth_protocol http

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken admin_user nova

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken admin_tenant_name service

# openstack-config --set /etc/nova/nova.conf DEFAULT keystone_authtoken admin_password PASSWD</blockquote>
Configuramos el uso de QPID.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT rpc_backend qpid

# openstack-config --set /etc/nova/nova.conf DEFAULT qpid_hostname controller</blockquote>
Configuramos VNC.
<blockquote># openstack-config --set /etc/nova/nova.conf DEFAULT my_ip 192.168.1.31

# openstack-config --set /etc/nova/nova.conf DEFAULT vnc_enabled True

# openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_listen 0.0.0.0

# openstack-config --set /etc/nova/nova.conf DEFAULT vncserver_proxyclient_address 192.168.1.31

# openstack-config --set /etc/nova/nova.conf DEFAULT novncproxy_base_url http://controller:6080/vnc_auto.html

Configuramos acceso a Glance Image Service.

# openstack-config --set /etc/nova/nova.conf DEFAULT glance_host controller</blockquote>
Comprobamos si la CPU soporta aceleración por hardware, si es 1 o mas el resultado si que soporta, si no, configurar libvirt para que utilice QEMU en vez de KVM.
<blockquote># egrep -c '(vmx|svm)' /proc/cpuinfo</blockquote>
**********************************************

Configurar libvirt para que use QEMU
<blockquote># openstack-config --set /etc/nova/nova.conf libvirt virt_type qemu</blockquote>
**********************************************

Iniciar servicios y ejecución en el arranque.
<blockquote># service libvirtd start

# service messagebus start

# service openstack-nova-compute start

# chkconfig libvirt on

#chkconfig messagebus on

# chkconfig openstack-nova-compute on</blockquote>