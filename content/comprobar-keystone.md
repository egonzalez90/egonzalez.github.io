Title: Comprobar Keystone
Date: 2014-12-29 18:14
Author: egongu90
Category: OpenStack
Tags: -, comprobar, instalacion, keystone, list, openstack, role, usr
Slug: comprobar-keystone
Status: published

En anteriores post hemos configurado Keystone(Identity Service), ahora
deberemos de comprobar que este correctamente configurado. Para ello he
creado esta entrada en el blog.

Lo primero que haremos será quitar las variables de entorno con las que
nos autenticábamos en el servicio, con ello nos tendremos que autenticar
con usuario y contraseña.

> unset OS\_SERVICE\_TOKEN OS\_SERVICE\_ENDPOINT

A continuación crearemos el archivo admin-openrc.sh, en el que
configuraremos los datos de nuestro usuario, en este caso el usuario
admin previamente creado. Una vez creado el fichero anterior mediante un
editor de texto, vi, gedit, nano, etc. Incluiremos el siguiente
contenido:

> export OS\_USERNAME=admin
>
> export OS\_PASSWORD=\<adminPASSWORD\>
>
> export OS\_TENANT\_NAME=admin
>
> export OS\_AUTH\_URL=http://controller:35357/v2.0

A continuación, estableceremos las variables de entorno añadidas en el
archivo admin-openrc.sh

> source admin-openrc.sh

Comprobaremos que podemos listar los usuarios y ya de paso comprobamos
que estan bien definidas las variables y por lo tanto estamos utilizando
el usuario admin en esta operación

> keystone user-list

Listamos los roles del usuario admin

> keystone user-role-list --user=admin --tenant=admin

Estos dos últimos comandos nos mostraran una información, en la que
comprobaremos que el ID del usuario admin esta en el rol de admin y
\_member\_

 

Si todo lo anterior salió correctamente quiere decir que tenemos la
configuración básica de Identity Service correctamente realizada y
podremos seguir configurando mas servicios en nuestro entorno
