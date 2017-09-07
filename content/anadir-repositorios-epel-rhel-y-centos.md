Title: Añadir repositorios EPEL RHEL y CentOS
Date: 2014-09-09 15:32
Author: egongu90
Category: Linux
Tags: añadir, centos, descargar, enablerepo, epel, fedoraproject, instalar, red hat, repolist, repositorios, rhel
Slug: anadir-repositorios-epel-rhel-y-centos
Status: published

Primero descargaremos el repositorio para nuestra versión de CentOS o
RHEL mediante wget.

A continuacion instalaremos el paquete que habiamos descargado con rpm.

Esta son las diferentes versiones de CentOS y RHEL

> \#\# RHEL/CentOS 7 64-Bit \#\#  
>  \#
> wget http://mirror.rackcentral.com.au/epel/7/x86\_64/epel-release-7-1.noarch.rpm  
>  \# rpm -ivh epel-release-7-0.2.noarch.rpm

 

> \#\# RHEL/CentOS 6 32-Bit \#\#  
>  \#
> wget http://mirror.rackcentral.com.au/epel/6/i386/epel-release-6-8.noarch.rpm  
>  \# rpm -ivh epel-release-6-8.noarch.rpm

 

> \#\# RHEL/CentOS 6 64-Bit \#\#  
>  \#
> wget http://mirror.rackcentral.com.au/epel/6/x86\_64/epel-release-6-8.noarch.rpm  
>  \# rpm -ivh epel-release-6-8.noarch.rpm

Lo siguiente que haremos sera comprobar que esta en la lista de
repositorios mediante este comando

> yum repolist

Por ultimo habilitaremos el repositorio, para que podamos usarlo
habitualmente

> yum --enablerepo=epel
