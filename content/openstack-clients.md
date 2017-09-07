Title: Openstack Clients
Date: 2015-01-05 16:23
Author: egongu90
Category: OpenStack
Tags: clients, openstack, pip, setuptools
Slug: openstack-clients
Status: published

En esta entrada instalaremos las tools de openstack que facilitaran la
configuración de los diferentes módulos que compondrán nuestro entorno.

Primero instalaremos setuptools

> wget https://bootstrap.pypa.io/ez\_setup.py -O | python

A continuacion instalamos PIP

> yum install python-pip

Instalaremos los clientes de los diferentes módulos que vamos a instalar
en el entorno

> pip install python-novaclient
>
> pip install python-swiftclient
>
> pip install python-keystoneclient
>
> pip install python-glanceclient
>
> pip install python-neutronclient
>
> pip install python-cinderclient

 
