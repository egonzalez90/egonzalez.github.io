Title: Paquetes de Openstack
Date: 2014-11-09 16:20
Author: egongu90
Category: OpenStack
Tags: cloud, epel, necesarios, openstack, paquetes, rdo, repositorios
Slug: paquetes-de-openstack
Status: published

Esta instalación de paquetes deberemos hacerla en todos los nodos de
Openstack(Controller,Network y Compute)

Primero instalaremos yum-plugin-priorities con el que podremos cambiar
la prioridad de los repositorios

> yum install yum-plugin-priorities

A continuación instalaremos el rpm con los repositorios RDO

> yum
> install https://repos.fedorapeople.org/repos/openstack/openstack-icehouse/rdo-release-icehouse-4.noarch.rpm

Lo siguiente que instalaremos serán los repositorios EPEL

> yum
> install https://dl.fedoraproject.org/pub/epel/6Server/x86\_64/epel-release-6-8.noarch.rpm

Instalaremos el paquete openstack-utils, que nos facilitara mucho la
configuración de nuestro Openstack

> yum install openstack-utils

Instalaremos SElinux para Openstack, que contiene una politicas SElinux
acorde con un sistema en la nube

> yum install openstack-selinux

Actualizamos todos los paquetes del sistema para tener la ultima versión
y con errores corregidos

> yum upgrade

Reiniciamos el sistema

> reboot

Ya tendríamos todos los repositorios necesarios para continuar con la
instalación de los nodos.

Un saludo
