---
id: 612
title: 'Reiniciar &#8220;quota count&#8221; incorrecto Openstack'
date: 2014-09-07T15:50:41+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=612
permalink: /reiniciar-quota-count-incorrecto-openstack/
kopa_resolution_total_view:
  - "5"
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
image: /wp-content/uploads/2014/09/openstack-logo_0.png
categories:
  - OpenStack
tags:
  - bbdd
  - cloud
  - count
  - cuenta
  - cuota
  - error
  - ID
  - incorrecto
  - nova
  - openstack
  - quota
  - reinicio
  - reset
  - tenant
  - usage
---
<p class="prettyprint">Para reiniciar quota count, deberemos conectarnos a la base de datos y establecer in_use en "-1"</p>

<blockquote>mysql -u nova -p&lt;password&gt; nova

select*from quota_usages;

update quota_usages set in_use='-1'where project_id='&lt;my project id&gt;';</blockquote>
A partir de la versión Icehouse, ya no se usa -1 y se pasa a usar 0
<blockquote>update quota_usages set in_use='0'where project_id='&lt;my project id&gt;';</blockquote>