--- layout: post title: Añadir repositorios EPEL RHEL y CentOS date:
2014-09-09 15:32:52.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Linux tags: -
añadir - centos - descargar - enablerepo - epel - fedoraproject -
instalar - red hat - repolist - repositorios - rhel meta: \_edit_last:
'2' \_login_radius_meta: '0' kopa_resolution_total_view: '3'
\_thumbnail_id: '557' snap_MYURL: '' snapEdIT: '1' snapFB: N;
snap_isAutoPosted: '1' snapTW: N; \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567706341;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:759;}i:1;a:1:{s:2:"id";i:806;}i:2;a:1:{s:2:"id";i:705;}}}}
dsq_thread_id: '6266827116' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/anadir-repositorios-epel-rhel-y-centos/" ---

Primero descargaremos el repositorio para nuestra versión de CentOS o
RHEL mediante wget.

A continuacion instalaremos el paquete que habiamos descargado con rpm.

Esta son las diferentes versiones de CentOS y RHEL

   | ## RHEL/CentOS 7 64-Bit ##
   | #
     wget http://mirror.rackcentral.com.au/epel/7/x86_64/epel-release-7-1.noarch.rpm
   | # rpm -ivh epel-release-7-0.2.noarch.rpm

 

   | ## RHEL/CentOS 6 32-Bit ##
   | #
     wget http://mirror.rackcentral.com.au/epel/6/i386/epel-release-6-8.noarch.rpm
   | # rpm -ivh epel-release-6-8.noarch.rpm

 

   | ## RHEL/CentOS 6 64-Bit ##
   | #
     wget http://mirror.rackcentral.com.au/epel/6/x86_64/epel-release-6-8.noarch.rpm
   | # rpm -ivh epel-release-6-8.noarch.rpm

Lo siguiente que haremos sera comprobar que esta en la lista de
repositorios mediante este comando

   yum repolist

Por ultimo habilitaremos el repositorio, para que podamos usarlo
habitualmente

   yum --enablerepo=epel
