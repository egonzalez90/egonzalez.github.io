--- layout: post title: 'Fix Bash (ShellShock) en diferentes SO: Debian,
RHEL y Solaris' date: 2014-10-01 17:20:52.000000000 +02:00 type: post
parent_id: '0' published: true password: '' status: publish categories:
- Linux - OpenStack - Various tags: - actualizar - bash - bug - centos -
Debian - fix - oracle - red hat - rhel - shellshock - solaris meta:
\_edit_last: '2' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_thumbnail_id: '526' \_wpas_done_all: '1'
\_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1' \_wpas_skip_8706018:
'1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568283897;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:616;}i:1;a:1:{s:2:"id";i:743;}i:2;a:1:{s:2:"id";i:731;}}}}
author: login: egongu90 email: egongu90@hotmail.com display_name: Editor
first_name: '' last_name: '' permalink:
"/fix-bash-shellshock-en-diferentes-so-debian-rhel-y-solaris-shellshock/"
---

Veremos la forma de instalar los parches de Bash en diferentes sistemas
Linux

Debian 6
========

Primero deberemos añadir el repositorio LTS. Lo haremos añadiendo esta
línea a el archivo siguiente archivo

   vi /etc/apt/sources.list/

..

   deb http://ftp.us.debian.org/debian squeeze-lts main non-free contrib

A continuación importaremos la clave del servidor de Debian

   gpg --keyserver pgpkeys.mit.edu --recv-key 8B48AD6246925553

La exportaremos y añadiremos para que al actualizar la reconozca, es
posible que estos pasos no sean necesarios, pero normalmente suele dar
el error de la clave

   gpg -a --export 8B48AD6246925553 \| apt-key add –

A partir de aquí será lo igual que con Debian 7

Debian 7
========

Actualizaremos la lista de repositorios

   apt-get update

Lo siguiente es actualizar solo el paquete bash

   apt-get install --only-upgrade bash

RHEL-CentOS 5, 6 y 7
====================

Directamente actualizando el paquete bash

   yum update bash

O instalándolo desde el paquete .rpm disponible en la página de RHEL, o
en los repositorios de CentOS, Scientific Linux, etc

   rpm –Uvh paquetebash.rpm

Puedes comprobar que esta la ultima versión instalada viendo la fecha y
la versión del paquete mediante

   rpm –qi bash

Oracle Linux 6
==============

En Oracle Linux primero deberemos añadir los repositorios de paquetes
públicos, para ello iremos a la siguiente ruta.

   cd /etc/yum.repos.d

A continuación descargaremos el repositorio público dentro de la misma
carpeta:

    wget http://public-yum.oracle.com/public-yum-ol6.repo

Por ultimo actualizaremos bash a su última versión disponible

   yum update bash
