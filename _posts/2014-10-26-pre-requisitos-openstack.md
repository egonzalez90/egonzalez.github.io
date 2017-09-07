---
id: 798
title: Pre-requisitos Openstack
date: 2014-10-26T16:43:07+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=798
permalink: /pre-requisitos-openstack/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - basico
  - cloud
  - firewalld
  - instalacion
  - iptables
  - network
  - network manager
  - ntp
  - openstack
  - prerequisitos
  - server
---
<h2>NTP</h2>
Deberemos tener instalado NTP en todos los nodos.
<blockquote>yum install ntp</blockquote>
<!--more-->

A continuacion tenemos que configurar los nodos para que usen NTP del nodo controller
<blockquote>vi /etc/ntp.conf</blockquote>
Editamos la linea server para que aparezca lo siguiente
<blockquote>server controller iburst</blockquote>
En el nodo controller borramos las opciones nopeer y noquery de las lineas restrict

Por ultimo iniciaremos el servicio y el nivel de ejecución en el arranque del sistema
<blockquote>service ntpd start

chkconfig ntpd on</blockquote>
<h2>Servicios de red</h2>
Deshabilitamos NetworkManager y habilitamos el servicio network, asi como quitamos y establecemos el nivel de ejecución a cada servicio respectivamente
<blockquote>service NetworkManager stop

service network start

chkconfig NetworkManager off

chkconfig network on</blockquote>
<h2>Servicios cortafuegos</h2>
Paramos y deshabilitamos firewalld por defecto y activamos e iniciamos iptables. Es posible que no tengas instalado firewalld, por lo que no tendrás que deshabilitarlo
<blockquote>service firewalld stop

service iptables start

chkconfig firewalld off

chkconfig iptables on</blockquote>
Estos son los prerequisitos necesarios para iniciar la instalación de un entorno con Openstack

Un saludo