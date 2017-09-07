Title: Carpetas compartidas Virtual Box y Ubuntu
Date: 2013-01-19 20:00
Author: egongu90
Category: Linux
Tags: carpetas, compartidas, linux, ubuntu, virtual box
Slug: carpetas-compartidas-virtual-box-y-ubuntu
Status: published

La primera vez que entras a Ubuntu con VirtualBox te puedes volver loco
buscando la carpeta compartida, que no la encontraras.No es como Windows
que te aparece en red, esta hay que montarla para poder acceder a
ella.<!--more-->

El mayor problema son las Guest Additions que muchas veces dan fallo
para compartir las carpetas, pues bien, si no te deja montar la carpeta
con el método que voy a describir abajo, deberás reinstalar las Guest
Additions, y con esto debería de permitírtelo, aunque si continua
repitelo de nuevo, ya te  digo que falla bastante.

Con esto entendido vamos a empezar creando la carpeta compartida desde
el menú de VirtualBox después de haber instalado las Guest Additions,
doy por hecho que eso si lo sabéis crear, a partir de ese momento se
enciende la maquina virtual de Ubuntu.

Se abre un terminal y se crea una carpeta, que sera la
compartida después:

-   mkdir /media/nombredelacarpeta

Después se crea el punto de montaje de la carpeta compartida:

-   <address>
    sudo mount -t vboxsf Nombre /media/Nombre de la carpeta de antes
    </address>

Donde Nombre es como hemos llamado a la carpeta compartida en VirtualBox
al principio.

Si te diera error aquí es donde tienes que volver a instalar las Guest
Additions, antes puedes probar a ejecutar el comando dentro del fichero
donde esta vboxsf:

-   <address>
    cd /sbin/vboxsf
    </address>

Después se ha de ir a

-   <address>
    cd /etc/init.d
    </address>

Aquí hay que editar un archivo para que se auto monte la carpeta
compartida cada vez que se encienda el equipo:

-   <address>
    gksudo gedit rc.local
    </address>

En este momento se copia el comando de montaje de la carpeta en el final
del archivo, se guarda y ya estaría todo hecho.

-   <address>
    sudo mount -t vboxsf Nombre /media/Nombre de la carpeta
    </address>

Si hubiera algún error comenten para arreglarlo. Un saludo
