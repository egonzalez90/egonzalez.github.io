---
id: 616
title: Añadir repositorios EPEL RHEL y CentOS
date: 2014-09-09T15:32:52+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=616
permalink: /anadir-repositorios-epel-rhel-y-centos/
kopa_resolution_total_view:
  - "3"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snap_isAutoPosted:
  - "1"
snapTW:
  - N;
image: /wp-content/uploads/2014/08/IMG_811278467062542.jpeg
categories:
  - Linux
tags:
  - añadir
  - centos
  - descargar
  - enablerepo
  - epel
  - fedoraproject
  - instalar
  - red hat
  - repolist
  - repositorios
  - rhel
---
Primero descargaremos el repositorio para nuestra versión de CentOS o RHEL mediante wget.

A continuacion instalaremos el paquete que habiamos descargado con rpm.

Esta son las diferentes versiones de CentOS y RHEL
<blockquote>## RHEL/CentOS 7 64-Bit ##
# wget http://mirror.rackcentral.com.au/epel/7/x86_64/epel-release-7-1.noarch.rpm
# rpm -ivh epel-release-7-0.2.noarch.rpm</blockquote>
&nbsp;
<blockquote>## RHEL/CentOS 6 32-Bit ##
# wget http://mirror.rackcentral.com.au/epel/6/i386/epel-release-6-8.noarch.rpm
# rpm -ivh epel-release-6-8.noarch.rpm</blockquote>
&nbsp;
<blockquote>## RHEL/CentOS 6 64-Bit ##
# wget http://mirror.rackcentral.com.au/epel/6/x86_64/epel-release-6-8.noarch.rpm
# rpm -ivh epel-release-6-8.noarch.rpm</blockquote>
Lo siguiente que haremos sera comprobar que esta en la lista de repositorios mediante este comando
<blockquote>yum repolist</blockquote>
Por ultimo habilitaremos el repositorio, para que podamos usarlo habitualmente
<blockquote>yum --enablerepo=epel</blockquote>