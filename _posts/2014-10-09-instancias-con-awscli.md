---
id: 769
title: Instancias con AWScli
date: 2014-10-09T15:56:23+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=769
permalink: /instancias-con-awscli/
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - OpenStack
tags:
  - amazon
  - AWS
  - aws cli
  - CLI
  - cloud
  - crear
  - describe-instance-status
  - image-id
  - instance-id
  - instancia
  - key-name
  - run-instance
  - security-groups.count
  - services
  - web
---
Crear una instancia en EC2 classic:
<blockquote>aws ec2 run-instances --image-id ami-d02386a7 --count 1 --instance-type t1.micro --key-name kp1 --security-groups default</blockquote>
<!--more-->
<ul>
	<li>run-instances: comando para ejecutar una instancia</li>
	<li>--image-id: ID de la imagen AMI a ejecutar</li>
	<li>--count: numero de instancias a ejecutar</li>
	<li>--instance-type: expecificaciones de hardware de la instancia(CPU,RAM)</li>
	<li>--key-name: keypair para poder conectarnos a la instancia</li>
	<li>--security-groups: grupo de seguridad del que dependera la instancia</li>
</ul>
Después comprobaremos que el estado de la instancia mediante el siguiente comando:
<blockquote> aws ec2 describe-instance-status --instance-id i-7815253a</blockquote>