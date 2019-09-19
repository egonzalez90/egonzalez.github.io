--- layout: post title: s3cmd, administración bucket AWS date:
2014-09-29 18:42:28.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - Linux -
OpenStack tags: - "--configure" - access denied - access key - amazon -
AWS - cloud - configurar - IAM - instalar - permisos - policy - s3cmd -
s3tools - secret key - services - usuario - web meta: \_edit_last: '2'
\_oembed_1f9db5030b8a2258f64c9c5b2420f35e: "{{unknown}}"
\_publicize_facebook_user: https://www.facebook.com/dudu.gonzalez90
\_publicize_twitter_user: "@hidanstillalive" \_thumbnail_id: '631'
\_wpas_done_all: '1' \_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568779125;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:759;}i:1;a:1:{s:2:"id";i:731;}i:2;a:1:{s:2:"id";i:616;}}}}
dsq_thread_id: '6096578804' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/s3cmd-administracion-bucket-aws/" ---

Buenos días, en esta entrada mostrare el proceso para instalar s3cmd con
el que podremos administrar nuestros contenedores de AWS.

Para ello primero deberemos localizar el repositorio para la versión de
nuestro RHEL, lo podéis hacer en este enlace:
http://s3tools.org/repositories

En mi caso uso la versión 6.5 de RHEL, por lo que usare el repositorio
de la versión 6, descargaremos el archivo .repo acorde con nuestra
versión, cambiando el enlace por el proporcionado por la pagina anterior
si fuera otra versión fuera de la 6

   wget http://s3tools.org/repo/RHEL_6/s3tools.repo

A continuación moveremos el archivo .repo a la localización de los
repositorios en el SO, este paso se puede saltar si el comando wget se
lanza desde el mismo directorio /etc/yum.repos.d/

   mv s3tools.repo /etc/yum.repos.d/

Ahora actualizaremos la lista de repositorios para que el SO la
reconozca

   sudo yum repolist

Después instalaremos s3cmd mediante el siguiente comando

   sudo yum install s3cmd

Para acabar, procederemos a configurar s3cmd para que pueda acceder a
nuestros contenedores en AWS

   s3cmd --configure

 

   ::

      Enter new values or accept defaults in brackets with Enter.
      Refer to user manual for detailed description of all options.

      Access key and Secret key are your identifiers for Amazon S3
      Access Key: xxxxxxxxxxxxxxxxxxxxxx
      Secret Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

      Encryption password is used to protect your files from reading
      by unauthorized persons while in transfer to S3
      Encryption password: xxxxxxxxxx
      Path to GPG program [/usr/bin/gpg]:

      When using secure HTTPS protocol all communication with Amazon S3
      servers is protected from 3rd party eavesdropping. This method is
      slower than plain HTTP and can't be used if you're behind a proxy
      Use HTTPS protocol [No]: Yes

      New settings:
        Access Key: xxxxxxxxxxxxxxxxxxxxxx
        Secret Key: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        Encryption password: xxxxxxxxxx
        Path to GPG program: /usr/bin/gpg
        Use HTTPS protocol: True
        HTTP Proxy server name:
        HTTP Proxy server port: 0

      Test access with supplied credentials? [Y/n] Y
      Please wait, attempting to list all buckets...
      Success. Your access key and secret key worked fine :-)

      Now verifying that encryption works...
      Success. Encryption and decryption worked fine :-)

      Save settings? [y/N] y
      Configuration saved to '/root/.s3cfg'

Access Key la puedes encontrar en: Security Credentials/ Users/ Access
Credentials

`access <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/access.png>`__

Secret Key solo se puede descargar una única vez, al crear las claves de
acceso, si fuera necesario, deberías de crear unas nuevas para poder
obtener Secret Key para esa clave.

Seguramente que te de un error si lanzas el comando ahora, para que no
te de el error Access Denied, tienes que agregar una política de usuario
con permisos

`userpolicy <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/userpolicy.png>`__

Por ultimo probaremos que tenemos acceso a los bucket

   s3cmd ls

Esto nos debería de mostrar los contenedores a los que tenemos permisos
dentro de AWS

Ahora solo te queda investigar las diferentes posibilidades que te da
s3cmd

Un saludo
