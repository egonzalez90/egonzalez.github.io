--- layout: post title: Crear Imagen AMI con AWScli date: 2014-10-12
16:59:30.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - amazon -
AMI - AWS - awscli - CLI - create.image - deregister-image -
describe-images - image - images - instancia - services - web meta:
\_edit_last: '2' \_thumbnail_id: '631' \_publicize_facebook_user:
https://www.facebook.com/dudu.gonzalez90 \_publicize_twitter_user:
"@hidanstillalive" \_wpas_done_all: '1' \_wpas_skip_5226565: '1'
\_wpas_skip_4949654: '1' \_wpas_skip_8706018: '1'
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568804078;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:859;}i:1;a:1:{s:2:"id";i:879;}i:2;a:1:{s:2:"id";i:898;}}}}
dsq_thread_id: '6177989950' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/crear-imagen-ami-con-awscli/" ---

Crear imagen AMI de una instancia

   aws ec2 create-image --instance-id i-7ac29a38 --name "PruebaImagen"
   --description "ImagenPrueba" --no-reboot

Ver información de una imagen AMI

   aws ec2 describe-images --image-id ami-defc5ea9

Des-registrar una imagen AMI (borrarla)

   aws ec2 deregister-image --image-id ami-f4fc5e83
