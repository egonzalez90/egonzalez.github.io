--- layout: post title: Instalar aws-cli date: 2014-10-03
17:11:26.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - Linux - OpenStack tags: -
access key - amazon - AWS - awscli - cloud - configurar - instalar -
linux - region - secret - services - web meta: \_edit_last: '2'
\_publicize_facebook_user: https://www.facebook.com/dudu.gonzalez90
\_publicize_twitter_user: "@hidanstillalive" \_thumbnail_id: '631'
\_wpas_done_all: '1' \_wpas_skip_5226565: '1' \_wpas_skip_4949654: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568601398;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:705;}i:1;a:1:{s:2:"id";i:866;}i:2;a:1:{s:2:"id";i:635;}}}}
dsq_thread_id: '6094296936' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/instalar-aws-cli/" ---

AWS-cli es una potente línea de comandos que permite interactuar con
todos los servicios de AWS, en esta entrada mostrare como instalarlo en
un Ubuntu Server.

--------------

Esto mismo lo podrás instalar en RHEL cambiando el gestor de paquetes
apt por yum.

Primero instalaremos python y pip

   sudo apt-get install -y python-pip

A continuación instalaremos awscli con pip

   sudo pip install awscli

Después configuraremos awscli para que conecte con nuestra cuenta de AWS

   aws configure

Aquí introduciremos los siguientes parámetros:

-  Access Key ID: En el archivo credentials que se descarga al crear una
   nueva Access Key en IAM
-  Secret Access Key: En el archivo credentials que se descarga al crear
   una nueva Access Key en IAM
-  Region Name: La region de EC2 (no la zona de disponibilidad), es
   importante no poner el ultimo dígito(a,b,c,d) porque dará error de
   configuración y no conectará
-  Output format: Formato en que queremos que nos muestre los datos
   awscli, lo normal suele ser table o text

..

   | AWS Access Key ID [None]: AK***XCLG******XYR7A
   | AWS Secret Access Key [None]:
     m*********q**********r5Zpyqsb*********AOL
   | Default region name [None]: eu-west-1
   | Default output format [None]: table

Por ultimo probaremos que funciona, listando las regiones que tenemos
disponibles, si este comando funciona quiere decir que esta bien
configurado

   aws ec2 describe-regions

.. raw:: html

   <div>

.. raw:: html

   <div>

`describe-regions <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/describe-regions.png>`__

 

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   </div>

Un saludo
