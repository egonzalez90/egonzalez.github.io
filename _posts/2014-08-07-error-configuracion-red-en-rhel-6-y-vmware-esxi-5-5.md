---
id: 541
title: Error configuración red en RHEL 6 y VMware ESXi 5.5
date: 2014-08-07T16:49:14+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=541
permalink: /error-configuracion-red-en-rhel-6-y-vmware-esxi-5-5/
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
categories:
  - Linux
  - Virtualizacion
tags:
  - "5.5"
  - 70-persistent-net.rules
  - clon
  - clondado
  - daemon
  - esxi
  - eth0
  - ifcfg-eth
  - linux
  - network
  - network manager
  - nic
  - nm_controlled
  - red hat
  - rhel6
  - sysadmin
  - virtualizacion
  - vmware
  - vmxnet3
---
Ultimamente, desde que hemos empezado a trabajar mas con RHEL 6, nos dimos cuenta que tras el clonado de las VM, las interfaces de red no se configuraban bien.

Primero vimos que las MAC de la eth, no se asignaban correctamente, y despues comprobamos que una vez configuradas al hacer reboot o reinicio de la red, estas se configuraban como les daba la gana y perdias la configuracion e internet.

Pues bien, tras un proceso de investigacion llege a la solucion( o al menos en nuestro sistema), los pasos son los siguientes:

-Quitar las NIC de la antigua configuracion

-Añadir las NIC en vmxnet3 en el vCenter igual que estaban configuradas anteriormente

-Borrar el archivo /etc/udev/rules.d/70-persistent-net.rules

-Configurar los archivos /etc/sysconfig/network-scripts/ifcfg-eth* añadiendo la linea entre su configuracion

<strong>NM_CONTROLLED=no</strong>

-Parar el servicio NetworkManager y deshabilitarlo del arranque

<strong>service NetworkManager stop</strong>

<strong>chkconfig NetworkManager off</strong>

-Habilitar el servicio network en arranque(puede que ya lo esté)

<strong>chkconfig network on</strong>

-Instalar las vmtools

-Reiniciar la maquina y comprobar que no cambia la configuración entre el inicio del sistema y tras service network restart

&nbsp;

Bien, el problema que había, es que por algún error, el network manager se hacia con el control de la red y daba errores con el demonio network, lo que hacemos para solucionarlo es, borrar el archivo de la configuración de las tarjetas,configurar las eth deshabilitando el control por el Network manager y después deshabilitar Network Manager del sistema.

De este modo nos funciona sin ningun problema la red.

Espero haber ayudado, un saludo