Title: Cambio de PSP para un dispositivo RDM en ESXi 5.x
Date: 2014-09-27 16:33
Author: egongu90
Category: Virtualizacion
Tags: cambiar, cambio, dispositivo, esxcli, esxi, most recent used, MRU, naa., nmp, PSP, raw, rdm, round robin, RR, storage, virtualizacion, vml., vmware
Slug: cambio-de-psp-para-un-dispositivo-rdm-en-esxi-5-x
Status: published

Primero veremos la información del RDM mediante este comando

> vmkfstools -q
> /vmfs/volumes/CabinaAlmacenamiento/MaquinaVirtual/MaquinaVirtual.vmdk

<!--more-->

Nos sacara esta información. A nosotros nos interesa el vml.\*\*\*\*\*,
el cual es el que utilizaremos en el siguiente paso.

> Disk
> /vmfs/volumes/CabinaAlmacenamiento/MaquinaVirtual/MaquinaVirtual.vmdk
> is a Passthrough Raw Device Mapping
>
> Maps to: vml.0200460111600c0ff0001db1507629da5301000000333833383334

A continuación utilizaremos el vml.\*\*\*\* para ver la información del
dispositivo

> esxcfg-scsidevs -l
> -d vml.0200460111600c0ff0001db1507629da5301000000333833383334

Esto nos mostrara una información parecida a esta, a nosotros nos
interesa el naa.\*\*\*\*\*

> naa.600drtf0001db1507629da5301055555
>
> Device Type: Direct-Access
>
> Size: 7629388 MB
>
> Display Name: DotHill Fibre Channel Disk
> (naa.600drtf0001db1507629da5301055555)
>
> Multipath Plugin: NMP
>
> Console Device:
> /vmfs/devices/disks/naa.600drtf0001db1507629da5301055555
>
> Devfs Path: /vmfs/devices/disks/naa.600drtf0001db1507629da5301055555
>
> Vendor: DotHill   Model: DH3834            Revis: G105
>
> SCSI Level: 5  Is Pseudo: false Status: on
>
> Is RDM Capable: true  Is Removable: false
>
> Is Local: false Is SSD: false
>
> Other Names:
>
> vml.0200460111600c0ff0001db1507629da5301000000333833383334
>
> VAAI Status: supported

Los siguiente es ver que configuración de PSP tiene el dispositivo, para
ello utilizaremos este comando con el naa.\*\*\*\*\* que nos mostró el
comando anterior

> esxcli storage nmp device list -d naa.600drtf0001db1507629da5301055555

Esta es la salida del comando anterior, en el que podremos ver el tipo
de PSP en la linea Path selection Policy, en este caso es MRU (Most
Recent Used)

> naa.600drtf0001db1507629da5301055555
>
> Device Display Name: DotHill Fibre Channel Disk
> (naa.600drtf0001db1507629da5301055555)
>
> Storage Array Type: VMW\_SATP\_ALUA
>
> Storage Array Type Device Config:
> {implicit\_support=on;explicit\_support=off;
> explicit\_allow=on;alua\_followover=on;{TPG\_id=1,TPG\_state=ANO}{TPG\_id=0,TPG\_state=AO}}
>
> Path Selection Policy: VMW\_PSP\_MRU
>
> Path Selection Policy Device Config: Current Path=vmhba0:C0:T3:L1
>
> Path Selection Policy Device Custom Config:
>
> Working Paths: vmhba0:C0:T3:L1
>
> Is Local SAS Device: false
>
> Is Boot USB Device: false

Si quisiéramos cambiar el PSP lo haremos mediante este comando, en este
caso la política que aplicaremos sera RR(Round Robin)

> esxcli storage nmp device set -d
> naa.600drtf0001db1507629da5301055555 --psp=VMW\_PSP\_RR

Volvemos a comprobar que tipo de politica se ha aplicado

> esxcli storage nmp device list -d naa.600drtf0001db1507629da5301055555

Aquí vemos como efectivamente esta en RR el PSP

> naa.600drtf0001db1507629da5301055555
>
> Device Display Name: DotHill Fibre Channel Disk
> (naa.600drtf0001db1507629da5301055555)
>
> Storage Array Type: VMW\_SATP\_ALUA
>
> Storage Array Type Device Config:
> {implicit\_support=on;explicit\_support=off;
> explicit\_allow=on;alua\_followover=on;{TPG\_id=1,TPG\_state=ANO}{TPG\_id=0,TPG\_state=AO}}
>
> Path Selection Policy: VMW\_PSP\_RR
>
> Path Selection Policy Device Config: Current Path=vmhba0:C0:T3:L1
>
> Path Selection Policy Device Custom Config:
>
> Working Paths: vmhba0:C0:T3:L1
>
> Is Local SAS Device: false
>
> Is Boot USB Device: false

 

Muchas gracias por leer el blog.
