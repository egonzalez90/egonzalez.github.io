---
id: 705
title: s3cmd, administración bucket AWS
date: 2014-09-29T18:42:28+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=705
permalink: /s3cmd-administracion-bucket-aws/
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - Linux
  - OpenStack
tags:
  - --configure
  - access denied
  - access key
  - amazon
  - AWS
  - cloud
  - configurar
  - IAM
  - instalar
  - permisos
  - policy
  - s3cmd
  - s3tools
  - secret key
  - services
  - usuario
  - web
---
Buenos días, en esta entrada mostrare el proceso para instalar s3cmd con el que podremos administrar nuestros contenedores de AWS.<!--more-->

Para ello primero deberemos localizar el repositorio para la versión de nuestro RHEL, lo podéis hacer en este enlace: <a title="Repositorios s3tools" href="http://s3tools.org/repositories" target="_blank">http://s3tools.org/repositories</a>

En mi caso uso la versión 6.5 de RHEL, por lo que usare el repositorio de la versión 6, descargaremos el archivo .repo acorde con nuestra versión, cambiando el enlace por el proporcionado por la pagina anterior si fuera otra versión fuera de la 6
<blockquote>wget http://s3tools.org/repo/RHEL_6/s3tools.repo</blockquote>
A continuación moveremos el archivo .repo a la localización de los repositorios en el SO, este paso se puede saltar si el comando wget se lanza desde el mismo directorio /etc/yum.repos.d/
<blockquote>mv s3tools.repo /etc/yum.repos.d/</blockquote>
Ahora actualizaremos la lista de repositorios para que el SO la reconozca
<blockquote>sudo yum repolist</blockquote>
Después instalaremos s3cmd mediante el siguiente comando
<blockquote>sudo yum install s3cmd</blockquote>
Para acabar, procederemos a configurar s3cmd para que pueda acceder a nuestros contenedores en AWS
<blockquote>s3cmd --configure</blockquote>
&nbsp;
<blockquote>
<pre>Enter new values or accept defaults in <span id="IL_AD1" class="IL_AD">brackets</span> with Enter.
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
Configuration saved to '/root/.s3cfg'</pre>
</blockquote>
Access Key la puedes encontrar en: Security Credentials/ Users/ Access Credentials

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/access.png"><img class="aligncenter size-full wp-image-708" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/access.png" alt="access" width="1000" height="387" /></a>

Secret Key solo se puede descargar una única vez, al crear las claves de acceso, si fuera necesario, deberías de crear unas nuevas para poder obtener Secret Key para esa clave.

Seguramente que te de un error si lanzas el comando ahora, para que no te de el error Access Denied, tienes que agregar una política de usuario con permisos

<a href="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/userpolicy.png"><img class="aligncenter size-full wp-image-709" src="http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/userpolicy.png" alt="userpolicy" width="1020" height="298" /></a>

Por ultimo probaremos que tenemos acceso a los bucket
<blockquote>s3cmd ls</blockquote>
Esto nos debería de mostrar los contenedores a los que tenemos permisos dentro de AWS

Ahora solo te queda investigar las diferentes posibilidades que te da s3cmd

Un saludo

&nbsp;

&nbsp;