---
id: 577
title: Componentes de OpenStack
date: 2014-08-27T16:41:58+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=577
permalink: /componentes-de-openstack/
kopa_resolution_total_view:
  - "8"
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
post_views_count:
  - "1"
image: /wp-content/uploads/2014/08/openstack-logo512-672x372.png
categories:
  - OpenStack
tags:
  - basico
  - cinder swift
  - cloud
  - componentes
  - computing
  - horizon
  - introducion
  - keystone
  - neutron
  - nova
  - openstack
---
Desde su aparición en  2010, la comunidad de Openstack ha estado añadiendo nuevos componentes y funcionalidades.

A día de hoy estos son los componentes oficiales de OpenStack
<table width="85%">
<tbody>
<tr>
<td><strong>Servicio</strong></td>
<td><strong>Componente</strong></td>
<td><strong> Descripcion</strong></td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Dashboard</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Horizon</a></td>
<td>&nbsp;

Interfaz gráfica que permite interactuar con Openstack para la administración básica del servicio

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Compute</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Nova</a></td>
<td>&nbsp;

Encargada de la computación de la nube, gestiona y automatiza los recursos. Es la parte principal de OpenStack

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Networking</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Neutron</a></td>
<td>&nbsp;

Gestiona la red y la asignación de IPs a las diferentes instancias

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Object Storage</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Swift</a></td>
<td>&nbsp;

Proporciona un Sistema de almacenamiento redundado y escalable. No es persistente el almacenamiento

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Block Storage</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Cinder</a></td>
<td>&nbsp;

Proporciona un almacenamiento en bloque persistente

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Identity service</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Keystone</a></td>
<td>&nbsp;

Servicio de autenticación y autorización de Openstack

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Image Service</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Glance</a></td>
<td>&nbsp;

Openstack utiliza este servicio para el uso de las imagines de disco durante la asignación de instancias

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Telemetry</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Ceilometer</a></td>
<td>&nbsp;

Monitorización para facturación con el cliente

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Orchestration</a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Heat</a></td>
<td>&nbsp;

Permite la orquestación de diferentes aplicaciones basadas en la nube, tales como AWS, etc.

&nbsp;</td>
</tr>
<tr>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Database </a></td>
<td><a href="http://docs.openstack.org/admin-guide-cloud/content/ch_getting-started-with-openstack.html">Trove</a></td>
<td>&nbsp;

Una base de datos escalable para el uso de DBaaS

&nbsp;</td>
</tr>
</tbody>
</table>