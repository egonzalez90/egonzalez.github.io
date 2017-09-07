Title: Montar volumen AWS en RHEL
Date: 2014-09-17 17:05
Author: egongu90
Category: Linux, OpenStack
Tags: amazon, añadir, AWS, cloud, computing, formatear, linux, montar, red hat, rhel, services, volumen, web, xvdf
Slug: montar-volumen-aws-en-rhel
Status: published

Para poder realizar estos pasos es necesario que se haya creado un
volumen previamente en EC2 de AWS, nos conectaremos a la maquina por SSH
y seguiremos los siguientes pasos<!--more-->

Primero comprobaremos que el volumen que habíamos creado en EC2 le ve el
SO, utilizaremos este comando

> <span class="command" style="color: #000000;">lsblk</span><span
> style="color: #000000;"> </span>

Lo normal es que el primer  volumen que añadas se llame xvdf alojado en
/dev/

Ahora lo formatearemos en EXT4

> sudo mkfs -t ext4 /dev/xvdf

A continuación crearemos la carpeta en donde montaremos el volumen y
después lo montaremos en dicha carpeta

> sudo mkdir /mnt/volumen
>
> sudo mount /dev/xvdf /mnt/volumen

Ahora con el comando df -h comprobaremos que el SO ya lo ve montado


