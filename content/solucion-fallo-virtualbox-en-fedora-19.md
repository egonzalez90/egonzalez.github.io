Title: Solución fallo VirtualBox en Fedora 19
Date: 2013-11-13 18:00
Author: egongu90
Category: Linux
Tags: error, fedora 19, linux, maquina virtual, solucion, Virtualbox, virtualizacion, VM
Slug: solucion-fallo-virtualbox-en-fedora-19
Status: published

Mucha gente ha tenido problemas a la hora de abrir una maquina virtual
en VirtualBox con Fedora 19, suele salir un error de compilación de VBox
que por mucho que lo recompiles no se soluciona si no sigues los pasos
previos que voy a explicar.  
<!--more-->  
En primer lugar deberías de desinstalar VirtualBox completamente, doy
por hecho de que si lo has instalado también sabrás desinstalarlo.  
A continuación deberías de actualizar los paquetes del sistema, esto no
es necesario, pero siempre recomendable por motivos de seguridad.Se hace
mediante este comando:

    # yum -y upate

<address>
 

</address>
Después instalamos datos del kernel

    # yum -y install kernel-headers kernel-devel dkms gcc

<address>
 

</address>
Ahora vamos a la carpeta de repositorios de fedora

    # cd /etc/yum.repos.d

<address>
 

</address>
Ahora creamos/modificamos este archivo

    # vi virtualbox.repo

<address>
 

</address>
Se rellena con la siguiente información:

                   [virtualbox]
    name=Fedora$releasever - $basearch - VirtualBox
    baseurl=http://download.virtualbox.org/virtualbox/rpm/fedora/$releasever/$basearch
    enabled=1
    gpgcheck=1
    gpgkey=http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc

Guardamos y salimos de este archivo

Ahora instalamos VirtualBox

    # yum -y install VirtualBox-4.2

<address>
 

</address>
Ahora ejecutamos este comando para configurar VirtualBox

    # /etc/init.d/vboxdrv setup

<address>
 

</address>
Ahora añadimos nuestro usuario al grupo que tiene permisos para usar
VirtualBox

    # usermod -G vboxusers -a "NombredeUsuario"

Esto debería permitirnos crear maquinas virtuales y abrirlas ya

<address>
 

</address>

