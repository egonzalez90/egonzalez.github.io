---
id: 859
title: Keystone API endpoint
date: 2014-12-23T18:14:06+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=859
permalink: /keystone-api-endpoint/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - api
  - cloud
  - endpoint
  - identity service
  - keystone
  - openstack
---
Una vez configurado Keystone, creados sus usuarios y el servicio, deberemos de decirle a Identity Service donde debe ir a "buscar" el servicio. Para ello configuramos los Endpoints, que no son ni mas ni menos que las direcciones donde están los servicios.Al tener únicamente a Identity Service configurado solo tenemos que configurar un Endpoint (de momento)

Antes que nada, debemos tener Identity Service configurado, para ello lo haremos mediante el siguiente comando:
<blockquote>keystone service-create --name=keystone --type=identity --description="Openstack Identity"</blockquote>
El siguiente paso a realizar es especificar/crear el Endpoint a Keystone de Identity Service. para ello necesitaremos el ID del servicio creado en el paso anterior.
<blockquote>keystone endpoint-create --service-id=&lt;ID&gt; 

--publicurl=http://controller:5000/v2.0 

--internalurl=http://controller:5000/v2.0 

--adminurl=http://controller:35357/v2.0</blockquote>
&nbsp;