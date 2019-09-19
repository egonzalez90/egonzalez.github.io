--- layout: post title: Montar directorio NFS date: 2014-09-05
15:46:24.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux tags: - centos -
default - df -h - directorio - fstab - linux - montar - mount - nfs -
red hat - rhel meta: \_edit_last: '2' \_thumbnail_id: '557'
\_login_radius_meta: a:1:{s:7:"sharing";i:0;}
kopa_resolution_total_view: '1' snap_MYURL: '' snapEdIT: '1' snapFB: N;
snap_isAutoPosted: '1' snapTW: N; \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567154216;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:662;}i:1;a:1:{s:2:"id";i:338;}i:2;a:1:{s:2:"id";i:781;}}}}
dsq_thread_id: '6194166188' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/montar-directorio-nfs/" ---

Primero crearemos la carpeta en donde vamos a montar el directorio NFS

   mkdir /rutadondemontareldirectorio

A continuación utilizaremos este comando para montar el directorio NFS
en la carpeta creada anteriormente.

SERVIDOR puede ser tanto hostname como IP(yo siempre prefiero utilizar
IP)

   mount SERVIDOR:/ruta/a/la/carpeta /rutadondemontareldirectorio

Una vez montado sin darnos ningún error, utilizaremos este comando para
comprobar que nos mostrara los directorios que están montados en nuestro
sistema y que tamaño tienen

   df -h

Ahora que ya hemos montado el directorio NFS, lo incluiremos en fstab
para que se monte siempre en el arranque del sistema sin tener que
hacerlo manualmente por los pasos anteriores, para ello modificaremos
este archivo

   vi /etc/fstab

Dentro del archivo incluiremos esta linea y guardaremos

   SERVIDOR:/ruta/a/la/carpeta            /rutadondemontareldirectorio  
            default            0 0

Podemos comprobar que el archivo fstab funciona correctamente utilizando
el mismo comando de antes para ver los directorios montados y su tamaño,
pero esta vez lo haremos una vez encendida la maquina, sin haber montado
el directorio NFS de forma manual

   df -h
