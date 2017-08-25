---
id: 670
title: Cambio de PSP para un dispositivo RDM en ESXi 5.x
date: 2014-09-27T16:33:05+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=670
permalink: /cambio-de-psp-para-un-dispositivo-rdm-en-esxi-5-x/
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
image: /wp-content/uploads/2014/09/vmware-logo-EA45624ADF-seeklogo.com_.gif
categories:
  - Virtualizacion
tags:
  - cambiar
  - cambio
  - dispositivo
  - esxcli
  - esxi
  - most recent used
  - MRU
  - naa.
  - nmp
  - PSP
  - raw
  - rdm
  - round robin
  - RR
  - storage
  - virtualizacion
  - vml.
  - vmware
---
Primero veremos la información del RDM mediante este comando
<blockquote>vmkfstools -q /vmfs/volumes/CabinaAlmacenamiento/MaquinaVirtual/MaquinaVirtual.vmdk</blockquote>
<!--more-->

Nos sacara esta información. A nosotros nos interesa el vml.*****, el cual es el que utilizaremos en el siguiente paso.
<blockquote>Disk /vmfs/volumes/CabinaAlmacenamiento/MaquinaVirtual/MaquinaVirtual.vmdk is a Passthrough Raw Device Mapping

Maps to: vml.0200460111600c0ff0001db1507629da5301000000333833383334</blockquote>
A continuación utilizaremos el vml.**** para ver la información del dispositivo
<blockquote>esxcfg-scsidevs -l -d vml.0200460111600c0ff0001db1507629da5301000000333833383334</blockquote>
Esto nos mostrara una información parecida a esta, a nosotros nos interesa el naa.*****
<blockquote>naa.600drtf0001db1507629da5301055555

Device Type: Direct-Access

Size: 7629388 MB

Display Name: DotHill Fibre Channel Disk (naa.600drtf0001db1507629da5301055555)

Multipath Plugin: NMP

Console Device: /vmfs/devices/disks/naa.600drtf0001db1507629da5301055555

Devfs Path: /vmfs/devices/disks/naa.600drtf0001db1507629da5301055555

Vendor: DotHill   Model: DH3834            Revis: G105

SCSI Level: 5  Is Pseudo: false Status: on

Is RDM Capable: true  Is Removable: false

Is Local: false Is SSD: false

Other Names:

vml.0200460111600c0ff0001db1507629da5301000000333833383334

VAAI Status: supported</blockquote>
Los siguiente es ver que configuración de PSP tiene el dispositivo, para ello utilizaremos este comando con el naa.***** que nos mostró el comando anterior
<blockquote>esxcli storage nmp device list -d naa.600drtf0001db1507629da5301055555</blockquote>
Esta es la salida del comando anterior, en el que podremos ver el tipo de PSP en la linea Path selection Policy, en este caso es MRU (Most Recent Used)
<blockquote>naa.600drtf0001db1507629da5301055555

Device Display Name: DotHill Fibre Channel Disk (naa.600drtf0001db1507629da5301055555)

Storage Array Type: VMW_SATP_ALUA

Storage Array Type Device Config: {implicit_support=on;explicit_support=off; explicit_allow=on;alua_followover=on;{TPG_id=1,TPG_state=ANO}{TPG_id=0,TPG_state=AO}}

Path Selection Policy: VMW_PSP_MRU

Path Selection Policy Device Config: Current Path=vmhba0:C0:T3:L1

Path Selection Policy Device Custom Config:

Working Paths: vmhba0:C0:T3:L1

Is Local SAS Device: false

Is Boot USB Device: false</blockquote>
Si quisiéramos cambiar el PSP lo haremos mediante este comando, en este caso la política que aplicaremos sera RR(Round Robin)
<blockquote>esxcli storage nmp device set -d naa.600drtf0001db1507629da5301055555 --psp=VMW_PSP_RR</blockquote>
Volvemos a comprobar que tipo de politica se ha aplicado
<blockquote>esxcli storage nmp device list -d naa.600drtf0001db1507629da5301055555</blockquote>
Aquí vemos como efectivamente esta en RR el PSP
<blockquote>naa.600drtf0001db1507629da5301055555

Device Display Name: DotHill Fibre Channel Disk (naa.600drtf0001db1507629da5301055555)

Storage Array Type: VMW_SATP_ALUA

Storage Array Type Device Config: {implicit_support=on;explicit_support=off; explicit_allow=on;alua_followover=on;{TPG_id=1,TPG_state=ANO}{TPG_id=0,TPG_state=AO}}

Path Selection Policy: VMW_PSP_RR

Path Selection Policy Device Config: Current Path=vmhba0:C0:T3:L1

Path Selection Policy Device Custom Config:

Working Paths: vmhba0:C0:T3:L1

Is Local SAS Device: false

Is Boot USB Device: false</blockquote>
&nbsp;

Muchas gracias por leer el blog.