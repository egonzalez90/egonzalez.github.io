---
id: 600
title: Alineamiento MBR maquinas virtuales
date: 2014-09-03T15:21:58+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=600
permalink: /alineamiento-mbr-maquinas-virtuales/
kopa_resolution_total_view:
  - "18"
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
post_views_count:
  - "4"
categories:
  - Linux
  - Virtualizacion
tags:
  - alinear
  - esxi
  - ext3
  - ext4
  - grub
  - maquina virtual
  - mbr
  - mbralign
  - mbrscan
  - netapp
  - redhat
  - rhel
  - VM
  - vmfs
  - vmware
  - volumes
---
Antes de la llegada de el sistema de ficheros EXT4, cuando creabas maquinas virtuales, estas estaban desalineadas el mbr del vmfs y de el almacenamiento,  lo que generaba menor rendimiento.<!--more-->

Para ello dedico esta entrada, con la que mostrare como alinear el mbr.

Lo primero que necesitaremos es el paquete con las tools mbrscan y mbralign, este paquete le copiaremos a el directorio /opt/ontap/ de un host ESXi que tenga acceso al almacenamiento donde tenemos la maquina guardada.

Una vez copiado el paquete a dicho directorio pasaremos a escanear y a realinear el mbr de la maquina, para ello necesitamos que este apagada.

Una vez apagada iremos al directorio /opt/ontap/ y ejecutaremos el siguiente comando con el que analizaremos el disco de la maquina para ver si necesita ser alineado.
<blockquote>./mbrscan /vmfs/volumes/ALMACENAMIENTO/maquinavirtual/maquinavirtual-flat.vmdk</blockquote>
Esto nos mostrara un mensaje en el que pondra:
<blockquote>Aligned yes o Aligned no</blockquote>
En el caso de que pusiera align no, deberemos realinear el mbr de la maquina, lo haremos mediante este comando:
<blockquote>./mbralign /vmfs/volumes/ALMACENAMIENTO/maquinavirtual/maquinavirtual-flat.vmdk</blockquote>
Esto nos creara un archivo .bak del disco que vamos a alinear por si fallara este proceso poder recuperarlo, este proceso tardara bastante(dependiendo del tamaño del disco)

Una vez acabado ese proceso de alineamiento, volveremos a utilizar el comando mbrscan para comprobar que este bien hecho.

Por ultimo, el alineado del mbr se carga totalmente el GRUB de la maquina, por lo que deberemos recuperarlo.

En esta entrada tienes como hacerlo: <a title="Recuperar GRUB RHEL y CentOS" href="http://egonzalez.org/recuperar-grub-rhel-y-centos/ " target="_blank"><span id="sample-permalink" style="color: #666666;" tabindex="-1">http://egonzalez.org/<span id="editable-post-name" title="Enlace permanente temporal. Haz clic para editar esta parte.">recuperar-grub-rhel-y-centos</span>/</span><span style="color: #666666;"> </span></a>

Una vez recuperado el GRUB y comprobado que la maquina funciona correctamente, borraremos el archivo .bak que se había creado.

Espero poder ayudar, un saludo