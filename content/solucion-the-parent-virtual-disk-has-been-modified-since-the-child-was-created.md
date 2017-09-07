Title: Solucion The parent virtual disk has been modified since the child was created
Date: 2014-05-10 13:10
Author: egongu90
Category: Virtualizacion
Tags: .vmdk, CID, consolidacion, error, esxi, host, parentCID, snapshot, vcenter, veeam, veeam backup, virtualizacion, vmware
Slug: solucion-the-parent-virtual-disk-has-been-modified-since-the-child-was-created
Status: published

Es frecuente que con determinadas soluciones de copias de seguridad como
Veeam Backup de este error a la hora de arrancar la VM o incluso a no
llegar a generarse ese Backup, también puede pasar si se ha modificado
el .vmdk  o el snapshot del que depende otro snapshot.<!--more-->Cuando
das a consolidar los snapshots de una maquina virtual te aparece este
error:

`Cannot open the disk '/vmfs/volumes/4a365b5d-eceda1-19-439b-000cfc0086f3/examplevm/examplevm-000001.vmdk' or one of the snapshot disks it depends on. Reason: The parent virtual disk has been modified since the child was created.`

Eso ocurre por lo escrito en la introducción de esta entrada.

La solución no es nada complicada, aunque si se tuviera un gran numero
de snapshots puede ser un poco larga.

Lo primero que debemos de hacer es saber en que Datastore tenemos la VM
alojada,para eso en vCenter o en el propio ESXi iremos a la pestaña
Sumary de nuestra VM, en la parte de Storage veremos el nombre de
nuestro Datastore

[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura15.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura15.png)

A continuación abriremos una sesión con SSH a el host ESXi o a cualquier
otro que tenga acceso a nuestro Datastore.

Una vez abierta la sesión, iremos a la siguiente ruta:

/vmfs/volumes/NOMBREDATASTORE/NOMBREVM/

Haciendo un ls a esta carpeta podremos ver los archivos que contienen
las VM, a nosotros nos interesan los .vmdk. En este caso tengo 3
importantes para esta entrada .vmdk:

-   CentOS\_Prueba1.vmdk
-   CentOS\_Prueba1-000001.vmdk
-   CentOS\_Prueba1-000002.vmdk

Los .vmdk delta y flat no nos interesan en este caso

[![Captura\_1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura_1.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura_1.png)

Lo primero que tenemos que hacer para arreglar este error es editar el
.vmdk padre, que es el que se llama igual que nuestra VM sin ninguna
numeración
detrás[![Captura1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura16.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura16.png)

Una vez abrimos este archivo, apuntaremos el CID y el parentCID, también
tenemos que observar que en este .vmdk el parentCID sea ffffffff(esto
indica que es el fichero padre del disco
VM)[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura22.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura22.png)

Después iremos al .vmdk con la numeración mas baja, que en este caso es
000001.vmdk[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura32.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura32.png)

Aquí podemos ver que el parentCID no coincide con el CID del .vmdk
padre(el ejemplo
anterior)[![Captura4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura42.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura42.png)

Modificaremos esa linea para hacerla coincidir con el CID del disco
padre, ademas tambien apuntaremos el CID de este
.vmdk[![Captura6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura62.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura62.png)

Ahora iremos a los demas snapshots e iremos realizando los pasos
anteriores para hacer coincidir los CID y los parentCID con sus
respectivos .vmdk. Tendremos que darnos cuenta de que el parentCID es el
CID del .vmdk anterior(no es siempre el del disco padre). Ejemplo:

Nieto tiene el parentCID de Padre, Padre tiene el parentCID de Abuelo y
Abuelo tiene el parentCID de Bisabuelo

Por ultimo iremos a comprobar que los cambios funcionaron y esta todo
correcto, para ello iremos a nuestro vCenter o host, aquí pulsaremos
boton derecho sobre la VM, Snapshot/Consolidate. Nos preguntara si
estamos seguros de querer consolidar, daremos que
si[![Captura7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura72.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura72.png)

Vemos que la consolidación se ejecuto
correctamente[![Captura8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura82.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/05/Captura82.png)

Espero ayudarles a resolver estos errores y que todo les funcione
correctamente, si quieren mas información sobre esto pueden hacerlo en
este enlace de ayuda de VMware:
<http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1007969>

Un saludo y muchas gracias por leer la entrada
