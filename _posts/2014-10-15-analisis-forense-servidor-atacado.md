---
id: 781
title: Análisis Forense Servidor Atacado
date: 2014-10-15T16:42:06+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=781
permalink: /analisis-forense-servidor-atacado/
image: /wp-content/uploads/2014/05/original-672x372.jpg
categories:
  - Linux
tags:
  - analisis
  - atacado
  - ataque
  - bash_history
  - busqueda
  - ethical
  - forense
  - Hacking
  - informatica
  - last
  - linux
  - lsattr
  - mtime
  - netstat
  - ps
  - rpm -Va
  - Seguridad
  - servidor
  - strace
  - top
  - unix
  - vulnerable
---
Esta guía te proporcionara las bases para investigar servidores que su seguridad ha sido comprometida.

Veremos  los diferentes modos para determinar:
<ul>
	<li>Punto de entrada</li>
	<li>Origen del ataque</li>
	<li>Archivos comprometidos</li>
	<li>Nivel de acceso obtenido por el atacante</li>
	<li>Investigación de pruebas y rastros dejados por los atacantes</li>
</ul>
<!--more-->

Son muchos los puntos de entradas que un servidor Linux/Unix puede tener, pero es importante que método se ha usado para determinar el daño que ha podido hacer en a máquina y/o otros servidores conectados entre sí.

La mejor forma de arreglar un servidor comprometido es re instalar el sistema operativo y restaurar los datos importantes desde una copia de seguridad, pero es importante investigar el servidor afectado para conocer el punto de entrada y así poder parchearlo en la reinstalación del SO.
<h1>Documentación</h1>
Cuando te enteras que un sistema bajo tu control puede haber sido comprometido, debes de intentar obtener la mayor información posible del denunciante. Entre ellas:
<ul>
	<li>Cuando se encontró el problema inicial</li>
	<li>La hora estimada del ataque</li>
	<li>Se ha modificado el servidor desde el ataque</li>
	<li>Alguna cosa más que el denunciante considere importante</li>
</ul>
NOTA: Si estás pensando en involucrar a las fuerzas de la ley, realizar denuncias, es muy importante que no se realice ninguna acción en el servidor. Este debe quedar en su estado actual a un equipo de informática forense para la búsqueda de pruebas.

Si vas a proceder a la investigación, documenta toda lo que encuentres en el servidor.
<h1>Herramientas usadas en la investigación</h1>
En un escenario ideal para un atacante, todos los archivos de log se habrán borrado dejando su rastro limpio. Por suerte estos casos no se suelen dar, y aunque los ataques estén automatizados, siempre hay alguna pista desde la que encontrar información sobre cómo se ha realizado el ataque, si es ataque web básico o un ataque que compromete el acceso root.

Aquí tienes algunas herramientas con las que podrás investigar posibles rastros para analizar el sistema.
<h2>last</h2>
Esta herramienta listara las últimas sesiones de usuario, con este comando podrás ver horas de sesión, IP, nombre de usuario, etc.

Un numero exagerado de direcciones IP en los archivos de log /var/log/messages o /var/log/secure puede indicar que el atacante realizo un ataque por fuerza bruta, eso reflejara en el comando last la hora de cuando consiguió dicho acceso al servidor
<h2>ls -lart</h2>
Este comando nos mostrara una lista de archivos y directorios ordenados por fecha según la última modificación. Esto nos permitirá saber que ha sido modificado o añadido comprobándolo con las fechas del ataque.
<h2>netstat -na</h2>
Eso nos listara las conexiones a la escucha existentes. Nos podrá revelar posibles backdoors o servicios que no deberían estar en escucha, los cuales pueden ser causa de alguno de los ficheros
<h2>alias</h2>
Este comando nos mostrara los alias de comandos, es posible que un atacante cree alias para que al ejecutar determinado comando se ejecute otro.
<h2>ps -wauxef</h2>
Este comando nos es muy útil a la hora de detectar procesos erróneos en escucha, además también nos listara otros procesos como los del usuario www. lsof | grep &lt;pid&gt; puede ser usado para encontrar que archivos está utilizando determinado proceso. Igualmente con cat /proc/&lt;pid&gt;/cmdline puedes saber dónde está el archivo que controla el proceso.
<h2>bash_history</h2>
Mediante este comando obtendremos el historial de los comandos ejecutados desde los diferentes usuarios. El archivo se encuentra en la carpeta / root y el /home/ de cada usuario. Es oculto
<h2>top</h2>
A veces un proceso malicioso causa extremo uso de CPU causando problemas en el entorno, suele estar situado en el principio de la lista. Todo proceso que este causando un consumo excesivo de CPU debe ser considerado sospechoso
<h2>strace -p</h2>
Este comando se ejecutara sobre procesos sospechosos, el cual nos dará mucha información sobre que está realizando.

En algunos casos, este comando no nos proporcionara ninguna información real, debido a que se pueden haber modificado los binarios para que la salida del comando no muestre lo que debería, complicando la investigación del ataque. Para ello investigaremos que dichos binarios no están trojanizados:
<h2>rpm -Va</h2>
Este comando comprobara la información de los paquetes instalados con los metadatos de la base de datos rpm. Entre otras cosas, compara el tamaño, suma de verificación MD5, permisos, tipo, propietario y grupo. Cualquier modificación del paquete original será mostrada.

Cuando se ejecuta este comando, es importante si alguno de los paquetes marcados como modificados esta en alguno de los siguientes directorios, de ser así, puede significar que se está usando una versión trojanizada del binario, por lo que no se puede fiar de la salida del comando.
<h4>/bin</h4>
<h4>/sbin</h4>
<h4>/usr/bin</h4>
<h4>/usr/sbin</h4>
&nbsp;
<h2>rpm -qa</h2>
Este comando te mostrara cuales son los últimos paquetes instalado en orden cronológico. En cualquier caso, si el acceso root ha sido comprometido, la base de datos rpm puede haber sido modificada y no ser fiable
<h2>lsattr</h2>
En el caso de que el atacante haya conseguido acceso root y trojanizar determinados binarios, puede que haya establecido dicho binario como inmutable, por lo que no podrás reinstalar una versión limpia del binario. Los directorios más comunes son:
<h4>/bin</h4>
<h4>/sbin</h4>
<h4>/usr/bin</h4>
<h4>/usr/sbin</h4>
También deberías de buscar por otros directorios como /etc, /root, /tmp, etc.

Un ejemplo del binario de ps establecido como inmutable es este:
<h4>-------i----- /bin/ps</h4>
&nbsp;
<h2>find / mtime 5</h2>
Con este comando buscaras archivos que han sido modificados en los últimos 5 días, puedes cambiar el digito numérico si sabes las fechas exactas, así afinaras más las búsqueda y evitaras ver archivos modificados que no tengan interés en la investigación.
<h1>Directorios comunes donde se encuentran los exploits</h1>
Comprueba los directorios que Apache comúnmente puede escribir sus archivos temporales
<h4>ls -al /tmp</h4>
<h4>ls -al /var/tmp</h4>
<h4>ls -al /dev/shm</h4>
Si tienes algun fichero con todos los permisos 777, sospecha de el.

Comprueba que los ficheros ocultos no tengan permisos de ejecución.
<h1>Encontrando el punto de acceso</h1>
Si has encontrado algo con la información anterior, quiere decir que ya sabes más o menos cuando el ataque se ha realizado, de qué forma y contra que. Ahora ya podrás investigar sobre los logs de acceso a la página web por la fecha por la que se produjo el ataque. También debes mirar en los archivos /var/log/* en los cuales encontraras información de accesos, del sistema, etc.

Si tienes alguna aplicación afectada que también guarde logs, puedes investigar sobre ellos para buscar más información sobre el atacante.

Debido a un ataque en uno de los servidores que administro tuve que lidiar con este tipo de investigación forense. Encontré poca información al respecto, hasta que encontré la siguiente web, que definitivamente me ayudo realmente.

https://community.rackspace.com/general/f/34/t/75

Estoy realmente agradecido al creador de esa información, por eso me decidí a traducirla (no literalmente) para que los que sufran de ese mismo problema y no sepan ingles puedan descubrir que les han hecho en su servidor.

En la misma web, tienen un ejemplo práctico de como el encontró su webshell en phpmyadmin, os recomiendo que la lean.

Infinitamente agradecido.

Un saludo