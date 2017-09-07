Title: Creación de claves con OpenPGP
Date: 2014-03-30 15:21
Author: egongu90
Category: Linux
Tags: asimetrico, cifrado, clave, linux, opengpg, openpgp, Seguridad, simetrico
Slug: creacion-de-claves-con-opengpg
Status: published

**En esta entrada mostrare el proceso para la creación de claves
simétricas y asimétricas con openpgp en Linux**

[<!--more-->](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png)

<span style="color: #ff0000;">***Clave Simétrica ***</span>

**En Linux por defecto te viene instalado openpgp.**

 

**Para crear una clave simétrica, deberemos escribir gpg con el
modificador –c y el nombre del archivo creado que se quiera encriptar**

[![1](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/1.png)

 

**Esto nos solicitara la clave que queramos asignarla dos veces, la
rellenamos y ya tenemos el archivo encriptado de forma simétrica.**

**Para desencriptar usaremos el comando gpg con el modificado –d y el
archivo que queramos desencriptar, que tiene que acabar en .gpg**

**Esto nos solicitara la clave que le habíamos puesto, y a continuación
nos creara el archivo desencriptado**

[![2](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/2.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/2.png)

**<span style="color: #ff0000;">Clave asimétrica </span>**

**Para crear la clave asimétrica, pondremos el comando gpg –gen-key**

[![3](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/3.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/3.png)

**Esto nos solicitara que le indiquemos el algoritmo de cifrado que
deseemos utilizar, nosotros usaremos la opción 1 default RSA**

[![4](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/4.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/4.png)

**Ahora nos pide que indiquemos la longitud de bits de las claves RSA,
nosotros pondremos un término medio y el que nos aconseja, esta longitud
es 2048**

[![5](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/5.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/5.png)

**Ahora indicaremos el tiempo que queremos que tenga de vida la clave,
nosotros usaremos 1y, para indicar 1 año**

[![6](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/6.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/6.png)

**Nos indicara el día y hora de la expiración de la clave y preguntara
si es correcto, damos y avanzamos**

[![7](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/7.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/7.png)

**Ahora nos preguntara el nombre real del que crea la clave, yo pongo el
nombre de usuario**

[![8](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/8.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/8.png)

**Seguidamente, nos preguntara el email,  le ponemos, y avanzamos a lo
siguiente**

[![9](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/9.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/9.png)

**Después nos dirá si todo es correcto y nos mostrara el nombre e email
del usuario, damos O y pasamos al siguiente paso**

[![10](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/10.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/10.png)

**Lo siguiente sería crear la clave, para ello la indicamos la clave que
queramos usar, la repetimos dos veces**

[![12](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/12.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/12.png)

**Ahora generara el proceso de creación de la clave, esto nos puede
solicitar que utilicemos recursos del sistema, abrimos ventanas,
navegadores, etc para que complete la creación de la clave asimétrica.**

**Después nos dará un mensaje con la información del proceso, deberías
ser que se ha creado correctamente todo.**

[![13](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/131.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/131.png)

**Ahora iremos a comprobar que se han creado las claves correctamente,
para ello utilizaremos el comando gpg –k, que nos mostrara las claves
que tenemos creadas.**

**Aquí vemos la clave pública y la privada, y en el medio de ambas, el
nombre de usuario de la clave.**

[![14](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/141.png)](http://vps38574.vps.ovh.ca/wp-content/uploads/2014/03/141.png)
