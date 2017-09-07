Title: Instalar aws-cli
Date: 2014-10-03 17:11
Author: egongu90
Category: Linux, OpenStack
Tags: access key, amazon, AWS, awscli, cloud, configurar, instalar, linux, region, secret, services, web
Slug: instalar-aws-cli
Status: published

AWS-cli es una potente línea de comandos que permite interactuar con
todos los servicios de AWS, en esta entrada mostrare como instalarlo en
un Ubuntu Server.<!--more-->

* * * * *

Esto mismo lo podrás instalar en RHEL cambiando el gestor de paquetes
apt por yum.

Primero instalaremos python y pip

> sudo apt-get install -y python-pip

A continuación instalaremos awscli con pip

> sudo pip install awscli

Después configuraremos awscli para que conecte con nuestra cuenta de AWS

> aws configure

Aquí introduciremos los siguientes parámetros:

-   Access Key ID: En el archivo credentials que se descarga al crear
    una nueva Access Key en IAM
-   Secret Access Key:<span style="line-height: 20.7999992370605px;"> En
    el archivo credentials que se descarga al crear una nueva Access Key
    en IAM</span>
-   Region Name: La region de EC2 (no la zona de disponibilidad), es
    importante no poner el ultimo dígito(a,b,c,d) porque dará error de
    configuración y no conectará
-   Output format: Formato en que queremos que nos muestre los datos
    awscli, lo normal suele ser table o text

> AWS Access Key ID [None]: AK\*\*\*XCLG\*\*\*\*\*\*XYR7A  
>  AWS Secret Access Key [None]:
> m\*\*\*\*\*\*\*\*\*q\*\*\*\*\*\*\*\*\*\*r5Zpyqsb\*\*\*\*\*\*\*\*\*AOL  
>  Default region name [None]: eu-west-1  
>  Default output format [None]: table

Por ultimo probaremos que funciona, listando las regiones que tenemos
disponibles, si este comando funciona quiere decir que esta bien
configurado

> aws ec2 describe-regions

<div>

<div>

[![describe-regions](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/describe-regions.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/describe-regions.png)

 

</div>

<div>

</div>

</div>

Un saludo
