--- layout: post title: Crear Plantilla AMI en AWS date: 2014-09-22
09:14:24.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - amazon -
AMI - AWS - cloud - computing - crear - ejecutar - hybrid - imagen -
instancia - launch - plantilla - private - public - services - web meta:
\_edit_last: '2' \_thumbnail_id: '631' snap_MYURL: '' snapEdIT: '1'
snapFB: N; snapTW: N; \_wpas_done_all: '1' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567454923;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:777;}i:1;a:1:{s:2:"id";i:769;}i:2;a:1:{s:2:"id";i:635;}}}}
dsq_thread_id: '6102557899' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/crear-plantilla-ami-en-aws/" ---

El primer paso es estar logeado en AWS, y en la pestaña Instances de
EC2.

Una vez aquí pulsaremos con el botón derecho sobre la instancia que
queremos convertir en plantilla AMI.

Aquí pulsaremos sobre Create Image\ `Captura
 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura.png>`__

Lo siguiente sera ponerle un nombre a la plantilla y una descripcion,
para finalizar le daremos a Create Image

`Captura2 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura2.png>`__

A continuación nos mostrara un mensage que indica que esta en proceso de
creacion, pulsaremos sobre View Pending Image \***\* para ver el estado
de la peticion

`Captura3  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura3.png>`__\ En
esta ventana veremos el estado de la peticion, una vez acabada la
creacion de la plantilla aparecera en verde Available, estos sencillos
pasos nos permitiran tener imagenes personalizadas para ejecutar tantas
instancias como queramos sobre esa plantilla

`Captura4 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura4.png>`__ Para
ejecutar la imagen como una instancia, solo tienes que pulsar sobre
Launch y crear la instancia como cualquier otra.

Si quieres saber como se crea una instancia puedes hacerlo siguiendo
esta entrada del blog: \ http://egonzalez.org/?p=635
