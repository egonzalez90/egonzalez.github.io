Title: Recuperar GRUB RHEL y CentOS
Date: 2014-08-28 15:34
Author: egongu90
Category: Linux
Tags: centos, grub, hd0, linux, red hat, rescue, rhel, root, setup
Slug: recuperar-grub-rhel-y-centos
Status: published

Muchas veces te sueles cargar la configuración del GRUB, o simplemente
cuando instalas Windows en otra partición. <!--more-->Para ello lo
tendremos que recuperar de la siguiente forma:

1º Insertaremos la ISO en el equipo

2º Cuando salga el prompt de arranque, escribiremos

> linux rescue

3º A continuación

> grub

4º Ahora pondremos este comando, donde hd0,0 es el disco donde esta el
grub

> root (hd0,0)

5º Lo configuraremos

> setup (hd0)

6º Ya terminamos

> quit
>
> ctrl-d
