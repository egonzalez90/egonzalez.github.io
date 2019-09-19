--- layout: post title: Primera instancia date: 2015-02-23
13:24:48.000000000 +01:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - crear -
habilitar - icehouse - icmp - instancias - openstack - ping - primera -
security group - ssh - ssh-keygen - vnc meta: \_edit_last: '2'
\_wpas_mess: Primera instancia \_wpas_skip_10228321: '1'
\_wpas_skip_5226565: '1' \_wpas_done_all: '1' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@egongu90" \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567580562;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:769;}i:1;a:1:{s:2:"id";i:718;}i:2;a:1:{s:2:"id";i:635;}}}}
dsq_thread_id: '6110714285' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/primera-instancia/" ---

Primero creamos la clave.

   # ssh-keygen

Añadimos la clave creada a openstack.

   # nova keypair-add --pub-key ~/.ssh/id_rsa.pub [nombre]

Comprobamos que está asociada en nuestro entorno.

   # nova keypair-list

Para crear instancias necesitaremos los siguientes valores:

-  Flavors (# nova flavor-list)
-  Imagenes (# nova image-list)
-  Networks (# nova net-list)
-  securityGroups (# nova secgroup-list)

Una vez tenemos esos valores necesarios procederemos a crear una
instancia.

   # nova boot --flavor [flavor] --image [image_ID] --nic
   net-id=[net_ID] --security-group [SecGroup] --key-name [keyname]
   [NombreInstancia]

Ejemplo:

   nova boot --flavor m1.tiny --image cirros-0.3.2-x86_64 --nic
   net-id=[NET_ID] --security-group default --key-name demo-key
   Instancia1

Comprobremos el estado de la instancia.

   # nova list

Crearemos una sesion por VNC.

   # nova get-vnc-console [Instancia] novnc

Habilitamos Ping y SSH al Security Group "Default".

   # nova secgroup-add-rule default icmp -1 -1 0.0.0.0/0

   # nova secgroup-add-rule default tcp 22 22 0.0.0.0/0

Comprobamos las conexiones por ping y por SSH.

   # ssh cirros@IP

   \*Password por defecto cubswin:)
