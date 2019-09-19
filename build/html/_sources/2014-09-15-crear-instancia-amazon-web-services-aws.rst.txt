--- layout: post title: Crear instancia Amazon Web Services (AWS) date:
2014-09-15 16:10:06.000000000 +02:00 type: post parent_id: '0'
published: true password: '' status: publish categories: - OpenStack
tags: - amazon - AWS - cloud - computing - creacion - crear - ec2 -
instancia - linux - pem - ppk - primera - putty - services - web meta:
\_edit_last: '2' \_thumbnail_id: '631' snap_MYURL: '' snapEdIT: '1'
snapFB: N; snap_isAutoPosted: '1' snapTW: N;
\_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1568291610;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:684;}i:1;a:1:{s:2:"id";i:769;}i:2;a:1:{s:2:"id";i:777;}}}}
dsq_thread_id: '6106850238' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/crear-instancia-amazon-web-services-aws/" ---

Buenos días, en esta entrada mostrare como crear una instancia en la
plataforma cloud de Amazon Web Services.

 Para poder crear las instancias, deberemos tener cuenta de AWS y nos
logearemos en la consola.

Lo primero que nos encontraremos sera el dashboard principal, aqui
podremos administrar las diferentes secciones de AWS. Nosotros iremos a
EC2

`01 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png>`__\ Una
vez entrado en EC2, nos encontraremos con esta ventana que nos mostrara
un resumen de lo que tenemos en nuestro EC2.

A nosotros nos interesa crear una instancia nueva, por lo que pulsaremos
sobre Launch Instance

`02 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png>`__\ La
siguiente pantalla nos mostrara varias instancias disponibles para
crear, en nuestro plan free disponemos de alguna, nosotros
seleccionaremos Amazon Linux AMI

`03 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png>`__\ Al
utilizar el plan free solo podremos usar el tipo t2.micro, por lo que lo
dejaremos por defecto y daremos a Configure Instance Details

`04 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png>`__\ En
esta pantalla también la dejaremos por defecto, se puede seleccionar
alguna opción si se quisiera como por ejemplo Monitoring, nosotros
iremos directamente a Add Storage

`05 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png>`__\ En
esta otra pantalla lo mismo, lo dejaremos por defecto y pasaremos a Tag
Instance

`06 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png>`__

`
 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png>`__\ `07 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/07.png>`__

Aquí si que rellenaremos el Valor con el nombre de la instancia, en este
ejemplo instancename, a continuación iremos a Configure Security Group

`08 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/08.png>`__

`09 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png>`__\ Aquí
pondremos un nombre para el Grupo de Seguridad y una descripción, como
vemos, tenemos creada una regla por defecto que permite el acceso por
SSH desde cualquier IP, eso no es muy recomendable, pero al ser una
Instancia de pruebas lo dejaremos por defecto

 

`10 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png>`__
`11 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png>`__\ Ya
son pocos los pasos para acabar de crear la instancia, aqui tenemos un
resumen de la configuración que hemos realizado, pulsaremos en Launch
Instance para pasar al siguiente paso

`12 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png>`__\ Por
ultimo crearemos una clave .pem para que podamos acceder a la instancia,
para ello marcaremos Create a new key pair y pondremos un nombre para
esa clave. Después pulsaremos en Download Key Pair, de esta forma se nos
descargara la clave a nuestro equipo y se habilitara la opción de Launch
Instances

`13 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png>`__

Ahora mismo ya se esta creando nuestra instancia, podremos ver el
progreso pulsando sobre View Instances

 

 

`14 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png>`__

 

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png>`__\ Esta
es la ventana en donde podemos ver las instancias, la primera es una que
esta en uso y completa, la segunda es la que acabamos de crear, cuando
Status Checks este en verde ya la tendremos completamente creada

`15 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png>`__\ Lo
ultimo que nos queda es conectarnos por SSH a la instancia creada, para
ello copiaremos el Public DNS, que es la dirección a la que nos podremos
conectar

`16 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png>`__\ En
mi caso me conecto con PuTTy, para ello debes de convertir el formato de
la clave .pem a .ppk, para ello tienes una entrada en este mismo blog de
como hacerlo: \ http://egonzalez.org/?p=630

Una vez abierto PuTTy utilizaremos la siguiente direccion:
ec2-user@DNSPUBLICO

El usuario ec2-user es creado automaticamente

DNSPUBLICO es la direccion que habiamos copiado previamente

`17 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png>`__

 

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png>`__\ Por
ultimo iremos a SSH/Auth y buscaremos la clave privada de nuestra
instancia

`18 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png>`__

`  <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png>`__\ Despues
de aceptar la clave nos veremos logeados en la instancia, con esto ya
estaria finalizada la instalacion y comprobacion de nuestra primera
instancia en AWS.

Es recomendable realizazar una actualizacion del sistema nada mas
arrancar con el comando

   sudo yum update

    

`19 <http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/19.png>`__

Espero ser de ayuda y muchas gracias por leer este blog, un saludo
