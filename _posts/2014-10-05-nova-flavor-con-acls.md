---
id: 718
title: Nova flavor con control de acceso
date: 2014-10-05T17:47:42+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=718
permalink: /nova-flavor-con-acls/
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - acceso
  - acl
  - cloud
  - control
  - flavor
  - flavor_id
  - flavor-access-add
  - flavor-create
  - list
  - nova
  - openstack
  - tenant_id
---
Primero crearemos un "flavor"(sabor) mediante es siguiente comando, este sabor le haremos privado mediante la opción --is-public=False, un ID 23, con 4vCPU y 4 GB de RAM.<!--more-->
<pre style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;"><span style="font-size: 11px;">$ nova flavor-create 4vCPU-4GB_Mem 23 4096 0 4 --is-public=False
+----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
| ID | Name           | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
| 23 | 4vCPU-4GB_Mem  |  4096     | 0    | 0         |      |     4 | 1.0         |     False |
+----+----------------+-----------+------+-----------+------+-------+-------------+-----------+</span></pre>
A continuación buscaremos el tenant_ID del tenant al que queramos asignar el sabor, en este caso el tenant(previamente creado) es prueba
<pre style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;">$ keystone tenant-list | grep prueba
| 41a0db24bc8940b<wbr />6a2f3297bef5f6c<wbr />ee | prueba | True |
</pre>
Con el tenant_ID y el flavor_ID, asignaremos el flavor a el tenant, lo haremos mediante el siguiente comando:
<ul>
	<li>23 es flavor_ID</li>
	<li>41a0db24bc8940b6a2f3297bef5f6cee es tenant_ID</li>
</ul>
<pre style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;">$ nova flavor-access-add 23 41a0db24bc8940b6a2f3297bef5f6cee
+-----------+----------------------------------+
| Flavor_ID | Tenant_ID                        |
+-----------+----------------------------------+
|        23 | 41a0db24bc8940b6a2f3297bef5f6cee |
+-----------+----------------------------------+</pre>
Por ultimo comprobaremos la lista de sabores, aqui veremos como el flavor no es publico,  y debería de estar solo disponible para el tenant asignado anteriormente
<pre style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;">$ nova flavor-list
<span style="font-size: 11px;">+----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
| ID | Name            | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
| 23 | 4vCPU-4GB_Mem   | 4096      | 0    | 0         |      | 4     | 4.0         | False     |
+----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+</span></pre>
<span style="font-size: 14px; line-height: 22.3999996185303px;">La información sacada para este post viene de este blog (en ingles), visitarle si tenéis ocasión: <a href="http://blog.aaronorosen.com/nova-flavors-with-access-control/" target="_blank">http://blog.aaronorosen.com/nova-flavors-with-access-control/</a></span>