--- layout: post title: Solución fallo VirtualBox en Fedora 19 date:
2013-11-13 18:00:14.000000000 +01:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Linux tags: -
error - fedora 19 - linux - maquina virtual - solucion - Virtualbox -
virtualizacion - VM meta: \_publicize_pending: '1'
publicize_facebook_url: https://facebook.com/10201630879271416
\_wpas_done_5226565: '1' \_publicize_done_external:
a:1:{s:8:"facebook";a:1:{i:1161837279;b:1;}} publicize_twitter_user:
suicidezombiie publicize_twitter_url: http://t.co/FSbdnIaLv0
\_wpas_done_4949654: '1' publicize_tumblr_url:
http://suicidezombiie.tumblr.com.tumblr.com/post/66884427381
\_wpas_done_5226570: '1' \_wpas_skip_5226565: '1' \_wpas_skip_4949654:
'1' \_wpas_skip_5226570: '1' \_wpas_mess: Solución fallo VirtualBox en
Fedora 19 http://wp.me/p3476y-3i \_edit_last: '2' \_layout: inherit
\_login_radius_meta: a:1:{s:7:"sharing";i:0;} snap_MYURL: '' snapEdIT:
'1' snapFB: N; snapTW: N; \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568927713;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:97;}i:1;a:1:{s:2:"id";i:295;}i:2;a:1:{s:2:"id";i:527;}}}}
dsq_thread_id: '6127711605' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/solucion-fallo-virtualbox-en-fedora-19/" ---

| Mucha gente ha tenido problemas a la hora de abrir una maquina virtual
  en VirtualBox con Fedora 19, suele salir un error de compilación de
  VBox que por mucho que lo recompiles no se soluciona si no sigues los
  pasos previos que voy a explicar.
| En primer lugar deberías de desinstalar VirtualBox completamente, doy
  por hecho de que si lo has instalado también sabrás desinstalarlo.
| A continuación deberías de actualizar los paquetes del sistema, esto
  no es necesario, pero siempre recomendable por motivos de seguridad.Se
  hace mediante este comando:

::

   # yum -y upate

 

Después instalamos datos del kernel

::

   # yum -y install kernel-headers kernel-devel dkms gcc

 

Ahora vamos a la carpeta de repositorios de fedora

::

   # cd /etc/yum.repos.d

 

Ahora creamos/modificamos este archivo

::

   # vi virtualbox.repo

 

Se rellena con la siguiente información:

::

                  [virtualbox]
   name=Fedora$releasever - $basearch - VirtualBox
   baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/$releasever/$basearch
   enabled=1
   gpgcheck=1
   gpgkey=http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc

Guardamos y salimos de este archivo

Ahora instalamos VirtualBox

::

   # yum -y install VirtualBox-4.2

 

Ahora ejecutamos este comando para configurar VirtualBox

::

   # /etc/init.d/vboxdrv setup

 

Ahora añadimos nuestro usuario al grupo que tiene permisos para usar
VirtualBox

::

   # usermod -G vboxusers -a "NombredeUsuario"

Esto debería permitirnos crear maquinas virtuales y abrirlas ya
