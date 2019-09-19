--- layout: post title: Convertir claves .pem a .ppk PuTTy AWS date:
2014-09-13 15:40:54.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - amazon - AWS - cloud - convertir - extension - formato - pem -
ppk - private key - putty - puttygen - services - web meta: \_edit_last:
'2' \_thumbnail_id: '631' \_login_radius_meta: '0'
kopa_resolution_total_view: '1' snap_MYURL: '' snapEdIT: '1' snapFB: N;
snap_isAutoPosted: '1' snapTW: N; \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568894637;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:635;}i:1;a:1:{s:2:"id";i:731;}i:2;a:1:{s:2:"id";i:684;}}}}
dsq_thread_id: '6095283686' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/convertir-claves-pem-a-ppk-putty-aws/" ---

Para poder conectarse a Amazon Web Services desde PuTTy, es necesario
que la clave .pem que nos proporciona AWS esté en formato .ppk que es el
que reconoce PuTTy. Para convertir las .pem a .ppk seguiremos los
siguientes pasos: 

Debes tener instalado Putty en el equipo con la tool PuTTygen

Una vez abierta la tool PuTTygen, pulsaremos en LOAD

Nos abrirá el explorador de archivos y marcaremos todos los archivos, ya
que PuTTY solo mostrara las claves .ppk

Seleccionaremos nuestra clave .pem

Por ultimo daremos a Save Private Key, nos preguntara si la queremos
guardar sin contraseña y pulsaremos YES.

Pondremos el mismo nombre que la clave .pem, PuTTY pondrá la extensión
.ppk

Ya estaría la clave creada en formato .ppk para poder conectarnos a AWS
a través de PuTTy
