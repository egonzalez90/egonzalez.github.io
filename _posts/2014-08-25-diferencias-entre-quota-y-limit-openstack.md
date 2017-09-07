---
id: 563
title: Diferencias entre Quota y Limit Openstack
date: 2014-08-25T13:33:00+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=563
permalink: /diferencias-entre-quota-y-limit-openstack/
snap_isAutoPosted:
  - "1"
snap_MYURL:
  - ""
snapEdIT:
  - "1"
snapFB:
  - N;
snapTW:
  - N;
kopa_resolution_total_view:
  - "5"
post_views_count:
  - "1"
image: /wp-content/uploads/2014/08/openstack-logo512-672x372.png
categories:
  - OpenStack
tags:
  - cloud
  - computing
  - diference
  - diferencia
  - limit
  - limite operacional
  - nova
  - openstack
  - que es
  - quota
  - quota-defaults
---
Las quotas en OpenStack se usan para evitar la saturacion de las capacidades del sistema, por ejemplo el máximo de GB permitidos a un tenant(o proyecto), de esta forma se controlará mas y se tendrá un rendimiento optimo de nuestra nube.
Mucha gente no sabe cual es la diferencia entre estos dos terminos en OpenStack, pues bien, para hacerlo mas visual lanzaremos el comando:
<pre class="prettyprint"><code style="color: inherit;"><span class="pln" style="color: #000000;">$ nova quota</span><span class="pun" style="color: #666600;">-</span><span class="pln" style="color: #000000;">defaults
</span><span class="pun" style="color: #666600;">+-----------------------------+-------+
</span><span class="pun" style="color: #666600;">|</span><span class="typ" style="color: #660066;">Quota                        </span><span class="pun" style="color: #666600;">| </span><span class="typ" style="color: #660066;">Limit </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">+-----------------------------+-------+</span><span class="pun" style="color: #666600;">
</span><span class="pln" style="color: #000000;">| instances                   </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">10   </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> cores                       </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">20   </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> ram                         </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">51200</span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> floating_ips                </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">10   </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> fixed_ips                   </span><span class="pun" style="color: #666600;">|  </span><span class="pun" style="color: #666600;">-</span><span class="lit" style="color: #006666;">1   </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> metadata_items              </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">128  </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> injected_files              </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">5    </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> injected_file_content_bytes </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">10240</span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> injected_file_path_bytes    </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">255  </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> key_pairs                   </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">100  </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> security_groups             </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">10   </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">|</span><span class="pln" style="color: #000000;"> security_group_rules        </span><span class="pun" style="color: #666600;">|  </span><span class="lit" style="color: #006666;">20   </span><span class="pun" style="color: #666600;">|
</span><span class="pun" style="color: #666600;">+-----------------------------+-------+</span></code></pre>
Este comando nos muestra 2 columnas delimitadas, en una Quota y en otra Limit

* Quota es el nombre del limite operacional
* Limit son los valores limite de las quotas, lo que es lo mismo, el valor del limite operacional que se le va a poder asignar a un tenant o proyecto

Visto asi es mas facil de asimilarlo en nuestra cabeza para un mejor entendimiento ¿verdad?
Espero haber ayudado en vuestras dudas, un saludo