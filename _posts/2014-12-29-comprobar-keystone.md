---
id: 862
title: Comprobar Keystone
date: 2014-12-29T18:14:32+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=862
permalink: /comprobar-keystone/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - -
  - comprobar
  - instalacion
  - keystone
  - list
  - openstack
  - role
  - usr
---
En anteriores post hemos configurado Keystone(Identity Service), ahora deberemos de comprobar que este correctamente configurado. Para ello he creado esta entrada en el blog.

Lo primero que haremos será quitar las variables de entorno con las que nos autenticábamos en el servicio, con ello nos tendremos que autenticar con usuario y contraseña.
<blockquote>unset OS_SERVICE_TOKEN OS_SERVICE_ENDPOINT</blockquote>
A continuación crearemos el archivo admin-openrc.sh, en el que configuraremos los datos de nuestro usuario, en este caso el usuario admin previamente creado. Una vez creado el fichero anterior mediante un editor de texto, vi, gedit, nano, etc. Incluiremos el siguiente contenido:
<blockquote>export OS_USERNAME=admin

export OS_PASSWORD=&lt;adminPASSWORD&gt;

export OS_TENANT_NAME=admin

export OS_AUTH_URL=http://controller:35357/v2.0</blockquote>
A continuación, estableceremos las variables de entorno añadidas en el archivo admin-openrc.sh
<blockquote>source admin-openrc.sh</blockquote>
Comprobaremos que podemos listar los usuarios y ya de paso comprobamos que estan bien definidas las variables y por lo tanto estamos utilizando el usuario admin en esta operación
<blockquote>keystone user-list</blockquote>
Listamos los roles del usuario admin
<blockquote>keystone user-role-list --user=admin --tenant=admin</blockquote>
Estos dos últimos comandos nos mostraran una información, en la que comprobaremos que el ID del usuario admin esta en el rol de admin y _member_

&nbsp;

Si todo lo anterior salió correctamente quiere decir que tenemos la configuración básica de Identity Service correctamente realizada y podremos seguir configurando mas servicios en nuestro entorno