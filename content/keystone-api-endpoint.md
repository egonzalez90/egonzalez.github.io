Title: Keystone API endpoint
Date: 2014-12-23 18:14
Author: egongu90
Category: OpenStack
Tags: api, cloud, endpoint, identity service, keystone, openstack
Slug: keystone-api-endpoint
Status: published

Una vez configurado Keystone, creados sus usuarios y el servicio,
deberemos de decirle a Identity Service donde debe ir a "buscar" el
servicio. Para ello configuramos los Endpoints, que no son ni mas ni
menos que las direcciones donde están los servicios.Al tener únicamente
a Identity Service configurado solo tenemos que configurar un Endpoint
(de momento)

Antes que nada, debemos tener Identity Service configurado, para ello lo
haremos mediante el siguiente comando:

> keystone service-create --name=keystone --type=identity
> --description="Openstack Identity"

El siguiente paso a realizar es especificar/crear el Endpoint a Keystone
de Identity Service. para ello necesitaremos el ID del servicio creado
en el paso anterior.

> keystone endpoint-create --service-id=\<ID\>
>
> --publicurl=http://controller:5000/v2.0
>
> --internalurl=http://controller:5000/v2.0
>
> --adminurl=http://controller:35357/v2.0

 
