--- layout: post title: Cambio de PSP para un dispositivo RDM en ESXi
5.x date: 2014-09-27 16:33:05.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: -
Virtualizacion tags: - cambiar - cambio - dispositivo - esxcli - esxi -
most recent used - MRU - naa. - nmp - PSP - raw - rdm - round robin - RR
- storage - virtualizacion - vml. - vmware meta: \_edit_last: '2'
\_thumbnail_id: '673' snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW: N;
\_wpas_done_all: '1' \_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567368493;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:527;}i:1;a:1:{s:2:"id";i:551;}i:2;a:1:{s:2:"id";i:263;}}}}
dsq_thread_id: '6238310012' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/cambio-de-psp-para-un-dispositivo-rdm-en-esxi-5-x/" ---

Primero veremos la información del RDM mediante este comando

   vmkfstools -q
   /vmfs/volumes/CabinaAlmacenamiento/MaquinaVirtual/MaquinaVirtual.vmdk

Nos sacara esta información. A nosotros nos interesa el vml.*****, el
cual es el que utilizaremos en el siguiente paso.

   Disk
   /vmfs/volumes/CabinaAlmacenamiento/MaquinaVirtual/MaquinaVirtual.vmdk
   is a Passthrough Raw Device Mapping

   Maps to: vml.0200460111600c0ff0001db1507629da5301000000333833383334

A continuación utilizaremos el vml.***\* para ver la información del
dispositivo

   esxcfg-scsidevs -l
   -d vml.0200460111600c0ff0001db1507629da5301000000333833383334

Esto nos mostrara una información parecida a esta, a nosotros nos
interesa el naa.****\*

   naa.600drtf0001db1507629da5301055555

   Device Type: Direct-Access

   Size: 7629388 MB

   Display Name: DotHill Fibre Channel Disk
   (naa.600drtf0001db1507629da5301055555)

   Multipath Plugin: NMP

   Console Device:
   /vmfs/devices/disks/naa.600drtf0001db1507629da5301055555

   Devfs Path: /vmfs/devices/disks/naa.600drtf0001db1507629da5301055555

   Vendor: DotHill   Model: DH3834            Revis: G105

   SCSI Level: 5  Is Pseudo: false Status: on

   Is RDM Capable: true  Is Removable: false

   Is Local: false Is SSD: false

   Other Names:

   vml.0200460111600c0ff0001db1507629da5301000000333833383334

   VAAI Status: supported

Los siguiente es ver que configuración de PSP tiene el dispositivo, para
ello utilizaremos este comando con el naa.****\* que nos mostró el
comando anterior

   esxcli storage nmp device list
   -d naa.600drtf0001db1507629da5301055555

Esta es la salida del comando anterior, en el que podremos ver el tipo
de PSP en la linea Path selection Policy, en este caso es MRU (Most
Recent Used)

   naa.600drtf0001db1507629da5301055555

   Device Display Name: DotHill Fibre Channel Disk
   (naa.600drtf0001db1507629da5301055555)

   Storage Array Type: VMW_SATP_ALUA

   Storage Array Type Device Config:
   {implicit_support=on;explicit_support=off;
   explicit_allow=on;alua_followover=on;{TPG_id=1,TPG_state=ANO}{TPG_id=0,TPG_state=AO}}

   Path Selection Policy: VMW_PSP_MRU

   Path Selection Policy Device Config: Current Path=vmhba0:C0:T3:L1

   Path Selection Policy Device Custom Config:

   Working Paths: vmhba0:C0:T3:L1

   Is Local SAS Device: false

   Is Boot USB Device: false

Si quisiéramos cambiar el PSP lo haremos mediante este comando, en este
caso la política que aplicaremos sera RR(Round Robin)

   esxcli storage nmp device set -d
   naa.600drtf0001db1507629da5301055555 --psp=VMW_PSP_RR

Volvemos a comprobar que tipo de politica se ha aplicado

   esxcli storage nmp device list
   -d naa.600drtf0001db1507629da5301055555

Aquí vemos como efectivamente esta en RR el PSP

   naa.600drtf0001db1507629da5301055555

   Device Display Name: DotHill Fibre Channel Disk
   (naa.600drtf0001db1507629da5301055555)

   Storage Array Type: VMW_SATP_ALUA

   Storage Array Type Device Config:
   {implicit_support=on;explicit_support=off;
   explicit_allow=on;alua_followover=on;{TPG_id=1,TPG_state=ANO}{TPG_id=0,TPG_state=AO}}

   Path Selection Policy: VMW_PSP_RR

   Path Selection Policy Device Config: Current Path=vmhba0:C0:T3:L1

   Path Selection Policy Device Custom Config:

   Working Paths: vmhba0:C0:T3:L1

   Is Local SAS Device: false

   Is Boot USB Device: false

 

Muchas gracias por leer el blog.
