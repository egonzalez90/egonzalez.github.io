Title: Crear Plantilla AMI en AWS
Date: 2014-09-22 09:14
Author: egongu90
Category: OpenStack
Tags: amazon, AMI, AWS, cloud, computing, crear, ejecutar, hybrid, imagen, instancia, launch, plantilla, private, public, services, web
Slug: crear-plantilla-ami-en-aws
Status: published

El primer paso es estar logeado en AWS, y en la pestaña Instances de
EC2.<!--more-->

Una vez aquí pulsaremos con el botón derecho sobre la instancia que
queremos convertir en plantilla AMI.

Aquí pulsaremos sobre Create
Image[![Captura](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura.png)  
](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura.png)

Lo siguiente sera ponerle un nombre a la plantilla y una descripcion,
para finalizar le daremos a Create Image

[![Captura2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura2.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura2.png)

A continuación nos mostrara un mensage que indica que esta en proceso de
creacion, pulsaremos sobre View Pending Image \*\*\*\* para ver el
estado de la peticion

[![Captura3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura3.png) ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura3.png)En
esta ventana veremos el estado de la peticion, una vez acabada la
creacion de la plantilla aparecera en verde Available, estos sencillos
pasos nos permitiran tener imagenes personalizadas para ejecutar tantas
instancias como queramos sobre esa plantilla

[![Captura4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura4.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/Captura4.png) Para
ejecutar la imagen como una instancia, solo tienes que pulsar sobre
Launch y crear la instancia como cualquier otra.

Si quieres saber como se crea una instancia puedes hacerlo siguiendo
esta entrada del blog: <http://egonzalez.org/?p=635>
