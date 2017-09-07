Title: Error configuración red en RHEL 6 y VMware ESXi 5.5
Date: 2014-08-07 16:49
Author: egongu90
Category: Linux, Virtualizacion
Tags: 5.5, 70-persistent-net.rules, clon, clondado, daemon, esxi, eth0, ifcfg-eth, linux, network, network manager, nic, nm_controlled, red hat, rhel6, sysadmin, virtualizacion, vmware, vmxnet3
Slug: error-configuracion-red-en-rhel-6-y-vmware-esxi-5-5
Status: published

Ultimamente, desde que hemos empezado a trabajar mas con RHEL 6, nos
dimos cuenta que tras el clonado de las VM, las interfaces de red no se
configuraban bien.

Primero vimos que las MAC de la eth, no se asignaban correctamente, y
despues comprobamos que una vez configuradas al hacer reboot o reinicio
de la red, estas se configuraban como les daba la gana y perdias la
configuracion e internet.

Pues bien, tras un proceso de investigacion llege a la solucion( o al
menos en nuestro sistema), los pasos son los siguientes:

-Quitar las NIC de la antigua configuracion

-Añadir las NIC en vmxnet3 en el vCenter igual que estaban configuradas
anteriormente

-Borrar el archivo /etc/udev/rules.d/70-persistent-net.rules

-Configurar los archivos /etc/sysconfig/network-scripts/ifcfg-eth\*
añadiendo la linea entre su configuracion

**NM\_CONTROLLED=no**

-Parar el servicio NetworkManager y deshabilitarlo del arranque

**service NetworkManager stop**

**chkconfig NetworkManager off**

-Habilitar el servicio network en arranque(puede que ya lo esté)

**chkconfig network on**

-Instalar las vmtools

-Reiniciar la maquina y comprobar que no cambia la configuración entre
el inicio del sistema y tras service network restart

 

Bien, el problema que había, es que por algún error, el network manager
se hacia con el control de la red y daba errores con el demonio network,
lo que hacemos para solucionarlo es, borrar el archivo de la
configuración de las tarjetas,configurar las eth deshabilitando el
control por el Network manager y después deshabilitar Network Manager
del sistema.

De este modo nos funciona sin ningun problema la red.

Espero haber ayudado, un saludo
