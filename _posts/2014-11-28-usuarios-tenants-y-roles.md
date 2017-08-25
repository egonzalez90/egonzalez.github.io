---
id: 825
title: Usuarios, Tenants y Roles
date: 2014-11-28T16:22:57+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=825
permalink: /usuarios-tenants-y-roles/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - add
  - admin
  - create
  - demo
  - keystone
  - openstack
  - role
  - service
  - tenant
  - user
---
Una vez tenemos instalado el servicio de Keystone, deberemos crear el usuario de administración, su rol y su tenant. Para ello seguiremos los siguientes pasos:

Como aun no tenemos el usuario de administración, utilizaremos ADMIN_TOKEN para poder utilizar comandos de keystone. Introduciremos estos comandos para establecer ADMIN_TOKEN y el ENDPOINT del servicio:
<blockquote>export OS_SERVICE_TOKEN=$ADMIN_TOKEN

export OS_SERVICE_ENDPOINT=http://controller:35357/v2.0</blockquote>
<h2>USUARIO ADMIN</h2>
A continuación crearemos el usuario Admin mediante el siguiente comando:
<blockquote>keystone user-create --name=admin --pass=PASSWORD --email=mail@mail.com</blockquote>
Una vez creado el usuario deberemos crear el rol de administración
<blockquote>keystone role-create --name=admin</blockquote>
El siguiente es crear el tenant de administración
<blockquote>keystone tenant-create --name=admin --description"Admin Tenant"</blockquote>
Una vez creados el usuario, rol y tenant de administración, deberemos  asignárselos al usuario Admin
<blockquote>keystone user-role-add --user=admin --tenant=admin</blockquote>
Ahora asignaremos al usuario Admin el rol de _member_
<blockquote>keystone user-role-add --user=admin --role=_member_ --tenant=admin</blockquote>
<h2>USUARIOS NORMALES</h2>
Ya tenemos el usuario de administración, ahora crearemos usuarios "normales"

Crearemos un usuario llamado demo
<blockquote>keystone user-create --name=demo --pass=PASSWORD --email=demomail@mail.com</blockquote>
Creamos el tenant demo
<blockquote>keystone tenant-create --name=demo --description="Demo Tenant"</blockquote>
#No volver a crear este mismo tenant cuando se creen otros usuarios que pertenezcan a el

Asignaremos rol y tenant al usuario demo
<blockquote>keystone user-role-add --name=demo --role__member_ tenant=demo</blockquote>
<h2>TENANT SERVICE</h2>
Crearemos el tenant "Service" para los servicios de nuestra instalación de Openstack
<blockquote>keystone tenant-create --name=service --description="Service Tenant"</blockquote>
Con esto ya tendríamos los tenants, roles y usuarios básicos para nuestro entorno.

Un saludo