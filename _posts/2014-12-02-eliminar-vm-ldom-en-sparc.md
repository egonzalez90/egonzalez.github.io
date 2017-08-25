---
id: 852
title: Eliminar VM (LDOM) en SPARC
date: 2014-12-02T14:51:11+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=852
permalink: /eliminar-vm-ldom-en-sparc/
image: /wp-content/uploads/2014/12/Aktualne_logo_Oracle_Solaris_OS_OSos.png
categories:
  - Virtualizacion
tags:
  - eliminar
  - ldm list
  - ldm remove
  - ldom
  - list-bindings
  - oracle
  - quitar
  - remove
  - solaris
  - sparc
  - VM
---
Primero comprobaremos que maquinas tenemos y el estado de ellas
<blockquote>ldm list</blockquote>
A continuación, si la maquina que queremos borrar esta encendida la apagaremos
<blockquote>ldm stop LDOM</blockquote>
&nbsp;

Lo siguiente será quitar la consola de la maquina
<blockquote>ldm unbind LDOM</blockquote>
Listaremos la configuración de la maquina y buscaremos los discos que tenga asignados, normalmente está al final del archivo
<blockquote>ldm list-bindings LDOM</blockquote>
Quitaremos el controlador del disco de la maquina
<blockquote>ldm remove-vdiskserverdevice VOLUMEN@LDOM</blockquote>
Eliminaremos el disco de la configuración de la maquina
<blockquote>ldm remove-vdisk DISKNAME LDOM</blockquote>
Eliminamos las NIC
<blockquote>ldm remove-vnet NIC_NAME LDOM</blockquote>
Borramos VDS
<blockquote>ldm remove-vds LDOM</blockquote>
Eliminamos configuración de la maquina
<blockquote>ldm remove-domain LDOM</blockquote>
Borramos los datos de la maquina, esto se hace eliminando la carpeta donde están las maquinas guardadas
<blockquote>rm -R /ruta/carpeta/LDOM/</blockquote>