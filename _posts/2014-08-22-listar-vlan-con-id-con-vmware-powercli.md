---
id: 551
title: Listar vlan ID con VMware PowerCLI
date: 2014-08-22T15:59:41+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=551
permalink: /listar-vlan-con-id-con-vmware-powercli/
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
kopa_resolution_total_view:
  - "1"
categories:
  - Virtualizacion
tags:
  - all vlan
  - CLI
  - CSV
  - esxi
  - Excel
  - host
  - ID
  - list portgroup id
  - list vlan
  - listar
  - portgroup
  - powercli
  - todas vlan
  - virtualizacion
  - Vlan
  - vlan id
  - vmware
---
Para poder listar todas las VLans de un host ESXi con su ID primero nos deberemos conectar a ese host por PowerCLI, usaremos este comando:
<blockquote>Connect_VIServer -server "host" -user "usuario" -password "contraseña"</blockquote>
Una vez conectados a dicho ESXi, utilizaremos el siguiente comando con el que listaremos las vlans y los ID, ademas lo exportaremos a un formato CSV para poder analizarlo con Excel
<blockquote>Get-VirtualPortGroup -VMHost "Host" | Select Name, VirtualSwitch, VLanId | Export-Csv C:nombre.csv</blockquote>
Espero les sirva, un saludo