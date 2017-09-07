---
id: 934
title: Primera instancia
date: 2015-02-23T13:24:48+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=934
permalink: /primera-instancia/
categories:
  - OpenStack
tags:
  - crear
  - habilitar
  - icehouse
  - icmp
  - instancias
  - openstack
  - ping
  - primera
  - security group
  - ssh
  - ssh-keygen
  - vnc
---
Primero creamos la clave.
<blockquote># ssh-keygen</blockquote>
Añadimos la clave creada a openstack.
<blockquote># nova keypair-add --pub-key ~/.ssh/id_rsa.pub [nombre]</blockquote>
Comprobamos que está asociada en nuestro entorno.
<blockquote># nova keypair-list</blockquote>
Para crear instancias necesitaremos los siguientes valores:
<ul>
	<li>Flavors (# nova flavor-list)</li>
	<li>Imagenes (# nova image-list)</li>
	<li>Networks (# nova net-list)</li>
	<li>securityGroups (# nova secgroup-list)</li>
</ul>
Una vez tenemos esos valores necesarios procederemos a crear una instancia.
<blockquote># nova boot --flavor [flavor] --image [image_ID] --nic net-id=[net_ID] --security-group [SecGroup] --key-name [keyname] [NombreInstancia]</blockquote>
Ejemplo:
<blockquote>nova boot --flavor m1.tiny --image cirros-0.3.2-x86_64 --nic net-id=[NET_ID] --security-group default --key-name demo-key Instancia1</blockquote>
Comprobremos el estado de la instancia.
<blockquote># nova list</blockquote>
Crearemos una sesion por VNC.
<blockquote># nova get-vnc-console [Instancia] novnc</blockquote>
Habilitamos Ping y SSH al Security Group "Default".
<blockquote># nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0

# nova secgroup-add-rule default tcp 22 22 0.0.0.0/0</blockquote>
Comprobamos las conexiones por ping y por SSH.
<blockquote># ssh cirros@IP

*Password por defecto cubswin:)</blockquote>