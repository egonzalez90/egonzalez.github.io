Title: Instancias con AWScli
Date: 2014-10-09 15:56
Author: egongu90
Category: OpenStack
Tags: amazon, AWS, aws cli, CLI, cloud, crear, describe-instance-status, image-id, instance-id, instancia, key-name, run-instance, security-groups.count, services, web
Slug: instancias-con-awscli
Status: published

Crear una instancia en EC2 classic:

> aws ec2 run-instances --image-id ami-d02386a7 --count 1
> --instance-type t1.micro --key-name kp1 --security-groups default

<!--more-->

-   run-instances: comando para ejecutar una instancia
-   --image-id: ID de la imagen AMI a ejecutar
-   --count: numero de instancias a ejecutar
-   --instance-type: expecificaciones de hardware de la
    instancia(CPU,RAM)
-   --key-name: keypair para poder conectarnos a la instancia
-   --security-groups: grupo de seguridad del que dependera la instancia

Después comprobaremos que el estado de la instancia mediante el
siguiente comando:

>  aws ec2 describe-instance-status --instance-id i-7815253a
