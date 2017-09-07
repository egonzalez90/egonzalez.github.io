Title: Extraer archivos .rar en Ubuntu
Date: 2013-01-13 12:13
Author: egongu90
Category: Linux
Slug: extraer-archivos-rar-en-ubuntu
Status: published

Muchos usuarios de Linux pensaran que es una bobada explicar este tema,
pero créanme que muchos usuarios noveles de las distribuciones de Ubuntu
no saben como hacerlo.  
Os voy a explicar como utilizar la aplicación Unrar en modo texto,
puesto que no tiene opción gráfica.<!--more-->  
<a name="more"></a>En primer lugar hay que realizar el comando básico 
  <span style="font-family:'Courier New', Courier, monospace;">apt-get
install</span>     , esto servirá para casi todas las aplicaciones que
se pretenda instalar en las distribuciones derivadas de Debian, como por
ejemplo en nuestro caso Ubuntu, BackBox, etc. Quedaría así el comando:

<span style="font-family:'Courier New', Courier, monospace;">apt-get
install unrar</span>

Alguna vez no te deja instalar unrar, por lo que se deberá añadir a el
comando unrar-free en vez  de     unrar.

Después se deberá localizar el directorio donde esta el archivo a
extraer, en mi caso es            /home/dudu/Descargas.

Se accede a el con el comando   <span
style="font-family:'Courier New', Courier, monospace;"> cd</span>   
 mas el directorio del archivo:

<span style="font-family:'Courier New', Courier, monospace;">      cd
/home/dudu/Descargas/</span>

Se comprueba los archivos dentro de este directorio escribiendo    
 <span style="font-family:'Courier New', Courier, monospace;">ls</span> 
en el terminal, esto muestra los archivos dentro de la carpeta en la que
estamos.

La mayoría de las aplicaciones te permiten ver una pequeña guía/manual
sobre las opciones del comando, de las aplicaciones, etc.  
Se accede a esta guía a través del comando    man  y la aplicación a
usar en nuestro caso unrar:  
<span style="font-family:'Courier New', Courier, monospace;">  
</span><span style="font-family:'Courier New', Courier, monospace;">   
    man unrar</span>

De esta guía se sale pulsando la letra <span
style="font-family:'Courier New', Courier, monospace;">  q    </span>  
Ahora bien, para extraer los archivos en el directorio actual se usa el
comando

<div>

<div>

            <span
style="font-family:'Courier New', Courier, monospace;">  unrar e
nombredelarchivo.rar</span>

</div>

</div>

<div>

</div>

<div>

Después de esto ya estaría extraído el archivo en el
directorio seleccionado, se puede utilizar en modo gráfico si se desea.

</div>

<div>

Esto es todo para extraer un .rar ,si tienen alguna duda escriban un
comentario y pregunten

</div>
