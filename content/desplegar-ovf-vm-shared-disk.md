Title: Desplegar OVF VM Shared Disk
Date: 2014-08-26 14:22
Author: egongu90
Category: Virtualizacion
Tags: .vmdk, deploy, desplegar, disco compartido, error, esxi, ID, independent, intercambio, ovf, persistent, scsi, shared disk, virtual, virtualizacion, vmware
Slug: desplegar-ovf-vm-shared-disk
Status: published

Cuando se exporta una maquina virtual en formato OVF conVMware, en el
entorno ESXi 5.1 es en donde lo tengo comprobado, los OVF que disponen
de disco compartido o en diferentes controladoras SCSi se despliegan
incorrectamente, intercambiando los discos compartidos de una
controladora por los de otra y cambiando la numeración ejemplo. VM1.vmdk
por VM1\_01.vmdk, por lo que al iniciar la maquina esta no encontrara el
sistema operativo y dará un Boot error.  
Pues bien, para poder exportar y desplegar correctamente estas maquinas
con disco compartido lo que debemos de hacer es lo siguiente:

1º Copiar los discos compartidos a otro almacenamiento y quitar de la
configuración de las maquinas virtuales que tengan esos discos
compartidos.  
2º Exportar en formato OVF la maquina virtual

Para un correcto despliegue de las VM hay que seguir unos pasos:

1º Desplegar OVF  
2º Sin encender las VM, copiar los discos compartidos al Datastore
correcto  
3º Añadir el disco compartido a la configuración de de cada VM que
comparta el disco

Para las VM que no tienen disco compartido solamente se desplegara e
iniciara, habiendo antes configurado la red o los parámetros necesarios
para el correcto funcionamiento.  
La controladoras de los discos SCSi de discos compartidos deberán de
ponerse en virtual y los discos en independiente/persistente.  
Recordar que al desplegar la VM se cambiara la MAC de las NIC, por lo
que se perderá la configuración de red que tenia configurada
previamente, dentro de el directorio /etc/sysconfig/network-script/ se
creara un archivo llamado eth\*.bak en donde esta la configuración de
red antigua.
