---
id: 955
title: Openstack-nova-api start error (Could not bind to 0.0.0.0, Address already in use)
date: 2015-03-16T17:23:45+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=955
permalink: /openstack-nova-api-start-error-could-not-bind-to-0-0-0-0-address-already-in-use/
categories:
  - OpenStack
tags:
  - address already in use
  - api
  - could
  - dead but pid file exists
  - error
  - not bind
  - nova
  - nova-api
  - nova-wsgi
  - openstack
  - update-rc.d
---
&nbsp;

Openstack-nova-api doesn't start, this error is  from the services boot priority in many times.
<blockquote># service openstack-nova-api start

2015-03-03 15:05:06.402 3313 ERROR nova.wsgi [-] Could not bind to
0.0.0.0:8775
2015-03-03 15:05:06.402 3313 CRITICAL nova [-] error: [Errno 98] Address
already in use

# service openstack-nova-api status

openstack-nova-api dead but pid file exists*</blockquote>
This Error happens because openstack-nova-api and openstack-nova-metadata-api use the same ports.
You can start nova-api stopping metadata-api service and starting nova-api before, then start again metadata-api service.
<blockquote># service openstack-nova-metadata-api stop
# service openstack-nova-api start
# service openstack-nova-metadata-api</blockquote>
This should fix your issue. After this you can set up boot order to this processes
<blockquote># update-rc.d openstack-nova-api defaults &lt;order&gt;</blockquote>
Example: If openstack-nova-metadata-api got an order boot of S90openstack-nova-metadata-api, you should use update-rc to set nova-api start before nova-metadata-api
<blockquote># update-rc.d openstack-nova-api defaults 90</blockquote>
This will set the priority of nova-api with the priority of nova-metadata-api, wich means that nova-api will run before metadata-api.

&nbsp;