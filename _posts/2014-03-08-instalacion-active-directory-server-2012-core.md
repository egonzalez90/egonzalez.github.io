---
id: 338
title: Instalacion Active Directory Server 2012 Core
date: 2014-03-08T16:19:51+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=338
permalink: /instalacion-active-directory-server-2012-core/
snap_isAutoPosted:
  - "1"
ac_featured_article:
  - ""
ac_show_post_thumbnail:
  - ""
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
kopa_resolution_total_view:
  - "3"
post_views_count:
  - "0"
image: /wp-content/uploads/2014/03/Captura92-672x372.png
categories:
  - Various
tags:
  - "2012"
  - active directory
  - configuraccion
  - dominio
  - instalacion
  - server core
  - usuarios
  - windows server
---
En esta entrada vamos a configurar un Server 2012 Core de forma basica, ademas instalaremos y configuraremos un sistema de Directorio Activo con grupos, usuarios, horarios de acceso y perfiles moviles

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png"><!--more--></a>Lo primero que haremos será configurar la red y el nombre del equipo.
<p style="margin-bottom: 0.14in;">Para ello abriremos el PowerShell</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png"><img class="aligncenter size-full wp-image-339" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura10.png" alt="Captura" width="677" height="344" /></a>
<p style="margin-bottom: 0.14in;">Una vez en el powershell, pondremos sconfig para abrir el configurador del sistema</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.12.png"><img class="aligncenter size-full wp-image-340" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.12.png" alt="Captura0.1" width="358" height="101" /></a>
<p style="margin-bottom: 0.14in;">Aquí vemos como está configurado actualmente el sistema.</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.22.png"><img class="aligncenter size-full wp-image-341" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.22.png" alt="Captura0.2" width="611" height="335" /></a>
<p style="margin-bottom: 0.14in;">Elegiremos la opción 2 para cambiar el nombre al equipo, lo escribimos y pulsamos intro</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.32.png"><img class="aligncenter size-full wp-image-342" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.32.png" alt="Captura0.3" width="584" height="344" /></a>
<p style="margin-bottom: 0.14in;">Ahora vemos como está el nombre del equipo cambiado, lo siguiente será configurar la red, para ello pondremos la opción 8</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.42.png"><img class="aligncenter size-full wp-image-343" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.42.png" alt="Captura0.4" width="578" height="338" /></a>
<p style="margin-bottom: 0.14in;">Esto nos mostrara esta imagen, en la que vemos las tarjetas de red que tenemos disponibles, pondremos la opción 10, que es la de nuestra tarjeta de red</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.52.png"><img class="aligncenter size-full wp-image-344" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.52.png" alt="Captura0.5" width="574" height="200" /></a>
<p style="margin-bottom: 0.14in;">Esto abrirá la información de nuestra tarjeta de red</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.62.png"><img class="aligncenter size-full wp-image-345" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.62.png" alt="Captura0.6" width="601" height="341" /></a>
<p style="margin-bottom: 0.14in;">Ahora configuraremos la red con nuestras direcciones IP, para ello seleccionaremos la opción 1.</p>
<p style="margin-bottom: 0.14in;">Aquí pondremos la opción s para seleccionar una IP estática, lo siguiente será poner la dirección IP, mascara de red, y puerta de enlace</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.72.png"><img class="aligncenter size-full wp-image-346" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.72.png" alt="Captura0.7" width="473" height="225" /></a>
<p style="margin-bottom: 0.14in;">A continuación seleccionaremos la opción 2 para establecer un servidor DNS, nosotros pondremos el servidor DNS de google</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.82.png"><img class="aligncenter size-full wp-image-347" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.82.png" alt="Captura0.8" width="507" height="83" /></a>
<p style="margin-bottom: 0.14in;">Ahora vemos como queda configurada nuestra tarjeta de red</p>
<p style="margin-bottom: 0.14in;">Volveremos al menú principal con la opción 4.</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.92.png"><img class="aligncenter size-full wp-image-348" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura0.92.png" alt="Captura0.9" width="643" height="226" /></a>
<h1 class="western">Instalación Active Directory</h1>
<p style="margin-bottom: 0.14in;">Ahora procederemos a la instalación del directorio activo.</p>
<p style="margin-bottom: 0.14in;">Para ello pondremos el comando Get-WindowsFeature, con el que cargara los roles del sistema disponible</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura22.png"><img class="aligncenter size-full wp-image-349" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura22.png" alt="Captura2" width="643" height="252" /></a>

&nbsp;
<h1 class="western"></h1>
<h1 class="western"></h1>
<p style="margin-bottom: 0.14in;">Después utilizaremos el comando Install-WindowsFeature –name AD-Domain-Services, con el que indicaremos que instale el rol de Directorio activo</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura32.png"><img class="aligncenter size-full wp-image-350" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura32.png" alt="Captura3" width="641" height="216" /></a>
<p style="margin-bottom: 0.14in;">Cuando acaben los procesos anteriores, utilizaremos el siguiente comando para instalar las herramientas de administración de directorio activo</p>
<p style="margin-bottom: 0.14in;"><span lang="en-US">El comando es el siguiente Install-WindowsFeature –name AD-Domain-Services -IncludeManagementTool</span></p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura42.png"><img class="aligncenter size-full wp-image-351" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura42.png" alt="Captura4" width="715" height="265" /></a>
<p style="margin-bottom: 0.14in;">Ahora utilizaremos el commando Get-command –module ADDSDeployment para adquirir este módulo de uso del directorio activ</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura52.png"><img class="aligncenter size-full wp-image-352" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura52.png" alt="Captura5" width="661" height="214" /></a>
<p style="margin-bottom: 0.14in;">Posteriormente importaremos este módulo a la configuración de nuestro directorio activo mediante el comando Import-Module ADDSDeployment</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura62.png"><img class="aligncenter size-full wp-image-353" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura62.png" alt="Captura6" width="480" height="46" /></a>
<p style="margin-bottom: 0.14in;">Finalmente instalaremos el bosque del dominio mediante el comando Install-ADDSForest</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura72.png"><img class="aligncenter size-full wp-image-354" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura72.png" alt="Captura7" width="451" height="47" /></a>
<p style="margin-bottom: 0.14in;">Aquí nos solicitara que indiquemos el nombre del dominio, después pondremos la contraseña de administrador del dominio.</p>
<p style="margin-bottom: 0.14in;">Lo siguiente que hará será solicitarnos que reiniciemos el equipo para aplicar los cambios, pulsamos Y para aceptarlo</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura82.png"><img class="aligncenter size-full wp-image-355" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura82.png" alt="Captura8" width="915" height="134" /></a>
<p style="margin-bottom: 0.14in;">Ahora cuando volvamos a iniciar el equipo, veremos que delante del nombre del usuario, nos aparece el nombre del dominio, esto indica que se ha creado correctamente este dominio</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura92.png"><img class="aligncenter size-full wp-image-356" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura92.png" alt="Captura9" width="1065" height="544" /></a>
<h1 class="western">Usuarios y grupos</h1>
<p style="margin-bottom: 0.14in;">Ahora lo siguiente que tenemos que hacer es crear los grupos del dominio.</p>
<p style="margin-bottom: 0.14in;">Se hace mediante el comando net localgroup Nombregrupo /add /domain</p>
<p style="margin-bottom: 0.14in;">Observamos que he creado los tres grupos necesarios</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura11.png"><img class="aligncenter size-full wp-image-358" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura11.png" alt="Captura" width="569" height="123" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura12.png"><img class="aligncenter size-full wp-image-359" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura12.png" alt="Captura" width="569" height="123" /></a>

&nbsp;

Ahora con este comando comprobamos que están los grupos creados correctamente.

&nbsp;

Es este comando: net localgroup

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura23.png"><img class="aligncenter size-full wp-image-360" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura23.png" alt="Captura2" width="484" height="296" /></a>
<p style="margin-bottom: 0.14in;">Ahora procederemos a crear los usuarios, se hace mediante el comando net user Nombreusuario contraseña /add /domain</p>
<p style="margin-bottom: 0.14in;">Vemos como aquí creo los usuarios de Informática</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura33.png"><img class="aligncenter size-full wp-image-361" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura33.png" alt="Captura3" width="629" height="198" /></a> <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura43.png"><img class="aligncenter size-full wp-image-362" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura43.png" alt="Captura4" width="633" height="198" /></a> <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura53.png"><img class="aligncenter size-full wp-image-363" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura53.png" alt="Captura5" width="612" height="195" /></a>
<p style="margin-bottom: 0.14in;">Para comprobar que los usuarios se han creado correctamente lo hacemos mediante el comando net user</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura63.png"><img class="aligncenter size-full wp-image-364" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura63.png" alt="Captura6" width="548" height="175" /></a>
<p style="margin-bottom: 0.14in;">Para añadir los usuarios a los grupos utilizaremos el comando net localgroup nombregrupo nombres de usuarios /add</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura73.png"><img class="aligncenter size-full wp-image-365" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura73.png" alt="Captura7" width="788" height="38" /></a>
<p style="margin-bottom: 0.14in;">Vemos los usuarios de informática dentro de su grupo</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura83.png"><img class="aligncenter size-full wp-image-366" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura83.png" alt="Captura8" width="502" height="191" /></a>
<p style="margin-bottom: 0.14in;">Ahora vemos los usuarios de Contabilidad dentro de su propio grupo</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura93.png"><img class="aligncenter size-full wp-image-367" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura93.png" alt="Captura9" width="734" height="222" /></a>
<p style="margin-bottom: 0.14in;">En esta otra captura vemos a los usuarios de Marketing dentro del grupo</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura101.png"><img class="aligncenter size-full wp-image-368" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura101.png" alt="Captura10" width="724" height="221" /></a>
<h1 class="western">Horarios</h1>
<p style="margin-bottom: 0.14in;">Ahora nos pondremos a indicarle restricciones de acceso a los usuarios al sistema en determinadas ocasiones.</p>
<p style="margin-bottom: 0.14in;">Para ello utilizaremos el comando net user nombreusuario /time:Dia1-Dia2,horainicio-horafin</p>
<p style="margin-bottom: 0.14in;">Aquí vemos las restricciones de uso a los usuarios de informática</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura13.png"><img class="aligncenter size-full wp-image-370" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura13.png" alt="Captura" width="530" height="287" /></a> <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura24.png"><img class="aligncenter size-full wp-image-371" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura24.png" alt="Captura2" width="651" height="256" /></a> <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura34.png"><img class="aligncenter size-full wp-image-372" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura34.png" alt="Captura3" width="549" height="263" /></a>
<p style="margin-bottom: 0.14in;">Ahora si utilizamos el comando net user nombreusuario, veremos como en su perfil tienen puestos los horarios adecuadamente.</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Contabilidad.png"><img class="aligncenter size-full wp-image-373" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Contabilidad.png" alt="Info Contabilidad" width="549" height="389" /></a> <a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Informatica.png"><img class="aligncenter size-full wp-image-374" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Informatica.png" alt="Info Informatica" width="554" height="416" /></a>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Marketing.png"><img class="aligncenter size-full wp-image-375" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Info-Marketing.png" alt="Info Marketing" width="563" height="376" /></a>
<h1 class="western">Perfiles Móviles</h1>
<p style="margin-bottom: 0.14in;">Ahora estableceremos perfiles móviles a un usuario de cada grupo.</p>
<p style="margin-bottom: 0.14in;">Lo haremos mediante el comando net user nombreusuario /profilepath:ruta carpeta</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura14.png"><img class="aligncenter size-full wp-image-378" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura14.png" alt="Captura" width="709" height="171" /></a>
<p style="margin-bottom: 0.14in;">Previamente habíamos creado la carpeta Profiles dentro de C:</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Carpeta-profiles.png"><img class="aligncenter size-full wp-image-380" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Carpeta-profiles.png" alt="Carpeta profiles" width="532" height="200" /></a>

&nbsp;
<p style="margin-bottom: 0.14in;">Ahora en el servidor vemos como se han creado las carpetas de cada perfil móvil una vez se han logeado en el sistema desde uno de los equipos dentro del dominio</p>
<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura35.png"><img class="aligncenter size-full wp-image-379" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/Captura35.png" alt="Captura3" width="675" height="343" /></a>
<p style="margin-bottom: 0.14in;">Con esto ya estaría creado el directorio activo y configurado de forma básica el servidor 2012 en Core</p>
&nbsp;