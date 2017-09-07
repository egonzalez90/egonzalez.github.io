---
id: 932
title: Dashboard
date: 2015-02-16T13:11:29+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=932
permalink: /dashboard/
categories:
  - OpenStack
tags:
  - dashboard
  - httpd
  - memcached
  - openstack
---
Instalamos los paquetes necesarios para usar Dashboard.
<blockquote># yum install memcached python-memcached mod_wsgi openstack-dashboard</blockquote>
Editamos el siguiente fichero y añadimos/modificamos las lineas Allowed_hosts y Openstack_host.
<blockquote># vi /etc/openstack-dashboard/local-settings

ALLOWED_HOSTS=['*']

OPENSTACK_HOST="controller"</blockquote>
Permitimos conexiones al servicio httpd en la politica de SElinux.
<blockquote># setsebool -P httpd_can_network_connect on</blockquote>
Iniciamos los servicios y establecemos el nivel de ejecución.
<blockquote># service httpd start

# service memcached start

# chkconfig httpd on

# chkconfig memcached on</blockquote>