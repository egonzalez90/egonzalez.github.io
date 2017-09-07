Title: Openstack-nova-api start error (Could not bind to 0.0.0.0, Address already in use)
Date: 2015-03-16 17:23
Author: egongu90
Category: OpenStack
Tags: address already in use, api, could, dead but pid file exists, error, not bind, nova, nova-api, nova-wsgi, openstack, update-rc.d
Slug: openstack-nova-api-start-error-could-not-bind-to-0-0-0-0-address-already-in-use
Status: published

 

Openstack-nova-api doesn't start, this error is  from the services boot
priority in many times.

> \# service openstack-nova-api start
>
> 2015-03-03 15:05:06.402 3313 ERROR nova.wsgi [-] Could not bind to  
>  0.0.0.0:8775  
>  2015-03-03 15:05:06.402 3313 CRITICAL nova [-] error: [Errno 98]
> Address  
>  already in use
>
> \# service openstack-nova-api status
>
> openstack-nova-api dead but pid file exists\*

This Error happens because openstack-nova-api and
openstack-nova-metadata-api use the same ports.  
You can start nova-api stopping metadata-api service and starting
nova-api before, then start again metadata-api service.

> \# service openstack-nova-metadata-api stop  
>  \# service openstack-nova-api start  
>  \# service openstack-nova-metadata-api

This should fix your issue. After this you can set up boot order to this
processes

> \# update-rc.d openstack-nova-api defaults \<order\>

Example: If openstack-nova-metadata-api got an order boot of
S90openstack-nova-metadata-api, you should use update-rc to set nova-api
start before nova-metadata-api

> \# update-rc.d openstack-nova-api defaults 90

This will set the priority of nova-api with the priority of
nova-metadata-api, wich means that nova-api will run before
metadata-api.

 
