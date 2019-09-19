--- layout: post title: ELB en AWS (Elastic Load Balancers) date:
2014-09-25 16:43:42.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - amazon - automatizar - AWS - Balancers - cloud - crear -
distribuir - ELB - http - instancias - Load - Services; Elastic -
trafico - virtualizacion - web meta: \_edit_last: '2' \_thumbnail_id:
'631' snap_MYURL: '' snapEdIT: '1' snapFB: N; snapTW: N;
\_wpas_done_all: '1' \_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568756471;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:635;}i:1;a:1:{s:2:"id";i:674;}i:2;a:1:{s:2:"id";i:630;}}}}
dsq_thread_id: '6239307173' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/elb-en-aws-elastic-load-balancers/" ---

Hoy mostraré como crear Elastic Load Balancer (ELB) en Amazon Web
Services el cual nos permitirá distribuir automáticamente el trafico
entre las aplicaciones de las distintas instancias y obtener una mejor
tolerancia a fallos.

Primero nos logearemos en AWS e iremos a la pestaña EC2, una vez a, aquí
pulsaremos sobre Load Balancers del menú izquierdo.

Se nos abrirá esta ventana en la que pulsaremos Create Load Balancer
para configurar un ELB nuevo. En esta misa ventana nos mostraría los ELB
ya creados

`01 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/011.png>`__

Una vez abierto Create Load Balancer, rellenaremos el Nombre del ELB a
crear y estableceremos los protocolos que soportara el ELB, por defecto
viene activado HTTP por el puerto 80

`02 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/021.png>`__

En esta próxima pantalla configuraremos los análisis de salud de
nuestras instancias, para ello ajustaremos los parámetros inferiores a
nuestro gusto

`03 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/031.png>`__

Aquí asignaremos o crearemos un Security Group, en mi caso utilizare uno
ya existente

`04 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/041.png>`__

Lo ultimo que configuraremos serán las instancias que harán uso del ELB,
seleccionamos las que queramos y pulsaremos en Continue

`05 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/051.png>`__

Finalizaremos estableciendo una etiqueta a nuestro ELB

`06 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/061.png>`__

Antes de terminar de crear el ELB, nos mostrara una resumen de la
configuración, si estuviéramos de acuerdo pulsaríamos en Create, de lo
contrario modificaremos alguna de las partes anteriores

`07 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/071.png>`__

Esta seria una imagen del ELB creado, tendremos que esperar un rato
hasta que este activo, una vez activo veremos In Service el Status de
las Instancias, aunque en algunas ocasiones aunque este In Service aun
no tenemos conexión a través del ELB

`08 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/081.png>`__

Un saludo
