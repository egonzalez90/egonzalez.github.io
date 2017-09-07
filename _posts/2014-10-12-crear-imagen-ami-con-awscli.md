---
id: 777
title: Crear Imagen AMI con AWScli
date: 2014-10-12T16:59:30+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=777
permalink: /crear-imagen-ami-con-awscli/
image: /wp-content/uploads/2014/09/supporter_1401479988.png
categories:
  - OpenStack
tags:
  - amazon
  - AMI
  - AWS
  - awscli
  - CLI
  - create.image
  - deregister-image
  - describe-images
  - image
  - images
  - instancia
  - services
  - web
---
Crear imagen AMI de una instancia
<blockquote>aws ec2 create-image --instance-id i-7ac29a38 --name "PruebaImagen" --description "ImagenPrueba" --no-reboot</blockquote>
<!--more-->

Ver información de una imagen AMI
<blockquote>aws ec2 describe-images --image-id ami-defc5ea9</blockquote>
Des-registrar una imagen AMI (borrarla)
<blockquote>aws ec2 deregister-image --image-id ami-f4fc5e83</blockquote>