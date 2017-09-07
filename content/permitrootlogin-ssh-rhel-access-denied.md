Title: PermitRootLogin ssh RHEL (Access Denied)
Date: 2014-08-25 11:55
Author: egongu90
Category: Linux
Tags: access, denied, enable root, linux, permitrootlogin, rhel, root, servicio, ssh, sshd
Slug: permitrootlogin-ssh-rhel-access-denied
Status: published

En algunos sistemas, el acceso por ssh al usuario root esta
deshabilitado por defecto, cuando intentemos logearnos nos mostrara el
error Access Denied, para habilitarlo deberemos modificar este archivo

> /etc/ssh/sshd/sshd\_config

Aquí buscaremos una linea en la que aparezca:

> PermitRootLogin no

Lo cambiaremos por:

> PermitRootLogin yes

Guardaremos y reiniciamos el servicio sshd

> service sshd restart

Ya podriamos acceder con el usuario root por ssh
