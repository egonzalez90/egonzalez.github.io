---
id: 605
title: Montar directorio NFS
date: 2014-09-05T15:46:24+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=605
permalink: /montar-directorio-nfs/
kopa_resolution_total_view:
  - "1"
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
  - centos
  - default
  - df -h
  - directorio
  - fstab
  - linux
  - montar
  - mount
  - nfs
  - red hat
  - rhel
---
Primero crearemos la carpeta en donde vamos a montar el directorio NFS
<blockquote>mkdir /rutadondemontareldirectorio</blockquote>
A continuación utilizaremos este comando para montar el directorio NFS en la carpeta creada anteriormente.

SERVIDOR puede ser tanto hostname como IP(yo siempre prefiero utilizar IP)
<blockquote>mount SERVIDOR:/ruta/a/la/carpeta /rutadondemontareldirectorio</blockquote>
Una vez montado sin darnos ningún error, utilizaremos este comando para comprobar que nos mostrara los directorios que están montados en nuestro sistema y que tamaño tienen
<blockquote>df -h</blockquote>
Ahora que ya hemos montado el directorio NFS, lo incluiremos en fstab para que se monte siempre en el arranque del sistema sin tener que hacerlo manualmente por los pasos anteriores, para ello modificaremos este archivo
<blockquote>vi /etc/fstab</blockquote>
Dentro del archivo incluiremos esta linea y guardaremos
<blockquote>SERVIDOR:/ruta/a/la/carpeta            /rutadondemontareldirectorio            default            0 0</blockquote>
Podemos comprobar que el archivo fstab funciona correctamente utilizando el mismo comando de antes para ver los directorios montados y su tamaño, pero esta vez lo haremos una vez encendida la maquina, sin haber montado el directorio NFS de forma manual
<blockquote>df -h</blockquote>