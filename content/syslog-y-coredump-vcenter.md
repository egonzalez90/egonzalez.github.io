Title: Syslog y coredump vCenter
Date: 2014-08-08 16:55
Author: egongu90
Category: Virtualizacion
Tags: cloud, collector, coredump, esxi, log, syslog, vcenter, virtualizacion, vmware
Slug: syslog-y-coredump-vcenter
Status: published

Vamos a configurar syslog y coredump de los host ESXi para que un
vCenter recoja los logs de estos host

Primero deberemos tener instaladas y configuradas en el vCenter estas
aplicaciones:

Dump Collector y Syslog collector.

Para configurar el Syslog  
\# esxcli system syslog config set --loghost="IPHOST"  
\# esxcli system syslog reload

Para configurar el Coredump  
\# esxcli system coredump network set --interface-name vmk0
--server-ipv4 "IPHOST"  
\# esxcli system coredump network set --enable true  
\# esxcli system coredump network get ( para comprobar que todo ok )  
--interface-name vmkX Hay que ver por que vmk ve la red de gestión

Estos comandos habría que ejecutarlos por cada host ESXi que queramos
que envié los logs al vCenter

 

Un saludo y espero que sea de ayuda
