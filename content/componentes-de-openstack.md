Title: Componentes de OpenStack
Date: 2014-08-27 16:41
Author: egongu90
Category: OpenStack
Tags: basico, cinder swift, cloud, componentes, computing, horizon, introducion, keystone, neutron, nova, openstack
Slug: componentes-de-openstack
Status: published

Desde su aparición en  2010, la comunidad de Openstack ha estado
añadiendo nuevos componentes y funcionalidades.

A día de hoy estos son los componentes oficiales de OpenStack

+--------------------------+--------------------------+--------------------------+
| **Servicio**             | **Componente**           | ** Descripcion**         |
+--------------------------+--------------------------+--------------------------+
| [Dashboard](http://docs. | [Horizon](http://docs.op |                          |
| openstack.org/admin-guid | enstack.org/admin-guide- | </p>                     |
| e-cloud/content/ch_getti | cloud/content/ch_getting | Interfaz gráfica que     |
| ng-started-with-openstac | -started-with-openstack. | permite interactuar con  |
| k.html)                  | html)                    | Openstack para la        |
|                          |                          | administración básica    |
|                          |                          | del servicio             |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Compute](http://docs.op | [Nova](http://docs.opens |                          |
| enstack.org/admin-guide- | tack.org/admin-guide-clo | </p>                     |
| cloud/content/ch_getting | ud/content/ch_getting-st | Encargada de la          |
| -started-with-openstack. | arted-with-openstack.htm | computación de la nube,  |
| html)                    | l)                       | gestiona y automatiza    |
|                          |                          | los recursos. Es la      |
|                          |                          | parte principal de       |
|                          |                          | OpenStack                |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Networking](http://docs | [Neutron](http://docs.op |                          |
| .openstack.org/admin-gui | enstack.org/admin-guide- | </p>                     |
| de-cloud/content/ch_gett | cloud/content/ch_getting | Gestiona la red y la     |
| ing-started-with-opensta | -started-with-openstack. | asignación de IPs a las  |
| ck.html)                 | html)                    | diferentes instancias    |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Object                  | [Swift](http://docs.open |                          |
| Storage](http://docs.ope | stack.org/admin-guide-cl | </p>                     |
| nstack.org/admin-guide-c | oud/content/ch_getting-s | Proporciona un Sistema   |
| loud/content/ch_getting- | tarted-with-openstack.ht | de almacenamiento        |
| started-with-openstack.h | ml)                      | redundado y escalable.   |
| tml)                     |                          | No es persistente el     |
|                          |                          | almacenamiento           |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Block                   | [Cinder](http://docs.ope |                          |
| Storage](http://docs.ope | nstack.org/admin-guide-c | </p>                     |
| nstack.org/admin-guide-c | loud/content/ch_getting- | Proporciona un           |
| loud/content/ch_getting- | started-with-openstack.h | almacenamiento en bloque |
| started-with-openstack.h | tml)                     | persistente              |
| tml)                     |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Identity                | [Keystone](http://docs.o |                          |
| service](http://docs.ope | penstack.org/admin-guide | </p>                     |
| nstack.org/admin-guide-c | -cloud/content/ch_gettin | Servicio de              |
| loud/content/ch_getting- | g-started-with-openstack | autenticación y          |
| started-with-openstack.h | .html)                   | autorización de          |
| tml)                     |                          | Openstack                |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Image                   | [Glance](http://docs.ope |                          |
| Service](http://docs.ope | nstack.org/admin-guide-c | </p>                     |
| nstack.org/admin-guide-c | loud/content/ch_getting- | Openstack utiliza este   |
| loud/content/ch_getting- | started-with-openstack.h | servicio para el uso de  |
| started-with-openstack.h | tml)                     | las imagines de disco    |
| tml)                     |                          | durante la asignación de |
|                          |                          | instancias               |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Telemetry](http://docs. | [Ceilometer](http://docs |                          |
| openstack.org/admin-guid | .openstack.org/admin-gui | </p>                     |
| e-cloud/content/ch_getti | de-cloud/content/ch_gett | Monitorización para      |
| ng-started-with-openstac | ing-started-with-opensta | facturación con el       |
| k.html)                  | ck.html)                 | cliente                  |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Orchestration](http://d | [Heat](http://docs.opens |                          |
| ocs.openstack.org/admin- | tack.org/admin-guide-clo | </p>                     |
| guide-cloud/content/ch_g | ud/content/ch_getting-st | Permite la orquestación  |
| etting-started-with-open | arted-with-openstack.htm | de diferentes            |
| stack.html)              | l)                       | aplicaciones basadas en  |
|                          |                          | la nube, tales como AWS, |
|                          |                          | etc.                     |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+
| [Database ](http://docs. | [Trove](http://docs.open |                          |
| openstack.org/admin-guid | stack.org/admin-guide-cl | </p>                     |
| e-cloud/content/ch_getti | oud/content/ch_getting-s | Una base de datos        |
| ng-started-with-openstac | tarted-with-openstack.ht | escalable para el uso de |
| k.html)                  | ml)                      | DBaaS                    |
|                          |                          |                          |
|                          |                          | <p>                      |
|                          |                          |                          |
+--------------------------+--------------------------+--------------------------+


