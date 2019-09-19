| Muchos usuarios de Linux pensaran que es una bobada explicar este
  tema, pero créanme que muchos usuarios noveles de las distribuciones
  de Ubuntu no saben como hacerlo.
| Os voy a explicar como utilizar la aplicación Unrar en modo texto,
  puesto que no tiene opción gráfica.
| En primer lugar hay que realizar el comando básico    apt-get install
      , esto servirá para casi todas las aplicaciones que se pretenda
  instalar en las distribuciones derivadas de Debian, como por ejemplo
  en nuestro caso Ubuntu, BackBox, etc. Quedaría así el comando:

apt-get install unrar

Alguna vez no te deja instalar unrar, por lo que se deberá añadir a el
comando unrar-free en vez  de     unrar.

Después se deberá localizar el directorio donde esta el archivo a
extraer, en mi caso es            /home/dudu/Descargas.

Se accede a el con el comando    cd     mas el directorio del archivo:

      cd /home/dudu/Descargas/

Se comprueba los archivos dentro de este directorio escribiendo      ls 
en el terminal, esto muestra los archivos dentro de la carpeta en la que
estamos.

| La mayoría de las aplicaciones te permiten ver una pequeña guía/manual
  sobre las opciones del comando, de las aplicaciones, etc.
| Se accede a esta guía a través del comando    man  y la aplicación a
  usar en nuestro caso unrar:
| 
          man unrar

| De esta guía se sale pulsando la letra   q    
| Ahora bien, para extraer los archivos en el directorio actual se usa
  el comando

.. raw:: html

   <div>

.. raw:: html

   <div>

              unrar e nombredelarchivo.rar

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Después de esto ya estaría extraído el archivo en el
directorio seleccionado, se puede utilizar en modo gráfico si se desea.

.. raw:: html

   </div>

.. raw:: html

   <div>

Esto es todo para extraer un .rar ,si tienen alguna duda escriban un
comentario y pregunten

.. raw:: html

   </div>
