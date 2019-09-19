--- layout: post title: Componentes de OpenStack date: 2014-08-27
16:41:58.000000000 +02:00 type: post parent_id: '0' published: true
password: '' status: publish categories: - OpenStack tags: - basico -
cinder swift - cloud - componentes - computing - horizon - introducion -
keystone - neutron - nova - openstack meta: \_edit_last: '2'
\_login_radius_meta: a:1:{s:7:"sharing";i:0;}
kopa_resolution_total_view: '8' \_thumbnail_id: '569' snap_MYURL: ''
snapEdIT: '1' snapFB: N; snap_isAutoPosted: '1' snapTW: N;
post_views_count: '1' \_wpas_skip_5226565: '1' \_wpas_skip_10228321: '1'
\_wpas_skip_8706018: '1' \_jetpack_related_posts_cache:
a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1567636798;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:788;}i:1;a:1:{s:2:"id";i:816;}i:2;a:1:{s:2:"id";i:809;}}}}
dsq_thread_id: '6098717642' author: login: egongu90 email:
egongu90@hotmail.com display_name: Editor first_name: '' last_name: ''
permalink: "/componentes-de-openstack/" ---

Desde su aparición en  2010, la comunidad de Openstack ha estado
añadiendo nuevos componentes y funcionalidades.

A día de hoy estos son los componentes oficiales de OpenStack

+----------------------+----------------------+----------------------+
| **Servicio**         | **Componente**       | ** Descripcion**     |
+----------------------+----------------------+----------------------+
| `Dashboard <http://d | `Horizon <http://doc |                      |
| ocs.openstack.org/ad | s.openstack.org/admi | Interfaz gráfica que |
| min-guide-cloud/cont | n-guide-cloud/conten | permite interactuar  |
| ent/ch_getting-start | t/ch_getting-started | con Openstack para   |
| ed-with-openstack.ht | -with-openstack.html | la administración    |
| ml>`__               | >`__                 | básica del servicio  |
|                      |                      |                      |
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| `Compute <http://doc | `Nova <http://docs.o |                      |
| s.openstack.org/admi | penstack.org/admin-g | Encargada de la      |
| n-guide-cloud/conten | uide-cloud/content/c | computación de la    |
| t/ch_getting-started | h_getting-started-wi | nube, gestiona y     |
| -with-openstack.html | th-openstack.html>`_ | automatiza los       |
| >`__                 | _                    | recursos. Es la      |
|                      |                      | parte principal de   |
|                      |                      | OpenStack            |
|                      |                      |                      |
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| `Networking <http:// | `Neutron <http://doc |                      |
| docs.openstack.org/a | s.openstack.org/admi | Gestiona la red y la |
| dmin-guide-cloud/con | n-guide-cloud/conten | asignación de IPs a  |
| tent/ch_getting-star | t/ch_getting-started | las diferentes       |
| ted-with-openstack.h | -with-openstack.html | instancias           |
| tml>`__              | >`__                 |                      |
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| `Object              | `Swift <http://docs. |                      |
| Storage <http://docs | openstack.org/admin- | Proporciona un       |
| .openstack.org/admin | guide-cloud/content/ | Sistema de           |
| -guide-cloud/content | ch_getting-started-w | almacenamiento       |
| /ch_getting-started- | ith-openstack.html>` | redundado y          |
| with-openstack.html> | __                   | escalable. No es     |
| `__                  |                      | persistente el       |
|                      |                      | almacenamiento       |
|                      |                      |                      |
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| `Block               | `Cinder <http://docs |                      |
| Storage <http://docs | .openstack.org/admin | Proporciona un       |
| .openstack.org/admin | -guide-cloud/content | almacenamiento en    |
| -guide-cloud/content | /ch_getting-started- | bloque persistente   |
| /ch_getting-started- | with-openstack.html> |                      |
| with-openstack.html> | `__                  |                      |
| `__                  |                      |                      |
+----------------------+----------------------+----------------------+
| `Identity            | `Keystone <http://do |                      |
| service <http://docs | cs.openstack.org/adm | Servicio de          |
| .openstack.org/admin | in-guide-cloud/conte | autenticación y      |
| -guide-cloud/content | nt/ch_getting-starte | autorización de      |
| /ch_getting-started- | d-with-openstack.htm | Openstack            |
| with-openstack.html> | l>`__                |                      |
| `__                  |                      |                      |
+----------------------+----------------------+----------------------+
| `Image               | `Glance <http://docs |                      |
| Service <http://docs | .openstack.org/admin | Openstack utiliza    |
| .openstack.org/admin | -guide-cloud/content | este servicio para   |
| -guide-cloud/content | /ch_getting-started- | el uso de las        |
| /ch_getting-started- | with-openstack.html> | imagines de disco    |
| with-openstack.html> | `__                  | durante la           |
| `__                  |                      | asignación de        |
|                      |                      | instancias           |
|                      |                      |                      |
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| `Telemetry <http://d | `Ceilometer <http:// |                      |
| ocs.openstack.org/ad | docs.openstack.org/a | Monitorización para  |
| min-guide-cloud/cont | dmin-guide-cloud/con | facturación con el   |
| ent/ch_getting-start | tent/ch_getting-star | cliente              |
| ed-with-openstack.ht | ted-with-openstack.h |                      |
| ml>`__               | tml>`__              |                      |
+----------------------+----------------------+----------------------+
| `Orchestration <http | `Heat <http://docs.o |                      |
| ://docs.openstack.or | penstack.org/admin-g | Permite la           |
| g/admin-guide-cloud/ | uide-cloud/content/c | orquestación de      |
| content/ch_getting-s | h_getting-started-wi | diferentes           |
| tarted-with-openstac | th-openstack.html>`_ | aplicaciones basadas |
| k.html>`__           | _                    | en la nube, tales    |
|                      |                      | como AWS, etc.       |
|                      |                      |                      |
|                      |                      |                      |
+----------------------+----------------------+----------------------+
| `Database  <http://d | `Trove <http://docs. |                      |
| ocs.openstack.org/ad | openstack.org/admin- | Una base de datos    |
| min-guide-cloud/cont | guide-cloud/content/ | escalable para el    |
| ent/ch_getting-start | ch_getting-started-w | uso de DBaaS         |
| ed-with-openstack.ht | ith-openstack.html>` |                      |
| ml>`__               | __                   |                      |
+----------------------+----------------------+----------------------+
