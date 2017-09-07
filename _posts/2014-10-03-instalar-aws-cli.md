---
id: 731
title: Instalar aws-cli
date: 2014-10-03T17:11:26+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=731
permalink: /instalar-aws-cli/
dsq_thread_id:
  - "6094296936"
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - Linux
  - OpenStack
tags:
  - access key
  - amazon
  - AWS
  - awscli
  - cloud
  - configurar
  - instalar
  - linux
  - region
  - secret
  - services
  - web
---
AWS-cli es una potente línea de comandos que permite interactuar con todos los servicios de AWS, en esta entrada mostrare como instalarlo en un Ubuntu Server.<!--more-->

<hr />

Esto mismo lo podrás instalar en RHEL cambiando el gestor de paquetes apt por yum.

Primero instalaremos python y pip
<blockquote>sudo apt-get install -y python-pip</blockquote>
A continuación instalaremos awscli con pip
<blockquote>sudo pip install awscli</blockquote>
Después configuraremos awscli para que conecte con nuestra cuenta de AWS
<blockquote>aws configure</blockquote>
Aquí introduciremos los siguientes parámetros:
<ul>
	<li>Access Key ID: En el archivo credentials que se descarga al crear una nueva Access Key en IAM</li>
	<li>Secret Access Key:<span style="line-height: 20.7999992370605px;"> En el archivo credentials que se descarga al crear una nueva Access Key en IAM</span></li>
	<li>Region Name: La region de EC2 (no la zona de disponibilidad), es importante no poner el ultimo dígito(a,b,c,d) porque dará error de configuración y no conectará</li>
	<li>Output format: Formato en que queremos que nos muestre los datos awscli, lo normal suele ser table o text</li>
</ul>
<blockquote>AWS Access Key ID [None]: AK***XCLG******XYR7A
AWS Secret Access Key [None]: m*********q**********r5Zpyqsb*********AOL
Default region name [None]: eu-west-1
Default output format [None]: table</blockquote>
Por ultimo probaremos que funciona, listando las regiones que tenemos disponibles, si este comando funciona quiere decir que esta bien configurado
<blockquote>aws ec2 describe-regions</blockquote>
<div>
<div>

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/describe-regions.png"><img class="aligncenter size-full wp-image-739" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/describe-regions.png" alt="describe-regions" width="470" height="255" /></a>

&nbsp;

</div>
<div></div>
</div>
Un saludo