--- layout: post title: Pre-requisitos Openstack date: 2014-10-26
16:43:07.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - basico -
cloud - firewalld - instalacion - iptables - network - network manager -
ntp - openstack - prerequisitos - server meta: \_edit_last: '2'
\_thumbnail_id: '615' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_wpas_skip_5226565: '1'
\_wpas_skip_4949654: '1' \_wpas_skip_8706018: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568413057;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:932;}i:1;a:1:{s:2:"id";i:809;}i:2;a:1:{s:2:"id";i:802;}}}}
dsq_thread_id: '6128274510' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/pre-requisitos-openstack/" ---

NTP
===

Deberemos tener instalado NTP en todos los nodos.

   yum install ntp

A continuacion tenemos que configurar los nodos para que usen NTP del
nodo controller

   vi /etc/ntp.conf

Editamos la linea server para que aparezca lo siguiente

   server controller iburst

En el nodo controller borramos las opciones nopeer y noquery de las
lineas restrict

Por ultimo iniciaremos el servicio y el nivel de ejecución en el
arranque del sistema

   service ntpd start

   chkconfig ntpd on

Servicios de red
================

Deshabilitamos NetworkManager y habilitamos el servicio network, asi
como quitamos y establecemos el nivel de ejecución a cada servicio
respectivamente

   service NetworkManager stop

   service network start

   chkconfig NetworkManager off

   chkconfig network on

Servicios cortafuegos
=====================

Paramos y deshabilitamos firewalld por defecto y activamos e iniciamos
iptables. Es posible que no tengas instalado firewalld, por lo que no
tendrás que deshabilitarlo

   service firewalld stop

   service iptables start

   chkconfig firewalld off

   chkconfig iptables on

Estos son los prerequisitos necesarios para iniciar la instalación de un
entorno con Openstack

Un saludo
