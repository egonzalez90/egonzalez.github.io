---
id: 790
title: Configuracion de red basica Openstack
date: 2014-10-19T16:46:16+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=790
permalink: /configuracion-de-red-basica-openstack/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - 3 nodos
  - basica
  - centos
  - compute
  - controller
  - eth0
  - network
  - openstack
  - red
  - redhat
  - rhel
---
En la siguiente entrada tienes como configurar las tarjetas de red para realizar esta instalación de Openstack: <a title="Configuracion basica red RHEL y centOS" href="http://egonzalez.org/configuracion-basica-red-rhel-y-centos/" target="_blank">Configuración básica de red RHEL</a>

Aquí mostrare el esquema conceptual de como ira configurada cada tarjeta de los distintos nodos.<!--more-->
<h1> CONTROLLER</h1>
<blockquote>hostname controller</blockquote>
<h3>eth0:</h3>
<ul>
	<li>IP 192.168.1.11</li>
	<li>GATEWAY 192.168.1.1</li>
</ul>
<h1>NETWORK</h1>
<blockquote>hostname network</blockquote>
<h3>eth0</h3>
<ul>
	<li>IP 192.168.1.21</li>
	<li>GATEWAY 192.168.1.1</li>
</ul>
<h3>eth1</h3>
<ul>
	<li>IP 10.0.1.21</li>
</ul>
<h3>External network (eth2)</h3>
<ul>
	<li>En el archivo de configuración dejaremos BOOTPROTO=none, sin configurar IP ni Netmask</li>
</ul>
<h1>COMPUTE</h1>
<blockquote>hostname compute1</blockquote>
<h3>eth0</h3>
<ul>
	<li>IP 192.168.1.31</li>
	<li>GATEWAY 192.168.1.1</li>
</ul>
<h3>eth1</h3>
<ul>
	<li>IP 10.0.1.31</li>
</ul>
*Los siguientes nodos de cómputo se pueden utilizar las siguientes IP

&nbsp;

En todos los nodos, se ha de configurar el archivo host de la siguiente manera
<blockquote>vi /etc/hosts</blockquote>
<blockquote>192.168.1.11      controller

192.168.1.21      network

192.168.1.31      compute1</blockquote>