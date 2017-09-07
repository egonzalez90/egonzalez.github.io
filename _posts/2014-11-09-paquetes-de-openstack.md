---
id: 806
title: Paquetes de Openstack
date: 2014-11-09T16:20:27+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=806
permalink: /paquetes-de-openstack/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - cloud
  - epel
  - necesarios
  - openstack
  - paquetes
  - rdo
  - repositorios
---
Esta instalación de paquetes deberemos hacerla en todos los nodos de Openstack(Controller,Network y Compute)

Primero instalaremos yum-plugin-priorities con el que podremos cambiar la prioridad de los repositorios
<blockquote>yum install yum-plugin-priorities</blockquote>
A continuación instalaremos el rpm con los repositorios RDO
<blockquote>yum install https://repos.fedorapeople.org/repos/openstack/openstack-icehouse/rdo-release-icehouse-4.noarch.rpm</blockquote>
Lo siguiente que instalaremos serán los repositorios EPEL
<blockquote>yum install https://dl.fedoraproject.org/pub/epel/6Server/x86_64/epel-release-6-8.noarch.rpm</blockquote>
Instalaremos el paquete openstack-utils, que nos facilitara mucho la configuración de nuestro Openstack
<blockquote>yum install openstack-utils</blockquote>
Instalaremos SElinux para Openstack, que contiene una politicas SElinux acorde con un sistema en la nube
<blockquote>yum install openstack-selinux</blockquote>
Actualizamos todos los paquetes del sistema para tener la ultima versión y con errores corregidos
<blockquote>yum upgrade</blockquote>
Reiniciamos el sistema
<blockquote>reboot</blockquote>
Ya tendríamos todos los repositorios necesarios para continuar con la instalación de los nodos.

Un saludo