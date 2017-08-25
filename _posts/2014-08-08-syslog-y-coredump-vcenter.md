---
id: 545
title: Syslog y coredump vCenter
date: 2014-08-08T16:55:09+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=545
permalink: /syslog-y-coredump-vcenter/
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
categories:
  - Virtualizacion
tags:
  - cloud
  - collector
  - coredump
  - esxi
  - log
  - syslog
  - vcenter
  - virtualizacion
  - vmware
---
Vamos a configurar syslog y coredump de los host ESXi para que un vCenter recoja los logs de estos host

Primero deberemos tener instaladas y configuradas en el vCenter estas aplicaciones:

Dump Collector y Syslog collector.

Para configurar el Syslog
# esxcli system syslog config set --loghost="IPHOST"
# esxcli system syslog reload

Para configurar el Coredump
# esxcli system coredump network set --interface-name vmk0 --server-ipv4 "IPHOST"
# esxcli system coredump network set --enable true
# esxcli system coredump network get ( para comprobar que todo ok )
--interface-name vmkX Hay que ver por que vmk ve la red de gestión

Estos comandos habría que ejecutarlos por cada host ESXi que queramos que envié los logs al vCenter

&nbsp;

Un saludo y espero que sea de ayuda