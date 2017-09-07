Title: Diferencias entre Quota y Limit Openstack
Date: 2014-08-25 13:33
Author: egongu90
Category: OpenStack
Tags: cloud, computing, diference, diferencia, limit, limite operacional, nova, openstack, que es, quota, quota-defaults
Slug: diferencias-entre-quota-y-limit-openstack
Status: published

Las quotas en OpenStack se usan para evitar la saturacion de las
capacidades del sistema, por ejemplo el máximo de GB permitidos a un
tenant(o proyecto), de esta forma se controlará mas y se tendrá un
rendimiento optimo de nuestra nube.  
Mucha gente no sabe cual es la diferencia entre estos dos terminos en
OpenStack, pues bien, para hacerlo mas visual lanzaremos el comando:

``` {.prettyprint}
$ nova quota-defaults
+-----------------------------+-------+
|Quota                        | Limit |
+-----------------------------+-------+
| instances                   |  10   |
| cores                       |  20   |
| ram                         |  51200|
| floating_ips                |  10   |
| fixed_ips                   |  -1   |
| metadata_items              |  128  |
| injected_files              |  5    |
| injected_file_content_bytes |  10240|
| injected_file_path_bytes    |  255  |
| key_pairs                   |  100  |
| security_groups             |  10   |
| security_group_rules        |  20   |
+-----------------------------+-------+
```

Este comando nos muestra 2 columnas delimitadas, en una Quota y en otra
Limit

\* Quota es el nombre del limite operacional  
\* Limit son los valores limite de las quotas, lo que es lo mismo, el
valor del limite operacional que se le va a poder asignar a un tenant o
proyecto

Visto asi es mas facil de asimilarlo en nuestra cabeza para un mejor
entendimiento ¿verdad?  
Espero haber ayudado en vuestras dudas, un saludo
