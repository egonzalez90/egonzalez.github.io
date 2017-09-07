Title: Montar directorio NFS
Date: 2014-09-05 15:46
Author: egongu90
Category: Linux
Tags: centos, default, df -h, directorio, fstab, linux, montar, mount, nfs, red hat, rhel
Slug: montar-directorio-nfs
Status: published

Primero crearemos la carpeta en donde vamos a montar el directorio NFS

> mkdir /rutadondemontareldirectorio

A continuación utilizaremos este comando para montar el directorio NFS
en la carpeta creada anteriormente.

SERVIDOR puede ser tanto hostname como IP(yo siempre prefiero utilizar
IP)

> mount SERVIDOR:/ruta/a/la/carpeta /rutadondemontareldirectorio

Una vez montado sin darnos ningún error, utilizaremos este comando para
comprobar que nos mostrara los directorios que están montados en nuestro
sistema y que tamaño tienen

> df -h

Ahora que ya hemos montado el directorio NFS, lo incluiremos en fstab
para que se monte siempre en el arranque del sistema sin tener que
hacerlo manualmente por los pasos anteriores, para ello modificaremos
este archivo

> vi /etc/fstab

Dentro del archivo incluiremos esta linea y guardaremos

> SERVIDOR:/ruta/a/la/carpeta            /rutadondemontareldirectorio  
>          default            0 0

Podemos comprobar que el archivo fstab funciona correctamente utilizando
el mismo comando de antes para ver los directorios montados y su tamaño,
pero esta vez lo haremos una vez encendida la maquina, sin haber montado
el directorio NFS de forma manual

> df -h
