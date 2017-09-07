Title: ELB en AWS (Elastic Load Balancers)
Date: 2014-09-25 16:43
Author: egongu90
Category: OpenStack
Tags: amazon, automatizar, AWS, Balancers, cloud, crear, distribuir, ELB, http, instancias, Load, Services; Elastic, trafico, virtualizacion, web
Slug: elb-en-aws-elastic-load-balancers
Status: published

Hoy mostraré como crear Elastic Load Balancer (ELB) en Amazon Web
Services el cual nos permitirá distribuir automáticamente el trafico
entre las aplicaciones de las distintas instancias y obtener una mejor
tolerancia a fallos.<!--more-->

Primero nos logearemos en AWS e iremos a la pestaña EC2, una vez a, aquí
pulsaremos sobre Load Balancers del menú izquierdo.

Se nos abrirá esta ventana en la que pulsaremos Create Load Balancer
para configurar un ELB nuevo. En esta misa ventana nos mostraría los ELB
ya creados

[![01](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/011.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/011.png)

Una vez abierto Create Load Balancer, rellenaremos el Nombre del ELB a
crear y estableceremos los protocolos que soportara el ELB, por defecto
viene activado HTTP por el puerto 80

[![02](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/021.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/021.png)

En esta próxima pantalla configuraremos los análisis de salud de
nuestras instancias, para ello ajustaremos los parámetros inferiores a
nuestro gusto

[![03](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/031.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/031.png)

Aquí asignaremos o crearemos un Security Group, en mi caso utilizare uno
ya existente

[![04](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/041.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/041.png)

Lo ultimo que configuraremos serán las instancias que harán uso del ELB,
seleccionamos las que queramos y pulsaremos en Continue

[![05](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/051.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/051.png)

Finalizaremos estableciendo una etiqueta a nuestro ELB

[![06](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/061.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/061.png)

Antes de terminar de crear el ELB, nos mostrara una resumen de la
configuración, si estuviéramos de acuerdo pulsaríamos en Create, de lo
contrario modificaremos alguna de las partes anteriores

[![07](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/071.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/071.png)

Esta seria una imagen del ELB creado, tendremos que esperar un rato
hasta que este activo, una vez activo veremos In Service el Status de
las Instancias, aunque en algunas ocasiones aunque este In Service aun
no tenemos conexión a través del ELB

[![08](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/081.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/081.png)

Un saludo
