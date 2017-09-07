Title: Primera instancia
Date: 2015-02-23 13:24
Author: egongu90
Category: OpenStack
Tags: crear, habilitar, icehouse, icmp, instancias, openstack, ping, primera, security group, ssh, ssh-keygen, vnc
Slug: primera-instancia
Status: published

Primero creamos la clave.

> \# ssh-keygen

Añadimos la clave creada a openstack.

> \# nova keypair-add --pub-key \~/.ssh/id\_rsa.pub [nombre]

Comprobamos que está asociada en nuestro entorno.

> \# nova keypair-list

Para crear instancias necesitaremos los siguientes valores:

-   Flavors (\# nova flavor-list)
-   Imagenes (\# nova image-list)
-   Networks (\# nova net-list)
-   securityGroups (\# nova secgroup-list)

Una vez tenemos esos valores necesarios procederemos a crear una
instancia.

> \# nova boot --flavor [flavor] --image [image\_ID] --nic
> net-id=[net\_ID] --security-group [SecGroup] --key-name [keyname]
> [NombreInstancia]

Ejemplo:

> nova boot --flavor m1.tiny --image cirros-0.3.2-x86\_64 --nic
> net-id=[NET\_ID] --security-group default --key-name demo-key
> Instancia1

Comprobremos el estado de la instancia.

> \# nova list

Crearemos una sesion por VNC.

> \# nova get-vnc-console [Instancia] novnc

Habilitamos Ping y SSH al Security Group "Default".

> \# nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0
>
> \# nova secgroup-add-rule default tcp 22 22 0.0.0.0/0

Comprobamos las conexiones por ping y por SSH.

> \# ssh cirros@IP
>
> \*Password por defecto cubswin:)
