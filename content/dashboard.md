Title: Dashboard
Date: 2015-02-16 13:11
Author: egongu90
Category: OpenStack
Tags: dashboard, httpd, memcached, openstack
Slug: dashboard
Status: published

Instalamos los paquetes necesarios para usar Dashboard.

> \# yum install memcached python-memcached mod\_wsgi
> openstack-dashboard

Editamos el siguiente fichero y añadimos/modificamos las lineas
Allowed\_hosts y Openstack\_host.

> \# vi /etc/openstack-dashboard/local-settings
>
> ALLOWED\_HOSTS=['\*']
>
> OPENSTACK\_HOST="controller"

Permitimos conexiones al servicio httpd en la politica de SElinux.

> \# setsebool -P httpd\_can\_network\_connect on

Iniciamos los servicios y establecemos el nivel de ejecución.

> \# service httpd start
>
> \# service memcached start
>
> \# chkconfig httpd on
>
> \# chkconfig memcached on
