Title: Nova flavor con control de acceso
Date: 2014-10-05 17:47
Author: egongu90
Category: OpenStack
Tags: acceso, acl, cloud, control, flavor, flavor_id, flavor-access-add, flavor-create, list, nova, openstack, tenant_id
Slug: nova-flavor-con-acls
Status: published

Primero crearemos un "flavor"(sabor) mediante es siguiente comando, este
sabor le haremos privado mediante la opción --is-public=False, un ID
23, con 4vCPU y 4 GB de RAM.<!--more-->

``` {style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;"}
$ nova flavor-create 4vCPU-4GB_Mem 23 4096 0 4 --is-public=False
+----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
| ID | Name           | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
| 23 | 4vCPU-4GB_Mem  |  4096     | 0    | 0         |      |     4 | 1.0         |     False |
+----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
```

A continuación buscaremos el tenant\_ID del tenant al que queramos
asignar el sabor, en este caso el tenant(previamente creado) es prueba

``` {style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;"}
$ keystone tenant-list | grep prueba
| 41a0db24bc8940b6a2f3297bef5f6cee | prueba | True |
```

Con el tenant\_ID y el flavor\_ID, asignaremos el flavor a el tenant, lo
haremos mediante el siguiente comando:

-   23 es flavor\_ID
-   41a0db24bc8940b6a2f3297bef5f6cee es tenant\_ID

``` {style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;"}
$ nova flavor-access-add 23 41a0db24bc8940b6a2f3297bef5f6cee
+-----------+----------------------------------+
| Flavor_ID | Tenant_ID                        |
+-----------+----------------------------------+
|        23 | 41a0db24bc8940b6a2f3297bef5f6cee |
+-----------+----------------------------------+
```

Por ultimo comprobaremos la lista de sabores, aqui veremos como el
flavor no es publico,  y debería de estar solo disponible para el tenant
asignado anteriormente

``` {style="border: 0px; margin-top: 0px; margin-bottom: 24px; padding: 1.5em; vertical-align: baseline; font-family: 'Courier 10 Pitch', Courier, monospace; color: #222222; line-height: 21px; overflow: auto; font-size: 15px; background: #f7f7f7;"}
$ nova flavor-list
+----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
| ID | Name            | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
+----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
| 23 | 4vCPU-4GB_Mem   | 4096      | 0    | 0         |      | 4     | 4.0         | False     |
+----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
```

<span style="font-size: 14px; line-height: 22.3999996185303px;">La
información sacada para este post viene de este blog (en ingles),
visitarle si tenéis
ocasión: <http://blog.aaronorosen.com/nova-flavors-with-access-control/></span>
