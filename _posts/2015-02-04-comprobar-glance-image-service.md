---
id: 877
title: Comprobar Glance Image Service
date: 2015-02-04T16:34:08+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=877
permalink: /comprobar-glance-image-service/
categories:
  - OpenStack
tags:
  - cloud
  - comprobar
  - glance
  - image
  - image-create
  - image-list
  - openstack
  - service
---
Una vez configurado Image Service, comprobaremos que funciona correctamente creando una carpeta y añadiendo una imagen de Cirros a nuestro nuevo entorno.

Lo primero que haremos será crear una carpeta y descargaremos la imagen de Cirros.
<blockquote># mkdir /tmp/images

# cd /tmp/images

# wget http://download.cirros-cloud.net/0.3.3/cirros-0.3.3-x86_64-disk.img</blockquote>
Crearemos la imagen de Cirros en Glance
<blockquote># glance image-create --name=cirros --disk-format=qcow2 --container-format=bare --is-public=True --      progress &gt; cirros-0.3.3-x86_64-disk.img</blockquote>
Listamos las imagenes disponibles
<blockquote># glance image-list</blockquote>
Eliminamos el archivo descargado de Cirros
<blockquote># rm -rf /tmp/images/cirros-0.3.3-x86_64-disk.img</blockquote>
&nbsp;