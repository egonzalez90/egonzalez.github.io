Title: Usuarios, Tenants y Roles
Date: 2014-11-28 16:22
Author: egongu90
Category: OpenStack
Tags: add, admin, create, demo, keystone, openstack, role, service, tenant, user
Slug: usuarios-tenants-y-roles
Status: published

Una vez tenemos instalado el servicio de Keystone, deberemos crear el
usuario de administración, su rol y su tenant. Para ello seguiremos los
siguientes pasos:

Como aun no tenemos el usuario de administración, utilizaremos
ADMIN\_TOKEN para poder utilizar comandos de keystone. Introduciremos
estos comandos para establecer ADMIN\_TOKEN y el ENDPOINT del servicio:

> export OS\_SERVICE\_TOKEN=\$ADMIN\_TOKEN
>
> export OS\_SERVICE\_ENDPOINT=http://controller:35357/v2.0

USUARIO ADMIN
-------------

A continuación crearemos el usuario Admin mediante el siguiente comando:

> keystone user-create --name=admin --pass=PASSWORD
> --email=mail@mail.com

Una vez creado el usuario deberemos crear el rol de administración

> keystone role-create --name=admin

El siguiente es crear el tenant de administración

> keystone tenant-create --name=admin --description"Admin Tenant"

Una vez creados el usuario, rol y tenant de administración, deberemos
 asignárselos al usuario Admin

> keystone user-role-add --user=admin --tenant=admin

Ahora asignaremos al usuario Admin el rol de \_member\_

> keystone user-role-add --user=admin --role=\_member\_ --tenant=admin

USUARIOS NORMALES
-----------------

Ya tenemos el usuario de administración, ahora crearemos usuarios
"normales"

Crearemos un usuario llamado demo

> keystone user-create --name=demo --pass=PASSWORD
> --email=demomail@mail.com

Creamos el tenant demo

> keystone tenant-create --name=demo --description="Demo Tenant"

\#No volver a crear este mismo tenant cuando se creen otros usuarios que
pertenezcan a el

Asignaremos rol y tenant al usuario demo

> keystone user-role-add --name=demo --role\_\_member\_ tenant=demo

TENANT SERVICE
--------------

Crearemos el tenant "Service" para los servicios de nuestra instalación
de Openstack

> keystone tenant-create --name=service --description="Service Tenant"

Con esto ya tendríamos los tenants, roles y usuarios básicos para
nuestro entorno.

Un saludo
