--- layout: post title: Openstack multinodo - Guia Básica date:
2014-10-19 16:25:49.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - centos - completa - icehouse - instalacion - multinodo -
openstack - red hat meta: \_edit_last: '2' \_thumbnail_id: '615'
\_publicize_facebook_user: https://www.facebook.com/dudu.gonzalez90
\_publicize_twitter_user: "@hidanstillalive" \_wpas_done_all: '1'
\_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1' \_wpas_skip_9011406:
'1' \_wpas_skip_8706018: '1' \_wpas_skip_10228321: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567376753;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:577;}i:1;a:1:{s:2:"id";i:790;}i:2;a:1:{s:2:"id";i:809;}}}}
dsq_thread_id: '6174004371' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink:
"/openstack-multinodo-escalable-controller-network-y-compute1/" ---

Inicio un proyecto nuevo en el blog en el que configuraremos nuestro
Cloud en Openstack Icehouse con una arquitectura de 2 nodos, dicha
instalación va a llevar el siguiente orden, con el que configuraremos
los principales componentes de Openstack.

#. `Configuración de red
   básica <http://egonzalez.org/configuracion-de-red-basica-openstack/>`__
#. `Pre-requisitos <http://egonzalez.org/pre-requisitos-openstack/>`__
#. `MySQL <http://egonzalez.org/mysql/>`__
#. `Paquetes de
   Openstack <http://egonzalez.org/paquetes-de-openstack/>`__
#. `Servidor de mensajes
   Qpid <http://egonzalez.org/servidor-de-mensajes-qpid/>`__
#. Keystone

   #. `Instalacion <http://egonzalez.org/816/>`__
   #. `Usuarios, tenants y
      roles <http://egonzalez.org/usuarios-tenants-y-roles/>`__
   #. `Servicios y
      endpoints <http://egonzalez.org/keystone-api-endpoint/>`__
   #. `Comprobacion <http://egonzalez.org/comprobar-keystone/>`__

#. `Clientes de Openstack <http://egonzalez.org/openstack-clients/>`__
#. Glance

   #. `Instalacion <http://egonzalez.org/configuracion-de-image-service-glance/>`__
   #. `Comprobación <http://egonzalez.org/comprobar-glance-image-service/>`__

#. Nova

   #. `Nova en Controller
      Node <http://egonzalez.org/nova-en-controller-node/>`__
   #. Nova en Compute Node

#. Legacy Network
#. Dashboard
#. Instancias

| Esta página será el menú principal de la instalación, en ella iré
  publicando los enlaces de los módulos configurados.
| Esta instalación se irá actualizando periódicamente hasta acabar por
  completo con todas las configuraciones necesarias.
