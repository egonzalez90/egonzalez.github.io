--- layout: post title: Alineamiento MBR maquinas virtuales date:
2014-09-03 15:21:58.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Linux -
Virtualizacion tags: - alinear - esxi - ext3 - ext4 - grub - maquina
virtual - mbr - mbralign - mbrscan - netapp - redhat - rhel - VM - vmfs
- vmware - volumes meta: \_edit_last: '2' \_login_radius_meta:
a:1:{s:7:"sharing";i:0;} kopa_resolution_total_view: '18'
snap_isAutoPosted: '1' snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW:
N; post_views_count: '4' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1566772089;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:559;}i:1;a:1:{s:2:"id";i:605;}i:2;a:1:{s:2:"id";i:527;}}}}
dsq_thread_id: '6218298245' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/alineamiento-mbr-maquinas-virtuales/" ---

Antes de la llegada de el sistema de ficheros EXT4, cuando creabas
maquinas virtuales, estas estaban desalineadas el mbr del vmfs y de el
almacenamiento,  lo que generaba menor rendimiento.

Para ello dedico esta entrada, con la que mostrare como alinear el mbr.

Lo primero que necesitaremos es el paquete con las tools mbrscan y
mbralign, este paquete le copiaremos a el directorio /opt/ontap/ de un
host ESXi que tenga acceso al almacenamiento donde tenemos la maquina
guardada.

Una vez copiado el paquete a dicho directorio pasaremos a escanear y a
realinear el mbr de la maquina, para ello necesitamos que este apagada.

Una vez apagada iremos al directorio /opt/ontap/ y ejecutaremos el
siguiente comando con el que analizaremos el disco de la maquina para
ver si necesita ser alineado.

   ./mbrscan
   /vmfs/volumes/ALMACENAMIENTO/maquinavirtual/maquinavirtual-flat.vmdk

Esto nos mostrara un mensaje en el que pondra:

   Aligned yes o Aligned no

En el caso de que pusiera align no, deberemos realinear el mbr de la
maquina, lo haremos mediante este comando:

   ./mbralign
   /vmfs/volumes/ALMACENAMIENTO/maquinavirtual/maquinavirtual-flat.vmdk

Esto nos creara un archivo .bak del disco que vamos a alinear por si
fallara este proceso poder recuperarlo, este proceso tardara
bastante(dependiendo del tamaño del disco)

Una vez acabado ese proceso de alineamiento, volveremos a utilizar el
comando mbrscan para comprobar que este bien hecho.

Por ultimo, el alineado del mbr se carga totalmente el GRUB de la
maquina, por lo que deberemos recuperarlo.

En esta entrada tienes como
hacerlo: \ `http://egonzalez.org/recuperar-grub-rhel-y-centos/  <http://egonzalez.org/recuperar-grub-rhel-y-centos/%20>`__

Una vez recuperado el GRUB y comprobado que la maquina funciona
correctamente, borraremos el archivo .bak que se había creado.

Espero poder ayudar, un saludo
