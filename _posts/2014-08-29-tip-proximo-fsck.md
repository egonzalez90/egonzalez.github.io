---
id: 607
title: 'TIP: Proximo fsck'
date: 2014-08-29T15:00:30+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=607
permalink: /tip-proximo-fsck/
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
post_views_count:
  - "1"
categories:
  - Linux
tags:
  - -l
  - /dev/sda1
  - filesystem check
  - fsck
  - intervalo
  - linux
  - proximo
  - tip
  - tune2fs
---
<blockquote>tune2fs -l /dev/dispositivo*</blockquote>
*dispositivo puede ser sda1, sda2, sdb1, etc

Entre los datos que te muestra el comando, puedes ver el intervalo de chequeo del fs, ultimo fsck, la cuenta de las veces montado y el máximo de las veces montado el fs hasta que se haga un fsck

&nbsp;