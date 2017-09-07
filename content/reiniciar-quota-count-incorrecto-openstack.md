Title: Reiniciar quota count incorrecto Openstack
Date: 2014-09-07 15:50
Author: egongu90
Category: OpenStack
Tags: bbdd, cloud, count, cuenta, cuota, error, ID, incorrecto, nova, openstack, quota, reinicio, reset, tenant, usage
Slug: reiniciar-quota-count-incorrecto-openstack
Status: published

Para reiniciar quota count, deberemos conectarnos a la base de datos y
establecer in\_use en "-1"

> mysql -u nova -p\<password\> nova
>
> select\*from quota\_usages;
>
> update quota\_usages set in\_use='-1'where project\_id='\<my project
> id\>';

A partir de la versión Icehouse, ya no se usa -1 y se pasa a usar 0

> update quota\_usages set in\_use='0'where project\_id='\<my project
> id\>';
