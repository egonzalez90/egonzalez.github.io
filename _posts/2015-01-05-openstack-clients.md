---
id: 866
title: Openstack Clients
date: 2015-01-05T16:23:16+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=866
permalink: /openstack-clients/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - clients
  - openstack
  - pip
  - setuptools
---
En esta entrada instalaremos las tools de openstack que facilitaran la configuración de los diferentes módulos que compondrán nuestro entorno.

Primero instalaremos setuptools
<blockquote>wget https://bootstrap.pypa.io/ez_setup.py -O | python</blockquote>
A continuacion instalamos PIP
<blockquote>yum install python-pip</blockquote>
Instalaremos los clientes de los diferentes módulos que vamos a instalar en el entorno
<blockquote>pip install python-novaclient 

pip install python-swiftclient 

pip install python-keystoneclient 

pip install python-glanceclient 

pip install python-neutronclient 

pip install python-cinderclient</blockquote>
&nbsp;