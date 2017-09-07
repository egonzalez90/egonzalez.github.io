Title: Crear Imagen AMI con AWScli
Date: 2014-10-12 16:59
Author: egongu90
Category: OpenStack
Tags: amazon, AMI, AWS, awscli, CLI, create.image, deregister-image, describe-images, image, images, instancia, services, web
Slug: crear-imagen-ami-con-awscli
Status: published

Crear imagen AMI de una instancia

> aws ec2 create-image --instance-id i-7ac29a38 --name "PruebaImagen"
> --description "ImagenPrueba" --no-reboot

<!--more-->

Ver información de una imagen AMI

> aws ec2 describe-images --image-id ami-defc5ea9

Des-registrar una imagen AMI (borrarla)

> aws ec2 deregister-image --image-id ami-f4fc5e83
