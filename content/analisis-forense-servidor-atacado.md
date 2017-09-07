Title: Análisis Forense Servidor Atacado
Date: 2014-10-15 16:42
Author: egongu90
Category: Linux
Tags: analisis, atacado, ataque, bash_history, busqueda, ethical, forense, Hacking, informatica, last, linux, lsattr, mtime, netstat, ps, rpm -Va, Seguridad, servidor, strace, top, unix, vulnerable
Slug: analisis-forense-servidor-atacado
Status: published

Esta guía te proporcionara las bases para investigar servidores que su
seguridad ha sido comprometida.

Veremos  los diferentes modos para determinar:

-   Punto de entrada
-   Origen del ataque
-   Archivos comprometidos
-   Nivel de acceso obtenido por el atacante
-   Investigación de pruebas y rastros dejados por los atacantes

<!--more-->

Son muchos los puntos de entradas que un servidor Linux/Unix puede
tener, pero es importante que método se ha usado para determinar el daño
que ha podido hacer en a máquina y/o otros servidores conectados entre
sí.

La mejor forma de arreglar un servidor comprometido es re instalar el
sistema operativo y restaurar los datos importantes desde una copia de
seguridad, pero es importante investigar el servidor afectado para
conocer el punto de entrada y así poder parchearlo en la reinstalación
del SO.

Documentación
=============

Cuando te enteras que un sistema bajo tu control puede haber sido
comprometido, debes de intentar obtener la mayor información posible del
denunciante. Entre ellas:

-   Cuando se encontró el problema inicial
-   La hora estimada del ataque
-   Se ha modificado el servidor desde el ataque
-   Alguna cosa más que el denunciante considere importante

NOTA: Si estás pensando en involucrar a las fuerzas de la ley, realizar
denuncias, es muy importante que no se realice ninguna acción en el
servidor. Este debe quedar en su estado actual a un equipo de
informática forense para la búsqueda de pruebas.

Si vas a proceder a la investigación, documenta toda lo que encuentres
en el servidor.

Herramientas usadas en la investigación
=======================================

En un escenario ideal para un atacante, todos los archivos de log se
habrán borrado dejando su rastro limpio. Por suerte estos casos no se
suelen dar, y aunque los ataques estén automatizados, siempre hay alguna
pista desde la que encontrar información sobre cómo se ha realizado el
ataque, si es ataque web básico o un ataque que compromete el acceso
root.

Aquí tienes algunas herramientas con las que podrás investigar posibles
rastros para analizar el sistema.

last
----

Esta herramienta listara las últimas sesiones de usuario, con este
comando podrás ver horas de sesión, IP, nombre de usuario, etc.

Un numero exagerado de direcciones IP en los archivos de log
/var/log/messages o /var/log/secure puede indicar que el atacante
realizo un ataque por fuerza bruta, eso reflejara en el comando last la
hora de cuando consiguió dicho acceso al servidor

ls -lart
--------

Este comando nos mostrara una lista de archivos y directorios ordenados
por fecha según la última modificación. Esto nos permitirá saber que ha
sido modificado o añadido comprobándolo con las fechas del ataque.

netstat -na
-----------

Eso nos listara las conexiones a la escucha existentes. Nos podrá
revelar posibles backdoors o servicios que no deberían estar en escucha,
los cuales pueden ser causa de alguno de los ficheros

alias
-----

Este comando nos mostrara los alias de comandos, es posible que un
atacante cree alias para que al ejecutar determinado comando se ejecute
otro.

ps -wauxef
----------

Este comando nos es muy útil a la hora de detectar procesos erróneos en
escucha, además también nos listara otros procesos como los del usuario
www. lsof | grep \<pid\> puede ser usado para encontrar que archivos
está utilizando determinado proceso. Igualmente con cat
/proc/\<pid\>/cmdline puedes saber dónde está el archivo que controla el
proceso.

bash\_history
-------------

Mediante este comando obtendremos el historial de los comandos
ejecutados desde los diferentes usuarios. El archivo se encuentra en la
carpeta / root y el /home/ de cada usuario. Es oculto

top
---

A veces un proceso malicioso causa extremo uso de CPU causando problemas
en el entorno, suele estar situado en el principio de la lista. Todo
proceso que este causando un consumo excesivo de CPU debe ser
considerado sospechoso

strace -p
---------

Este comando se ejecutara sobre procesos sospechosos, el cual nos dará
mucha información sobre que está realizando.

En algunos casos, este comando no nos proporcionara ninguna información
real, debido a que se pueden haber modificado los binarios para que la
salida del comando no muestre lo que debería, complicando la
investigación del ataque. Para ello investigaremos que dichos binarios
no están trojanizados:

rpm -Va
-------

Este comando comprobara la información de los paquetes instalados con
los metadatos de la base de datos rpm. Entre otras cosas, compara el
tamaño, suma de verificación MD5, permisos, tipo, propietario y grupo.
Cualquier modificación del paquete original será mostrada.

Cuando se ejecuta este comando, es importante si alguno de los paquetes
marcados como modificados esta en alguno de los siguientes directorios,
de ser así, puede significar que se está usando una versión trojanizada
del binario, por lo que no se puede fiar de la salida del comando.

#### /bin

#### /sbin

#### /usr/bin

#### /usr/sbin

 

rpm -qa
-------

Este comando te mostrara cuales son los últimos paquetes instalado en
orden cronológico. En cualquier caso, si el acceso root ha sido
comprometido, la base de datos rpm puede haber sido modificada y no ser
fiable

lsattr
------

En el caso de que el atacante haya conseguido acceso root y trojanizar
determinados binarios, puede que haya establecido dicho binario como
inmutable, por lo que no podrás reinstalar una versión limpia del
binario. Los directorios más comunes son:

#### /bin

#### /sbin

#### /usr/bin

#### /usr/sbin

También deberías de buscar por otros directorios como /etc, /root, /tmp,
etc.

Un ejemplo del binario de ps establecido como inmutable es este:

#### -------i----- /bin/ps

 

find / mtime 5
--------------

Con este comando buscaras archivos que han sido modificados en los
últimos 5 días, puedes cambiar el digito numérico si sabes las fechas
exactas, así afinaras más las búsqueda y evitaras ver archivos
modificados que no tengan interés en la investigación.

Directorios comunes donde se encuentran los exploits
====================================================

Comprueba los directorios que Apache comúnmente puede escribir sus
archivos temporales

#### ls -al /tmp

#### ls -al /var/tmp

#### ls -al /dev/shm

Si tienes algun fichero con todos los permisos 777, sospecha de el.

Comprueba que los ficheros ocultos no tengan permisos de ejecución.

Encontrando el punto de acceso
==============================

Si has encontrado algo con la información anterior, quiere decir que ya
sabes más o menos cuando el ataque se ha realizado, de qué forma y
contra que. Ahora ya podrás investigar sobre los logs de acceso a la
página web por la fecha por la que se produjo el ataque. También debes
mirar en los archivos /var/log/\* en los cuales encontraras información
de accesos, del sistema, etc.

Si tienes alguna aplicación afectada que también guarde logs, puedes
investigar sobre ellos para buscar más información sobre el atacante.

Debido a un ataque en uno de los servidores que administro tuve que
lidiar con este tipo de investigación forense. Encontré poca información
al respecto, hasta que encontré la siguiente web, que definitivamente me
ayudo realmente.

https://community.rackspace.com/general/f/34/t/75

Estoy realmente agradecido al creador de esa información, por eso me
decidí a traducirla (no literalmente) para que los que sufran de ese
mismo problema y no sepan ingles puedan descubrir que les han hecho en
su servidor.

En la misma web, tienen un ejemplo práctico de como el encontró su
webshell en phpmyadmin, os recomiendo que la lean.

Infinitamente agradecido.

Un saludo
