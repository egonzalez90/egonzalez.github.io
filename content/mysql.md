Title: MySQL
Date: 2014-11-02 16:01
Author: egongu90
Category: OpenStack
Tags: bbdd, compute, configuracion, controller. network, instalacion, mysql, openstack
Slug: mysql
Status: published

MySQL en Controller node
------------------------

Instalamos MySQL

> yum install mysql mysql-server MySQL-python

Editamos el fichero de configuracion de MySQL

> vi /etc/my.cnf

Modificamos la linea bind-address con la IP de eth0 y añadimos las
siguientes entradas:

> [mysqld]
>
> bind-address=192.168.1.11
>
> default-storage-engine=innodb
>
> innodb\_file\_per\_table
>
> collation-server=utf8\_general\_ci
>
> init-connect='SET NAMES utf8'
>
> character-set-server=utf8

Iniciamos el servicio mysqld y lo añadimos al arranque del sistema

> service mysqld start
>
> chkconfig mysqld on

Instalamos la base de datos nueva, establecemos contraseña de root y
quitamos los usuarios anónimos. El primer comando puede no ser necesario
a no ser que el segundo comando nos diera error

> mysql\_install\_db
>
> mysql\_secure\_installation

Nodos Network y Compute
-----------------------

En estos nodos solamente necesitamos instalar el paquete MySQL-python

> yum install MySQL-python

 

Un saludo
