Title: Instalacion Active Directory Server 2012 Core
Date: 2014-03-08 16:19
Author: egongu90
Category: Various
Tags: 2012, active directory, configuraccion, dominio, instalacion, server core, usuarios, windows server
Slug: instalacion-active-directory-server-2012-core
Status: published

En esta entrada vamos a configurar un Server 2012 Core de forma basica,
ademas instalaremos y configuraremos un sistema de Directorio Activo con
grupos, usuarios, horarios de acceso y perfiles moviles

[<!--more-->](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png)Lo
primero que haremos será configurar la red y el nombre del equipo.

Para ello abriremos el PowerShell

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png)

Una vez en el powershell, pondremos sconfig para abrir el configurador
del sistema

[![Captura0.1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.12.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.12.png)

Aquí vemos como está configurado actualmente el sistema.

[![Captura0.2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.22.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.22.png)

Elegiremos la opción 2 para cambiar el nombre al equipo, lo escribimos y
pulsamos intro

[![Captura0.3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.32.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.32.png)

Ahora vemos como está el nombre del equipo cambiado, lo siguiente será
configurar la red, para ello pondremos la opción 8

[![Captura0.4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.42.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.42.png)

Esto nos mostrara esta imagen, en la que vemos las tarjetas de red que
tenemos disponibles, pondremos la opción 10, que es la de nuestra
tarjeta de red

[![Captura0.5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.52.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.52.png)

Esto abrirá la información de nuestra tarjeta de red

[![Captura0.6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.62.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.62.png)

Ahora configuraremos la red con nuestras direcciones IP, para ello
seleccionaremos la opción 1.

Aquí pondremos la opción s para seleccionar una IP estática, lo
siguiente será poner la dirección IP, mascara de red, y puerta de enlace

[![Captura0.7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.72.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.72.png)

A continuación seleccionaremos la opción 2 para establecer un servidor
DNS, nosotros pondremos el servidor DNS de google

[![Captura0.8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.82.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.82.png)

Ahora vemos como queda configurada nuestra tarjeta de red

Volveremos al menú principal con la opción 4.

[![Captura0.9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.92.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.92.png)

Instalación Active Directory {.western}
============================

Ahora procederemos a la instalación del directorio activo.

Para ello pondremos el comando Get-WindowsFeature, con el que cargara
los roles del sistema disponible

[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura22.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura22.png)

 

 {.western}

 {.western}

Después utilizaremos el comando Install-WindowsFeature –name
AD-Domain-Services, con el que indicaremos que instale el rol de
Directorio activo

[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura32.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura32.png)

Cuando acaben los procesos anteriores, utilizaremos el siguiente comando
para instalar las herramientas de administración de directorio activo

<span lang="en-US">El comando es el siguiente Install-WindowsFeature
–name AD-Domain-Services -IncludeManagementTool</span>

[![Captura4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura42.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura42.png)

Ahora utilizaremos el commando Get-command –module ADDSDeployment para
adquirir este módulo de uso del directorio activ

[![Captura5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura52.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura52.png)

Posteriormente importaremos este módulo a la configuración de nuestro
directorio activo mediante el comando Import-Module ADDSDeployment

[![Captura6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura62.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura62.png)

Finalmente instalaremos el bosque del dominio mediante el comando
Install-ADDSForest

[![Captura7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura72.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura72.png)

Aquí nos solicitara que indiquemos el nombre del dominio, después
pondremos la contraseña de administrador del dominio.

Lo siguiente que hará será solicitarnos que reiniciemos el equipo para
aplicar los cambios, pulsamos Y para aceptarlo

[![Captura8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura82.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura82.png)

Ahora cuando volvamos a iniciar el equipo, veremos que delante del
nombre del usuario, nos aparece el nombre del dominio, esto indica que
se ha creado correctamente este dominio

[![Captura9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura92.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura92.png)

Usuarios y grupos {.western}
=================

Ahora lo siguiente que tenemos que hacer es crear los grupos del
dominio.

Se hace mediante el comando net localgroup Nombregrupo /add /domain

Observamos que he creado los tres grupos necesarios

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura11.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura11.png)

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura12.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura12.png)

 

Ahora con este comando comprobamos que están los grupos creados
correctamente.

 

Es este comando: net localgroup

[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura23.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura23.png)

Ahora procederemos a crear los usuarios, se hace mediante el comando net
user Nombreusuario contraseña /add /domain

Vemos como aquí creo los usuarios de Informática

[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura33.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura33.png)
[![Captura4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura43.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura43.png)
[![Captura5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura53.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura53.png)

Para comprobar que los usuarios se han creado correctamente lo hacemos
mediante el comando net user

[![Captura6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura63.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura63.png)

Para añadir los usuarios a los grupos utilizaremos el comando net
localgroup nombregrupo nombres de usuarios /add

[![Captura7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura73.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura73.png)

Vemos los usuarios de informática dentro de su grupo

[![Captura8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura83.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura83.png)

Ahora vemos los usuarios de Contabilidad dentro de su propio grupo

[![Captura9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura93.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura93.png)

En esta otra captura vemos a los usuarios de Marketing dentro del grupo

[![Captura10](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura101.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura101.png)

Horarios {.western}
========

Ahora nos pondremos a indicarle restricciones de acceso a los usuarios
al sistema en determinadas ocasiones.

Para ello utilizaremos el comando net user nombreusuario
/time:Dia1-Dia2,horainicio-horafin

Aquí vemos las restricciones de uso a los usuarios de informática

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura13.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura13.png)
[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura24.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura24.png)
[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura34.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura34.png)

Ahora si utilizamos el comando net user nombreusuario, veremos como en
su perfil tienen puestos los horarios adecuadamente.

[![Info
Contabilidad](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Contabilidad.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Contabilidad.png)
[![Info
Informatica](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Informatica.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Informatica.png)

[![Info
Marketing](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Marketing.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Marketing.png)

Perfiles Móviles {.western}
================

Ahora estableceremos perfiles móviles a un usuario de cada grupo.

Lo haremos mediante el comando net user nombreusuario /profilepath:ruta
carpeta

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura14.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura14.png)

Previamente habíamos creado la carpeta Profiles dentro de C:

[![Carpeta
profiles](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Carpeta-profiles.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Carpeta-profiles.png)

 

Ahora en el servidor vemos como se han creado las carpetas de cada
perfil móvil una vez se han logeado en el sistema desde uno de los
equipos dentro del dominio

[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura35.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura35.png)

Con esto ya estaría creado el directorio activo y configurado de forma
básica el servidor 2012 en Core

 
