--- layout: post title: Comprobar Keystone date: 2014-12-29
18:14:32.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - "-" -
comprobar - instalacion - keystone - list - openstack - role - usr meta:
\_edit_last: '2' \_thumbnail_id: '615' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_wpas_skip_10228321: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567152095;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:825;}i:1;a:1:{s:2:"id";i:859;}i:2;a:1:{s:2:"id";i:816;}}}}
dsq_thread_id: '6110320358' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/comprobar-keystone/" ---

En anteriores post hemos configurado Keystone(Identity Service), ahora
deberemos de comprobar que este correctamente configurado. Para ello he
creado esta entrada en el blog.

Lo primero que haremos será quitar las variables de entorno con las que
nos autenticábamos en el servicio, con ello nos tendremos que autenticar
con usuario y contraseña.

   unset OS_SERVICE_TOKEN OS_SERVICE_ENDPOINT

A continuación crearemos el archivo admin-openrc.sh, en el que
configuraremos los datos de nuestro usuario, en este caso el usuario
admin previamente creado. Una vez creado el fichero anterior mediante un
editor de texto, vi, gedit, nano, etc. Incluiremos el siguiente
contenido:

   export OS_USERNAME=admin

   export OS_PASSWORD=<adminPASSWORD>

   export OS_TENANT_NAME=admin

   export OS_AUTH_URL=http://controller:35357/v2.0

A continuación, estableceremos las variables de entorno añadidas en el
archivo admin-openrc.sh

   source admin-openrc.sh

Comprobaremos que podemos listar los usuarios y ya de paso comprobamos
que estan bien definidas las variables y por lo tanto estamos utilizando
el usuario admin en esta operación

   keystone user-list

Listamos los roles del usuario admin

   keystone user-role-list --user=admin --tenant=admin

Estos dos últimos comandos nos mostraran una información, en la que
comprobaremos que el ID del usuario admin esta en el rol de admin y
\_member\_

 

Si todo lo anterior salió correctamente quiere decir que tenemos la
configuración básica de Identity Service correctamente realizada y
podremos seguir configurando mas servicios en nuestro entorno
