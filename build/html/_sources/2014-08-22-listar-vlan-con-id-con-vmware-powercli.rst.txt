--- layout: post title: Listar vlan ID con VMware PowerCLI date:
2014-08-22 15:59:41.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: -
Virtualizacion tags: - all vlan - CLI - CSV - esxi - Excel - host - ID -
list portgroup id - list vlan - listar - portgroup - powercli - todas
vlan - virtualizacion - Vlan - vlan id - vmware meta: \_edit_last: '2'
\_login_radius_meta: a:1:{s:7:"sharing";i:0;} \_layout: inherit
snap_MYURL: '' snapEdIT: '1' snapFB: N; snap_isAutoPosted: '1' snapTW:
N; kopa_resolution_total_view: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568623815;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:513;}i:1;a:1:{s:2:"id";i:545;}i:2;a:1:{s:2:"id";i:769;}}}}
dsq_thread_id: '6188717945' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/listar-vlan-con-id-con-vmware-powercli/" ---

Para poder listar todas las VLans de un host ESXi con su ID primero nos
deberemos conectar a ese host por PowerCLI, usaremos este comando:

   Connect_VIServer -server "host" -user "usuario" -password
   "contraseña"

Una vez conectados a dicho ESXi, utilizaremos el siguiente comando con
el que listaremos las vlans y los ID, ademas lo exportaremos a un
formato CSV para poder analizarlo con Excel

   Get-VirtualPortGroup -VMHost "Host" \| Select Name, VirtualSwitch,
   VLanId \| Export-Csv C:nombre.csv

Espero les sirva, un saludo
