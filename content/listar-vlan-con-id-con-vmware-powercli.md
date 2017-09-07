Title: Listar vlan ID con VMware PowerCLI
Date: 2014-08-22 15:59
Author: egongu90
Category: Virtualizacion
Tags: all vlan, CLI, CSV, esxi, Excel, host, ID, list portgroup id, list vlan, listar, portgroup, powercli, todas vlan, virtualizacion, Vlan, vlan id, vmware
Slug: listar-vlan-con-id-con-vmware-powercli
Status: published

Para poder listar todas las VLans de un host ESXi con su ID primero nos
deberemos conectar a ese host por PowerCLI, usaremos este comando:

> Connect\_VIServer -server "host" -user "usuario" -password
> "contraseña"

Una vez conectados a dicho ESXi, utilizaremos el siguiente comando con
el que listaremos las vlans y los ID, ademas lo exportaremos a un
formato CSV para poder analizarlo con Excel

> Get-VirtualPortGroup -VMHost "Host" | Select Name, VirtualSwitch,
> VLanId | Export-Csv C:nombre.csv

Espero les sirva, un saludo
