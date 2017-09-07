Title: Crear instancia Amazon Web Services (AWS)
Date: 2014-09-15 16:10
Author: egongu90
Category: OpenStack
Tags: amazon, AWS, cloud, computing, creacion, crear, ec2, instancia, linux, pem, ppk, primera, putty, services, web
Slug: crear-instancia-amazon-web-services-aws
Status: published

Buenos días, en esta entrada mostrare como crear una instancia en la
plataforma cloud de Amazon Web Services.

<!--more--> Para poder crear las instancias, deberemos tener cuenta de
AWS y nos logearemos en la consola.

Lo primero que nos encontraremos sera el dashboard principal, aqui
podremos administrar las diferentes secciones de AWS. Nosotros iremos a
EC2

[![01](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/01.png)Una vez
entrado en EC2, nos encontraremos con esta ventana que nos mostrara un
resumen de lo que tenemos en nuestro EC2.

A nosotros nos interesa crear una instancia nueva, por lo que pulsaremos
sobre Launch Instance

[![02](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/02.png)La
siguiente pantalla nos mostrara varias instancias disponibles para
crear, en nuestro plan free disponemos de alguna, nosotros
seleccionaremos Amazon Linux AMI

[![03](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/03.png)Al
utilizar el plan free solo podremos usar el tipo t2.micro, por lo que lo
dejaremos por defecto y daremos a Configure Instance Details

[![04](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/04.png)En esta
pantalla también la dejaremos por defecto, se puede seleccionar alguna
opción si se quisiera como por ejemplo Monitoring, nosotros iremos
directamente a Add Storage

[![05](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/05.png)En esta
otra pantalla lo mismo, lo dejaremos por defecto y pasaremos a Tag
Instance

[![06](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png)

[  
](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/06.png)[![07](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/07.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/07.png)

Aquí si que rellenaremos el Valor con el nombre de la instancia, en este
ejemplo instancename, a continuación iremos a Configure Security Group

[![08](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/08.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/08.png)

[![09](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/09.png)Aquí
pondremos un nombre para el Grupo de Seguridad y una descripción, como
vemos, tenemos creada una regla por defecto que permite el acceso por
SSH desde cualquier IP, eso no es muy recomendable, pero al ser una
Instancia de pruebas lo dejaremos por defecto

 

[![10](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/10.png)
[![11](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/11.png)Ya son
pocos los pasos para acabar de crear la instancia, aqui tenemos un
resumen de la configuración que hemos realizado, pulsaremos en Launch
Instance para pasar al siguiente paso

[![12](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/12.png)Por
ultimo crearemos una clave .pem para que podamos acceder a la instancia,
para ello marcaremos Create a new key pair y pondremos un nombre para
esa clave. Después pulsaremos en Download Key Pair, de esta forma se nos
descargara la clave a nuestro equipo y se habilitara la opción de Launch
Instances

[![13](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/13.png)

Ahora mismo ya se esta creando nuestra instancia, podremos ver el
progreso pulsando sobre View Instances

 

 

[![14](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png)

 

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/14.png)Esta es
la ventana en donde podemos ver las instancias, la primera es una que
esta en uso y completa, la segunda es la que acabamos de crear, cuando
Status Checks este en verde ya la tendremos completamente creada

[![15](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/15.png)Lo
ultimo que nos queda es conectarnos por SSH a la instancia creada, para
ello copiaremos el Public DNS, que es la dirección a la que nos podremos
conectar

[![16](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/16.png)En mi
caso me conecto con PuTTy, para ello debes de convertir el formato de la
clave .pem a .ppk, para ello tienes una entrada en este mismo blog de
como hacerlo: <http://egonzalez.org/?p=630>

Una vez abierto PuTTy utilizaremos la siguiente direccion:
ec2-user@DNSPUBLICO

El usuario ec2-user es creado automaticamente

DNSPUBLICO es la direccion que habiamos copiado previamente

[![17](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png)

 

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/17.png)Por
ultimo iremos a SSH/Auth y buscaremos la clave privada de nuestra
instancia

[![18](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png)

[ ](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/18.png)Despues
de aceptar la clave nos veremos logeados en la instancia, con esto ya
estaria finalizada la instalacion y comprobacion de nuestra primera
instancia en AWS.

Es recomendable realizazar una actualizacion del sistema nada mas
arrancar con el comando

> sudo yum update
>
>  

[![19](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/19.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/09/19.png)

Espero ser de ayuda y muchas gracias por leer este blog, un saludo
