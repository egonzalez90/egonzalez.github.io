Title: Comprobar Glance Image Service
Date: 2015-02-04 16:34
Author: egongu90
Category: OpenStack
Tags: cloud, comprobar, glance, image, image-create, image-list, openstack, service
Slug: comprobar-glance-image-service
Status: published

Una vez configurado Image Service, comprobaremos que funciona
correctamente creando una carpeta y añadiendo una imagen de Cirros a
nuestro nuevo entorno.

Lo primero que haremos será crear una carpeta y descargaremos la imagen
de Cirros.

> \# mkdir /tmp/images
>
> \# cd /tmp/images
>
> \#
> wget http://download.cirros-cloud.net/0.3.3/cirros-0.3.3-x86\_64-disk.img

Crearemos la imagen de Cirros en Glance

> \# glance image-create --name=cirros --disk-format=qcow2
> --container-format=bare --is-public=True --      progress
> \> cirros-0.3.3-x86\_64-disk.img

Listamos las imagenes disponibles

> \# glance image-list

Eliminamos el archivo descargado de Cirros

> \# rm -rf /tmp/images/cirros-0.3.3-x86\_64-disk.img

 
