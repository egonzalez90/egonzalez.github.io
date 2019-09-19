--- layout: post title: Instalacion Active Directory Server 2012 Core
date: 2014-03-08 16:19:51.000000000 +01:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Various tags:
- '2012' - active directory - configuraccion - dominio - instalacion -
server core - usuarios - windows server meta: \_edit_last: '2'
\_login_radius_meta: a:1:{s:7:"sharing";i:0;} snap_isAutoPosted: '1'
\_thumbnail_id: '356' ac_featured_article: '' ac_show_post_thumbnail: ''
snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW: N;
kopa_resolution_total_view: '3' post_views_count: '0'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568669365;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:481;}i:1;a:1:{s:2:"id";i:186;}i:2;a:1:{s:2:"id";i:635;}}}}
dsq_thread_id: '6098558673' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/instalacion-active-directory-server-2012-core/" ---

En esta entrada vamos a configurar un Server 2012 Core de forma basica,
ademas instalaremos y configuraremos un sistema de Directorio Activo con
grupos, usuarios, horarios de acceso y perfiles moviles

` <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png>`__\ Lo
primero que haremos será configurar la red y el nombre del equipo.

Para ello abriremos el PowerShell

`Captura <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png>`__

Una vez en el powershell, pondremos sconfig para abrir el configurador
del sistema

`Captura0.1 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.12.png>`__

Aquí vemos como está configurado actualmente el sistema.

`Captura0.2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.22.png>`__

Elegiremos la opción 2 para cambiar el nombre al equipo, lo escribimos y
pulsamos intro

`Captura0.3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.32.png>`__

Ahora vemos como está el nombre del equipo cambiado, lo siguiente será
configurar la red, para ello pondremos la opción 8

`Captura0.4 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.42.png>`__

Esto nos mostrara esta imagen, en la que vemos las tarjetas de red que
tenemos disponibles, pondremos la opción 10, que es la de nuestra
tarjeta de red

`Captura0.5 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.52.png>`__

Esto abrirá la información de nuestra tarjeta de red

`Captura0.6 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.62.png>`__

Ahora configuraremos la red con nuestras direcciones IP, para ello
seleccionaremos la opción 1.

Aquí pondremos la opción s para seleccionar una IP estática, lo
siguiente será poner la dirección IP, mascara de red, y puerta de enlace

`Captura0.7 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.72.png>`__

A continuación seleccionaremos la opción 2 para establecer un servidor
DNS, nosotros pondremos el servidor DNS de google

`Captura0.8 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.82.png>`__

Ahora vemos como queda configurada nuestra tarjeta de red

Volveremos al menú principal con la opción 4.

`Captura0.9 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.92.png>`__

Instalación Active Directory
============================

Ahora procederemos a la instalación del directorio activo.

Para ello pondremos el comando Get-WindowsFeature, con el que cargara
los roles del sistema disponible

`Captura2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura22.png>`__

 

.. _section-1:

Después utilizaremos el comando Install-WindowsFeature –name
AD-Domain-Services, con el que indicaremos que instale el rol de
Directorio activo

`Captura3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura32.png>`__

Cuando acaben los procesos anteriores, utilizaremos el siguiente comando
para instalar las herramientas de administración de directorio activo

El comando es el siguiente Install-WindowsFeature –name
AD-Domain-Services -IncludeManagementTool

`Captura4 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura42.png>`__

Ahora utilizaremos el commando Get-command –module ADDSDeployment para
adquirir este módulo de uso del directorio activ

`Captura5 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura52.png>`__

Posteriormente importaremos este módulo a la configuración de nuestro
directorio activo mediante el comando Import-Module ADDSDeployment

`Captura6 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura62.png>`__

Finalmente instalaremos el bosque del dominio mediante el comando
Install-ADDSForest

`Captura7 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura72.png>`__

Aquí nos solicitara que indiquemos el nombre del dominio, después
pondremos la contraseña de administrador del dominio.

Lo siguiente que hará será solicitarnos que reiniciemos el equipo para
aplicar los cambios, pulsamos Y para aceptarlo

`Captura8 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura82.png>`__

Ahora cuando volvamos a iniciar el equipo, veremos que delante del
nombre del usuario, nos aparece el nombre del dominio, esto indica que
se ha creado correctamente este dominio

`Captura9 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura92.png>`__

Usuarios y grupos
=================

Ahora lo siguiente que tenemos que hacer es crear los grupos del
dominio.

Se hace mediante el comando net localgroup Nombregrupo /add /domain

Observamos que he creado los tres grupos necesarios

`Captura <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura11.png>`__

`Captura <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura12.png>`__

 

Ahora con este comando comprobamos que están los grupos creados
correctamente.

 

Es este comando: net localgroup

`Captura2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura23.png>`__

Ahora procederemos a crear los usuarios, se hace mediante el comando net
user Nombreusuario contraseña /add /domain

Vemos como aquí creo los usuarios de Informática

`Captura3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura33.png>`__
`Captura4 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura43.png>`__
`Captura5 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura53.png>`__

Para comprobar que los usuarios se han creado correctamente lo hacemos
mediante el comando net user

`Captura6 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura63.png>`__

Para añadir los usuarios a los grupos utilizaremos el comando net
localgroup nombregrupo nombres de usuarios /add

`Captura7 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura73.png>`__

Vemos los usuarios de informática dentro de su grupo

`Captura8 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura83.png>`__

Ahora vemos los usuarios de Contabilidad dentro de su propio grupo

`Captura9 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura93.png>`__

En esta otra captura vemos a los usuarios de Marketing dentro del grupo

`Captura10 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura101.png>`__

Horarios
========

Ahora nos pondremos a indicarle restricciones de acceso a los usuarios
al sistema en determinadas ocasiones.

Para ello utilizaremos el comando net user nombreusuario
/time:Dia1-Dia2,horainicio-horafin

Aquí vemos las restricciones de uso a los usuarios de informática

`Captura <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura13.png>`__
`Captura2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura24.png>`__
`Captura3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura34.png>`__

Ahora si utilizamos el comando net user nombreusuario, veremos como en
su perfil tienen puestos los horarios adecuadamente.

`Info
Contabilidad <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Contabilidad.png>`__
`Info
Informatica <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Informatica.png>`__

`Info
Marketing <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Marketing.png>`__

Perfiles Móviles
================

Ahora estableceremos perfiles móviles a un usuario de cada grupo.

Lo haremos mediante el comando net user nombreusuario /profilepath:ruta
carpeta

`Captura <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura14.png>`__

Previamente habíamos creado la carpeta Profiles dentro de C:

`Carpeta
profiles <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Carpeta-profiles.png>`__

 

Ahora en el servidor vemos como se han creado las carpetas de cada
perfil móvil una vez se han logeado en el sistema desde uno de los
equipos dentro del dominio

`Captura3 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura35.png>`__

Con esto ya estaría creado el directorio activo y configurado de forma
básica el servidor 2012 en Core
