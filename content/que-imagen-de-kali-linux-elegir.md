Title: Que imagen de Kali Linux elegir
Date: 2014-03-07 15:24
Author: egongu90
Category: Linux
Tags: 32 bits, 64 bits, descargar, elegir, iso, kali, linux, version, vmware
Slug: que-imagen-de-kali-linux-elegir
Status: published

<div>

Una de las dudas mas comunes de la gente que empieza en la seguridad
informatica es que version o imagen descargar de Kali Linux.<!--more-->

</div>

<div>

</div>

<div>

En esta entrada explicare un poco las diferencias entre las diferentes
arquitecturas y tipos de imagen. Normalmente los que empiezan no suelen
tener idea alguna sobre Linux ni sus tipos de arquitectura, por eso se
deciden a instalarlo en maquinas virtuales.

</div>

<div>

</div>

<div>

Cuando vas a la pagina de descargas de Kali, aqui podran observar que
hay 3 categorias principales:

</div>

<div>

-   ISO 32 bits
-   ISO 64 bits
-   Imagen de VMWARE

</div>

<div>

</div>

<div>

Bien, ahora explicare las diferencias entre cada una y explicare que
hacer en caso de tener un equipo de 32 o 64 bits, aso podran decantarse
por una version u otra.

</div>

<div>

</div>

<div style="text-align: center;">

***Equipo 32 bits***

</div>

<div>

</div>

<div>

***ISO 32 bits***

</div>

<div>

</div>

<div>

Esta imagen podra ser instalada en el equipo y/o ser virtualizada por
virtualbox, normalmente se llaman i368, no te deberia de asustar si tu
procesador es AMD, ya que la "i" se refiere a Intel, pero porque en un
principio, esta arquitectura se hizo basandose en los procesadores i386
de Intel. Esta imagen sera compatible con tu procesador AMD sin ningun
problema.

</div>

<div>

</div>

<div>

**ISO 64 bits**

</div>

<div>

</div>

<div>

Esta imagen no la puedes instalar en un equipo de 32 bits, quizas si que
te permita instalarla, pero el sistema no funcionara correctamente. No
se debe instalar nunca en equipos de 32 bits

</div>

<div>

</div>

<div>

**Imagen VMWARE**

</div>

<div>

</div>

<div>

Aqui es donde la mayoria de la gente tiene dudas y recurre a preguntar a
las multiples comunidades y foros. Bien, si tienes VMWARE esta es la
mejor opcion, ya que esta imagen es de un disco virtualizado de kali ya
configurado para funcionar correctamente la red, ya que al virtualizar
una imagen ISO, hay veces que te puede dar problemas a la hora de poner
la red en bridged. Aqui deberias de elegir la version de 32 bits.

</div>

<div>

</div>

<div>

**Resumen equipo 32 bits**

</div>

<div>

</div>

<div>

Lo principal que te debe quedar claro es que solo puedes instalar
imagenes de 32 bits, dentro de las cuales, tienes la opcion entre ISO y
VMWARE. Aqui tienes que decidir: Si vas a instalarlo en fisico, debes
utilizar una imagen ISO, si vas a virtualizar con VMWARE utilizar el
disco ya instalado y si lo que vas a hacer es instalar en VirtualBox
utiliza la imagen ISO 32 Bits.

</div>

<div>

</div>

<div style="text-align: center;">

***Equipo 64 bits***

</div>

<div>

**ISO 32 bits**

</div>

<div>

</div>

<div>

En un equipo de 64 bits podras instalar tanto arquitecturas 32 como 64
bits, por lo que esta tipo de Iso sera compatible con el equipo. Piensa
que la virtualizacion es un programa normal de Windows, en tu equipo de
64 bits, puedes instalar tanto programas de 32 como de 64 bits.

</div>

<div>

</div>

<div>

**ISO 64 bits**

</div>

<div>

</div>

<div>

Quizas esta pensaras que es la adecuada para tu equipo, pero la mayoria
de la gente recomienda utilizar la version de 32 bits, por el simple
echo de que virtualizar 64 bits consume mas recursos, con el agrabante
de que si tienes una BIOS relativamente nueva, tendras que habilitar la
opcion de Virtualizacion en ella, sino no podras virtualizar 64 bits. La
Iso de 64 bits es recomendable si instalas en un disco fisico.

</div>

<div>

</div>

<div>

**Imagen de VMWARE**

</div>

<div>

</div>

<div>

Esta parte es igual que en el equipo de 32 bits, salvo que aqui podras
instalar la version de 32 o de 64, siendo mas recomendable igualmente la
de 32 bits, por el tema de consumo de los recursos del sistema.

</div>

<div>

</div>

<div>

**Resumen de equipo 64 bits**

</div>

<div>

</div>

<div>

Si vas a instalar en un disco fisico, usa la Iso de 64 bits, si vas a
virtualizar con VirtualBox, usa la Iso y si vas a virtualizar en VMWARE,
usa la Imagen de VMWARE. La decision entre virtualizar 64 y 32 bits la
tendras que sopesar con los recursos de hardware de los que dispone tu
equipo, ya que la de 64 bits te pedira bastante mas RAM que la de 32
bits.

</div>

<div>

</div>

<div>

Espero que esta entrada les sirva de ayuda, si tienen alguna duda
pregunten en los comentarios sin ningun problema.

</div>

<div>

</div>

 
