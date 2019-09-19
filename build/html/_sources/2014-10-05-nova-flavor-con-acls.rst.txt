--- layout: post title: Nova flavor con control de acceso date:
2014-10-05 17:47:42.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - acceso - acl - cloud - control - flavor - flavor_id -
flavor-access-add - flavor-create - list - nova - openstack - tenant_id
meta: \_edit_last: '2' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_thumbnail_id: '615' \_wpas_done_all: '1'
\_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1' \_wpas_skip_8706018:
'1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567023544;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:934;}i:1;a:1:{s:2:"id";i:825;}i:2;a:1:{s:2:"id";i:563;}}}}
author: login: egongu90 email: egongu90@hotmail.com display_name: Editor
first_name: '' last_name: '' permalink: "/nova-flavor-con-acls/" ---

Primero crearemos un "flavor"(sabor) mediante es siguiente comando, este
sabor le haremos privado mediante la opción --is-public=False, un ID
23, con 4vCPU y 4 GB de RAM.

::

   $ nova flavor-create 4vCPU-4GB_Mem 23 4096 0 4 --is-public=False
   +----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
   | ID | Name           | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
   +----+----------------+-----------+------+-----------+------+-------+-------------+-----------+
   | 23 | 4vCPU-4GB_Mem  |  4096     | 0    | 0         |      |     4 | 1.0         |     False |
   +----+----------------+-----------+------+-----------+------+-------+-------------+-----------+

A continuación buscaremos el tenant_ID del tenant al que queramos
asignar el sabor, en este caso el tenant(previamente creado) es prueba

::

   $ keystone tenant-list | grep prueba
   | 41a0db24bc8940b6a2f3297bef5f6cee | prueba | True |

Con el tenant_ID y el flavor_ID, asignaremos el flavor a el tenant, lo
haremos mediante el siguiente comando:

-  23 es flavor_ID
-  41a0db24bc8940b6a2f3297bef5f6cee es tenant_ID

::

   $ nova flavor-access-add 23 41a0db24bc8940b6a2f3297bef5f6cee
   +-----------+----------------------------------+
   | Flavor_ID | Tenant_ID                        |
   +-----------+----------------------------------+
   |        23 | 41a0db24bc8940b6a2f3297bef5f6cee |
   +-----------+----------------------------------+

Por ultimo comprobaremos la lista de sabores, aqui veremos como el
flavor no es publico,  y debería de estar solo disponible para el tenant
asignado anteriormente

::

   $ nova flavor-list
   +----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
   | ID | Name            | Memory_MB | Disk | Ephemeral | Swap | VCPUs | RXTX_Factor | Is_Public |
   +----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+
   | 23 | 4vCPU-4GB_Mem   | 4096      | 0    | 0         |      | 4     | 4.0         | False     |
   +----+-----------------+-----------+------+-----------+------+-------+-------------+-----------+

La información sacada para este post viene de este blog (en ingles),
visitarle si tenéis
ocasión: \ \ http://blog.aaronorosen.com/nova-flavors-with-access-control/
