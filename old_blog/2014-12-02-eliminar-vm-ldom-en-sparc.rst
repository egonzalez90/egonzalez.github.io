--- layout: post title: Eliminar VM (LDOM) en SPARC date: 2014-12-02
14:51:11.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Virtualizacion tags: -
eliminar - ldm list - ldm remove - ldom - list-bindings - oracle -
quitar - remove - solaris - sparc - VM meta: \_edit_last: '2'
\_thumbnail_id: '853' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_wpas_skip_5226565: '1'
\_wpas_skip_4949654: '1' \_wpas_skip_8706018: '1' \_wpas_skip_10228321:
'1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568781861;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:559;}i:1;a:1:{s:2:"id";i:541;}i:2;a:1:{s:2:"id";i:527;}}}}
dsq_thread_id: '6108527150' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/eliminar-vm-ldom-en-sparc/" ---

Primero comprobaremos que maquinas tenemos y el estado de ellas

   ldm list

A continuación, si la maquina que queremos borrar esta encendida la
apagaremos

   ldm stop LDOM

 

Lo siguiente será quitar la consola de la maquina

   ldm unbind LDOM

Listaremos la configuración de la maquina y buscaremos los discos que
tenga asignados, normalmente está al final del archivo

   ldm list-bindings LDOM

Quitaremos el controlador del disco de la maquina

   ldm remove-vdiskserverdevice VOLUMEN@LDOM

Eliminaremos el disco de la configuración de la maquina

   ldm remove-vdisk DISKNAME LDOM

Eliminamos las NIC

   ldm remove-vnet NIC_NAME LDOM

Borramos VDS

   ldm remove-vds LDOM

Eliminamos configuración de la maquina

   ldm remove-domain LDOM

Borramos los datos de la maquina, esto se hace eliminando la carpeta
donde están las maquinas guardadas

   rm -R /ruta/carpeta/LDOM/
