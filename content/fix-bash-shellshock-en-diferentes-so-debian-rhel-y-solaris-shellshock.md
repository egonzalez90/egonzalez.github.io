Title: Fix Bash (ShellShock) en diferentes SO: Debian, RHEL y Solaris
Date: 2014-10-01 17:20
Author: egongu90
Category: Linux, OpenStack, Various
Tags: actualizar, bash, bug, centos, Debian, fix, oracle, red hat, rhel, shellshock, solaris
Slug: fix-bash-shellshock-en-diferentes-so-debian-rhel-y-solaris-shellshock
Status: published

Veremos la forma de instalar los parches de Bash en diferentes sistemas
Linux<!--more-->

Debian 6
========

Primero deberemos añadir el repositorio LTS. Lo haremos añadiendo esta
línea a el archivo siguiente archivo

> vi /etc/apt/sources.list/

> deb http://ftp.us.debian.org/debian squeeze-lts main non-free contrib

A continuación importaremos la clave del servidor de Debian

> gpg --keyserver pgpkeys.mit.edu --recv-key 8B48AD6246925553

La exportaremos y añadiremos para que al actualizar la reconozca, es
posible que estos pasos no sean necesarios, pero normalmente suele dar
el error de la clave

> gpg -a --export 8B48AD6246925553 | apt-key add –

A partir de aquí será lo igual que con Debian 7

Debian 7
========

Actualizaremos la lista de repositorios

> apt-get update

Lo siguiente es actualizar solo el paquete bash

> apt-get install --only-upgrade bash

RHEL-CentOS 5, 6 y 7
====================

Directamente actualizando el paquete bash

> yum update bash

O instalándolo desde el paquete .rpm disponible en la página de RHEL, o
en los repositorios de CentOS, Scientific Linux, etc

> rpm –Uvh paquetebash.rpm

Puedes comprobar que esta la ultima versión instalada viendo la fecha y
la versión del paquete mediante

> rpm –qi bash

Oracle Linux 6
==============

En Oracle Linux primero deberemos añadir los repositorios de paquetes
públicos, para ello iremos a la siguiente ruta.

> cd /etc/yum.repos.d

A continuación descargaremos el repositorio público dentro de la misma
carpeta:

>  wget http://public-yum.oracle.com/public-yum-ol6.repo

Por ultimo actualizaremos bash a su última versión disponible

> yum update bash
