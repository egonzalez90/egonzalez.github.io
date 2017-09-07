Title: Crear Raid 1 en Linux
Date: 2014-02-14 00:34
Author: egongu90
Category: Linux
Tags: configuracion, Debian, disco duro, linux, mdadm, raid
Slug: crear-raid-1-en-linux
Status: published

 

**En esta entrada, voy a mostrar como se crea un raid de nivel 1 bajo
Linux, también simulare como cambiar un disco en caso de que uno
falle.<!--more-->**

**Empecemos:**

**Cuando iniciamos la consola de Linux, comprobaremos que discos duros
tenemos disponibles, en esta pantalla vemos que están sda, sdb**

[![1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/1.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/1.jpg)

**En esta otra esta sdc, vemos que tanto sdb como sdc están sin formato
alguno**

[![2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/2.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/2.jpg)

**Ahora instalaremos el paquete mdadm, que será el que nos permita
configurar un raid en el sistema **

[![3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/3.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/3.jpg)

**Ahora crearemos un nuevo dispositivo llamado md0, con un raid de nivel
1, añadiendo los dispositivos sdb y sdc a este**

 

[![4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/4.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/4.jpg)

**Ahora configuraremos este dispositivo que hemos creado previamente**

[![5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/5.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/5.jpg)

**Utilizaremos la opción N para crear una nueva partición**

**Seleccionaremos P para hacerla primaria**

**Estableceremos que la partición es la numero 1**

**Pondremos el cilindro número 1 como primero, y el último de los que
tengamos disponibles como final**

[![6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/6.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/6.jpg)

**Después utilizaremos la opción W para escribir los cambios al disco**

[![7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/7.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/7.jpg)

**Ahora crearemos el sistema de fichero mediante el comando mkfs y el
dispositivo que habíamos creado**

[![8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/8.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/8.jpg)

**Ahora crearemos una carpeta de montaje de nuestro dispositivo mediante
mkdir**

**Después montaremos el dispositivo a dicha carpeta mediante el comando
mount**

[![9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/9.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/9.jpg)

**Ahora crearemos un fichero de un tamaño determinado que se especifica
en la opción bs **

[![10](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/10.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/10.jpg)

**Ahora comprobamos esta carpeta, y vemos que los tamaños están bien
configurados**

[![11](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/11.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/11.jpg)

**Ahora comprobaremos en este archivo que el raid está activo, y tiene
los dispositivos sdb y sdc**

[![12](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/12.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/12.jpg)

**Ahora haremos como que el disco sdb ha fallado, para poder quitarle
del raid para remplazarle primero hay que marcarle como disco fallido
mediante este comando**

[![13](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/13.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/13.jpg)

**Ahora le quitaremos del raid el disco sdb**

[![14](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/14.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/14.jpg)

**Iremos al archivo del raid y comprobamos que no está el disco sdb
dentro de el**

[![15](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/15.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/15.jpg)

**Ahora borraremos los datos de configuración anterior del disco sdb
mediante el primer comando.**

**Después añadimos el disco sdb al disco raid, esto si tiene datos
tardara un tiempo en sincronizar**

[![16](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/16.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/16.jpg)

**Ahora desactivaremos el raid mediante este comando**

[![17](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/17.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/17.jpg)

**Si queremos volver a activarle, lo haremos mediante este otro
comando**

[![18](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/18.jpg)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/02/18.jpg)
