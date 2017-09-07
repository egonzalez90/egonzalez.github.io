Title: Eliminar VM (LDOM) en SPARC
Date: 2014-12-02 14:51
Author: egongu90
Category: Virtualizacion
Tags: eliminar, ldm list, ldm remove, ldom, list-bindings, oracle, quitar, remove, solaris, sparc, VM
Slug: eliminar-vm-ldom-en-sparc
Status: published

Primero comprobaremos que maquinas tenemos y el estado de ellas

> ldm list

A continuación, si la maquina que queremos borrar esta encendida la
apagaremos

> ldm stop LDOM

 

Lo siguiente será quitar la consola de la maquina

> ldm unbind LDOM

Listaremos la configuración de la maquina y buscaremos los discos que
tenga asignados, normalmente está al final del archivo

> ldm list-bindings LDOM

Quitaremos el controlador del disco de la maquina

> ldm remove-vdiskserverdevice VOLUMEN@LDOM

Eliminaremos el disco de la configuración de la maquina

> ldm remove-vdisk DISKNAME LDOM

Eliminamos las NIC

> ldm remove-vnet NIC\_NAME LDOM

Borramos VDS

> ldm remove-vds LDOM

Eliminamos configuración de la maquina

> ldm remove-domain LDOM

Borramos los datos de la maquina, esto se hace eliminando la carpeta
donde están las maquinas guardadas

> rm -R /ruta/carpeta/LDOM/
