--- layout: post title: Paquetes de Openstack date: 2014-11-09
16:20:27.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - cloud -
epel - necesarios - openstack - paquetes - rdo - repositorios meta:
\_edit_last: '2' \_thumbnail_id: '615' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_wpas_skip_5226565: '1'
\_wpas_skip_4949654: '1' \_wpas_skip_8706018: '1' \_wpas_skip_10228321:
'1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567144582;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:866;}i:1;a:1:{s:2:"id";i:616;}i:2;a:1:{s:2:"id";i:816;}}}}
dsq_thread_id: '6177880549' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/paquetes-de-openstack/" ---

Esta instalación de paquetes deberemos hacerla en todos los nodos de
Openstack(Controller,Network y Compute)

Primero instalaremos yum-plugin-priorities con el que podremos cambiar
la prioridad de los repositorios

   yum install yum-plugin-priorities

A continuación instalaremos el rpm con los repositorios RDO

   yum
   install https://repos.fedorapeople.org/repos/openstack/openstack-icehouse/rdo-release-icehouse-4.noarch.rpm

Lo siguiente que instalaremos serán los repositorios EPEL

   yum
   install https://dl.fedoraproject.org/pub/epel/6Server/x86_64/epel-release-6-8.noarch.rpm

Instalaremos el paquete openstack-utils, que nos facilitara mucho la
configuración de nuestro Openstack

   yum install openstack-utils

Instalaremos SElinux para Openstack, que contiene una politicas SElinux
acorde con un sistema en la nube

   yum install openstack-selinux

Actualizamos todos los paquetes del sistema para tener la ultima versión
y con errores corregidos

   yum upgrade

Reiniciamos el sistema

   reboot

Ya tendríamos todos los repositorios necesarios para continuar con la
instalación de los nodos.

Un saludo
