Title: Crear Swap AWS en RHEL
Date: 2014-09-19 16:28
Author: egongu90
Category: Linux, OpenStack
Tags: /etc/fstab, amazon, AWS, cloud, mkswap, red hat, rhel, services, swap, swapon, web
Slug: crear-swap-rhel-aws
Status: published

Cuando creas una instancia, esta se hace sin swap, el cual es necesario
para el uso de determinadas aplicaciones.<!--more-->

Para ello deberemos tener espacio en disco, si no tuvieras suficiente
puedes seguir esta entrada pare ver como se
hace: [http://egonzalez.org/?p=635](http://egonzalez.org/?p=662 "Montar volumen AWS en RHEL")

A continuación iremos a la consola y ejecutaremos los siguientes
comandos:

> sudo /bin/dd if=/dev/zero of=/var/swap.1 bs=1M count=1024
>
> sudo /sbin/mkswap /var/swap.1
>
> sudo /sbin/swapon /var/swap.1

Con ello crearemos el archivo swap y lo montaremos.  
Con este comando se crea de un tamaño de 1024 MB, si se quisiera mas,
abría que cambiar el valor count a el deseado.

Por ultimo abría que añadir esta linea al archivo /etc/fstab , esto
permitirá que se monte durante el arranque automáticamente.

> /var/swap.1 swap swap defaults 0 0

Espero ser de ayuda, un saludo
