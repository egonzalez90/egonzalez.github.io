Title: Alineamiento MBR maquinas virtuales
Date: 2014-09-03 15:21
Author: egongu90
Category: Linux, Virtualizacion
Tags: alinear, esxi, ext3, ext4, grub, maquina virtual, mbr, mbralign, mbrscan, netapp, redhat, rhel, VM, vmfs, vmware, volumes
Slug: alineamiento-mbr-maquinas-virtuales
Status: published

Antes de la llegada de el sistema de ficheros EXT4, cuando creabas
maquinas virtuales, estas estaban desalineadas el mbr del vmfs y de el
almacenamiento,  lo que generaba menor rendimiento.<!--more-->

Para ello dedico esta entrada, con la que mostrare como alinear el mbr.

Lo primero que necesitaremos es el paquete con las tools mbrscan y
mbralign, este paquete le copiaremos a el directorio /opt/ontap/ de un
host ESXi que tenga acceso al almacenamiento donde tenemos la maquina
guardada.

Una vez copiado el paquete a dicho directorio pasaremos a escanear y a
realinear el mbr de la maquina, para ello necesitamos que este apagada.

Una vez apagada iremos al directorio /opt/ontap/ y ejecutaremos el
siguiente comando con el que analizaremos el disco de la maquina para
ver si necesita ser alineado.

> ./mbrscan
> /vmfs/volumes/ALMACENAMIENTO/maquinavirtual/maquinavirtual-flat.vmdk

Esto nos mostrara un mensaje en el que pondra:

> Aligned yes o Aligned no

En el caso de que pusiera align no, deberemos realinear el mbr de la
maquina, lo haremos mediante este comando:

> ./mbralign
> /vmfs/volumes/ALMACENAMIENTO/maquinavirtual/maquinavirtual-flat.vmdk

Esto nos creara un archivo .bak del disco que vamos a alinear por si
fallara este proceso poder recuperarlo, este proceso tardara
bastante(dependiendo del tamaño del disco)

Una vez acabado ese proceso de alineamiento, volveremos a utilizar el
comando mbrscan para comprobar que este bien hecho.

Por ultimo, el alineado del mbr se carga totalmente el GRUB de la
maquina, por lo que deberemos recuperarlo.

En esta entrada tienes como hacerlo: [<span id="sample-permalink"
style="color: #666666;" tabindex="-1">http://egonzalez.org/<span
id="editable-post-name"
title="Enlace permanente temporal. Haz clic para editar esta parte.">recuperar-grub-rhel-y-centos</span>/</span><span
style="color: #666666;"> </span>](http://egonzalez.org/recuperar-grub-rhel-y-centos/%20 "Recuperar GRUB RHEL y CentOS")

Una vez recuperado el GRUB y comprobado que la maquina funciona
correctamente, borraremos el archivo .bak que se había creado.

Espero poder ayudar, un saludo
