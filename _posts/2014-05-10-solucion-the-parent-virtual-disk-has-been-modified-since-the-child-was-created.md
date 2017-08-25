---
id: 527
title: Solucion The parent virtual disk has been modified since the child was created
date: 2014-05-10T13:10:43+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=527
permalink: /solucion-the-parent-virtual-disk-has-been-modified-since-the-child-was-created/
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
kopa_resolution_total_view:
  - "2"
image: /wp-content/uploads/2014/05/Captura62.png
categories:
  - Virtualizacion
tags:
  - .vmdk
  - CID
  - consolidacion
  - error
  - esxi
  - host
  - parentCID
  - snapshot
  - vcenter
  - veeam
  - veeam backup
  - virtualizacion
  - vmware
---
Es frecuente que con determinadas soluciones de copias de seguridad como Veeam Backup de este error a la hora de arrancar la VM o incluso a no llegar a generarse ese Backup, también puede pasar si se ha modificado el .vmdk  o el snapshot del que depende otro snapshot.<!--more-->Cuando das a consolidar los snapshots de una maquina virtual te aparece este error:

<code>Cannot open the disk '/vmfs/volumes/4a365b5d-eceda1-19-439b-000cfc0086f3/<em>examplevm/examplevm-000001.vmdk</em>' or one of the snapshot disks it depends on.
Reason: The parent virtual disk has been modified since the child was created.</code>

Eso ocurre por lo escrito en la introducción de esta entrada.

La solución no es nada complicada, aunque si se tuviera un gran numero de snapshots puede ser un poco larga.

Lo primero que debemos de hacer es saber en que Datastore tenemos la VM alojada,para eso en vCenter o en el propio ESXi iremos a la pestaña Sumary de nuestra VM, en la parte de Storage veremos el nombre de nuestro Datastore

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura15.png"><img class="aligncenter size-full wp-image-528" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura15.png" alt="Captura" width="728" height="370" /></a>

A continuación abriremos una sesión con SSH a el host ESXi o a cualquier otro que tenga acceso a nuestro Datastore.

Una vez abierta la sesión, iremos a la siguiente ruta:

/vmfs/volumes/NOMBREDATASTORE/NOMBREVM/

Haciendo un ls a esta carpeta podremos ver los archivos que contienen las VM, a nosotros nos interesan los .vmdk. En este caso tengo 3 importantes para esta entrada .vmdk:
<ul>
	<li>CentOS_Prueba1.vmdk</li>
	<li>CentOS_Prueba1-000001.vmdk</li>
	<li>CentOS_Prueba1-000002.vmdk</li>
</ul>
Los .vmdk delta y flat no nos interesan en este caso

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura_1.png"><img class="aligncenter size-full wp-image-529" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura_1.png" alt="Captura_1" width="674" height="207" /></a>

Lo primero que tenemos que hacer para arreglar este error es editar el .vmdk padre, que es el que se llama igual que nuestra VM sin ninguna numeración detrás<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura16.png"><img class="aligncenter size-full wp-image-530" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura16.png" alt="Captura1" width="737" height="31" /></a>

Una vez abrimos este archivo, apuntaremos el CID y el parentCID, también tenemos que observar que en este .vmdk el parentCID sea ffffffff(esto indica que es el fichero padre del disco VM)<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura22.png"><img class="aligncenter size-full wp-image-531" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura22.png" alt="Captura2" width="557" height="372" /></a>

Después iremos al .vmdk con la numeración mas baja, que en este caso es 000001.vmdk<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura32.png"><img class="aligncenter size-full wp-image-532" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura32.png" alt="Captura3" width="819" height="67" /></a>

Aquí podemos ver que el parentCID no coincide con el CID del .vmdk padre(el ejemplo anterior)<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura42.png"><img class="aligncenter size-full wp-image-533" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura42.png" alt="Captura4" width="523" height="276" /></a>

Modificaremos esa linea para hacerla coincidir con el CID del disco padre, ademas tambien apuntaremos el CID de este .vmdk<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura62.png"><img class="aligncenter size-full wp-image-534" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura62.png" alt="Captura6" width="536" height="248" /></a>

Ahora iremos a los demas snapshots e iremos realizando los pasos anteriores para hacer coincidir los CID y los parentCID con sus respectivos .vmdk. Tendremos que darnos cuenta de que el parentCID es el CID del .vmdk anterior(no es siempre el del disco padre). Ejemplo:

Nieto tiene el parentCID de Padre, Padre tiene el parentCID de Abuelo y Abuelo tiene el parentCID de Bisabuelo

Por ultimo iremos a comprobar que los cambios funcionaron y esta todo correcto, para ello iremos a nuestro vCenter o host, aquí pulsaremos boton derecho sobre la VM, Snapshot/Consolidate. Nos preguntara si estamos seguros de querer consolidar, daremos que si<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura72.png"><img class="aligncenter size-full wp-image-535" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura72.png" alt="Captura7" width="499" height="174" /></a>

Vemos que la consolidación se ejecuto correctamente<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura82.png"><img class="aligncenter size-full wp-image-536" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura82.png" alt="Captura8" width="1082" height="60" /></a>

Espero ayudarles a resolver estos errores y que todo les funcione correctamente, si quieren mas información sobre esto pueden hacerlo en este enlace de ayuda de VMware: <a href="http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1007969" target="_blank">http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&amp;cmd=displayKC&amp;externalId=1007969</a>

Un saludo y muchas gracias por leer la entrada