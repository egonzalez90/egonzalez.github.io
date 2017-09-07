Title: Fix Keystone malformed endpoint url 500 Openstack
Date: 2015-02-04 17:34
Author: egongu90
Category: OpenStack
Tags: 500, database, delete, endpoint, entry, error, fix, http, keystone, malformed, openstack
Slug: fix-keystone-malformed-endpoint-url-500-openstack
Status: published

 

How to fix error malformed endpoint url (HTTP 500) in Openstack

<span style="color: #ff0000;">DON'T DO IT IN A PRODUCTION ENVIRONMENT</span>
----------------------------------------------------------------------------

1st - Delete the malformed endpoint in the database.

> mysql -u root -p
>
> \# use keystone;
>
> \# select \* from endpoint;
>
> \# delete from endpoint where service\_id="ENDPOINT\_ID";

2nd - Recreate the endpoint with the keystone endpoint-create command.

 

 

 
