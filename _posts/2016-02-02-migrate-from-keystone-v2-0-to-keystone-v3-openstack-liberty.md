---
id: 1140
title: Migrate from keystone v2.0 to keystone v3 OpenStack Liberty
date: 2016-02-02T19:43:46+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=1140
permalink: /migrate-from-keystone-v2-0-to-keystone-v3-openstack-liberty/
dsq_thread_id:
  - "6094296853"
image: /wp-content/uploads/2015/09/learn-about-openstack-badge.png
categories:
  - OpenStack
tags:
  - auth
  - auth_url
  - core
  - guide
  - how to
  - keystone
  - migrate
  - openstack
  - packstack
  - rdo
  - services
  - Tutorial
  - v2.0
  - v3
  - version
---
Migrate from keystone v2.0 to v3 isn't as easy like just changing the endpoints at the database, every service must be configured to authenticate against keystone v3.

I've been working on that the past few days looking for a method, with the purpose of facilitate operators life's who need this kind of migration.
I have to thank Adam Young work, i followed his blog to make a first configuration idea, after that, i configured all core services to make use of keystone v3.
If you want to check Adam's blog, follow this link: <a href="http://adam.younglogic.com/2015/05/rdo-v3-only/" target="_blank">http://adam.younglogic.com/2015/05/rdo-v3-only/</a>

I used OpenStack Liberty installed with RDO packstack over CentOS 7 servers.
The example IP used is <code>192.168.200.168</code>, use your own according your needs.
Password used for all services is <code>PASSWD1234</code>, use your own password, you can locate your passwords at the packstack answer file. 

<ins datetime="2016-02-02T18:25:21+00:00"><strong>Horizon</strong></ins>

First we configure Horizon with keystone v3 as below:
<pre>
vi /etc/openstack-dashboard/local_settings

OPENSTACK_API_VERSIONS = {
    "identity": 3
}

OPENSTACK_KEYSTONE_MULTIDOMAIN_SUPPORT = True
OPENSTACK_KEYSTONE_DEFAULT_DOMAIN = 'Default'
</pre>

<ins datetime="2016-02-02T18:25:21+00:00"><strong>keystone</strong></ins>

Check your current identity endpoints
<pre>
mysql  --user keystone_admin --password=PASSWD1234  keystone -e "select interface, url from endpoint where service_id =  (select id from service where service.type = 'identity');"
</pre>
Change your public, admin and internal endpoints with v3 at the end, instead of v2.0
<pre>
mysql  --user keystone_admin --password=PASSWD1234   keystone -e "update endpoint set   url  = 'http://192.168.200.178:5000/v3' where  interface ='internal' and  service_id =  (select id from service where service.type = 'identity');"

mysql  --user keystone_admin --password=PASSWD1234   keystone -e "update endpoint set   url  = 'http://192.168.200.178:5000/v3' where  interface ='public' and  service_id =  (select id from service where service.type = 'identity');"

mysql  --user keystone_admin --password=PASSWD1234   keystone -e "update endpoint set   url  = 'http://192.168.200.178:35357/v3' where  interface ='admin' and  service_id =  (select id from service where service.type = 'identity');"
</pre>
Ensure the endpoints are properly created
<pre>
mysql  --user keystone_admin --password=KEYSTONE_DB_PW   keystone -e "select interface, url from endpoint where service_id =  (select id from service where service.type = 'identity');"
</pre>
Create a source file or edit keystonerc_admin with the following data
<pre>
vi v3_keystone

unset OS_SERVICE_TOKEN
export OS_USERNAME=admin
export OS_PASSWORD=PASSWD1234
export OS_AUTH_URL=http://192.168.200.178:5000/v3
export OS_PROJECT_NAME=admin
export OS_PROJECT_DOMAIN_NAME=Default
export OS_USER_DOMAIN_NAME=Default
export OS_REGION_NAME=RegionOne
export PS1='[\u@\h \W(keystone_admin)]\$ '
export OS_IDENTITY_API_VERSION=3
</pre>
Comment both pipelines, in public_api and admin_api
<pre>
vi /usr/share/keystone/keystone-dist-paste.ini

[pipeline:public_api]
# The last item in this pipeline must be public_service or an equivalent
# application. It cannot be a filter.
#pipeline = sizelimit url_normalize request_id build_auth_context token_auth admin_token_auth json_body ec2_extension user_crud_extension public_service

[pipeline:admin_api]
# The last item in this pipeline must be admin_service or an equivalent
# application. It cannot be a filter.
#pipeline = sizelimit url_normalize request_id build_auth_context token_auth admin_token_auth json_body ec2_extension s3_extension crud_extension admin_service
</pre>
Comment v2.0 entries in composite:main and admin sections.
<pre>
[composite:main]
use = egg:Paste#urlmap
#/v2.0 = public_api
/v3 = api_v3
/ = public_version_api

[composite:admin]
use = egg:Paste#urlmap
#/v2.0 = admin_api
/v3 = api_v3
/ = admin_version_api
</pre>
Restart httpd to apply changes
<pre>
systemctl restart httpd
</pre>
Check whether keystone and horizon are properly working
The command below should prompt an user list, if not, check configuration in previous steps
<pre>
openstack user list
</pre>

<ins datetime="2016-02-02T18:25:21+00:00"><strong>Glance</strong></ins>

Edit the following files, with the content below:
<pre>
vi /etc/glance/glance-api.conf 
vi /etc/glance/glance-registry.conf 
vi /etc/glance/glance-cache.conf 

[keystone_authtoken]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = glance
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
</pre>
Comment the following lines:
<pre>
#auth_host=127.0.0.1
#auth_port=35357
#auth_protocol=http
#identity_uri=http://192.168.200.178:35357
#admin_user=glance
#admin_password=PASSWD1234
#admin_tenant_name=services
</pre>
Those lines, should be commented in all the other OpenStack core services at keystone_authtoken section

Edit the files below and comment the lines inside keystone_authtoken section.
<pre>
vi /usr/share/glance/glance-api-dist.conf 
vi /usr/share/glance/glance-registry-dist.conf 

[keystone_authtoken]
#admin_tenant_name = %SERVICE_TENANT_NAME%
#admin_user = %SERVICE_USER%
#admin_password = %SERVICE_PASSWORD%
#auth_host = 127.0.0.1
#auth_port = 35357
#auth_protocol = http
</pre>
Restart glance services
<pre>
openstack-service restart glance
</pre>
Ensure glance service is working
<pre>
openstack image list
</pre>


<ins datetime="2016-02-02T18:25:21+00:00"><strong>Nova</strong></ins>


Edit the file below and comment the lines inside keystone_authtoken
<pre>
vi /usr/share/nova/nova-dist.conf

[keystone_authtoken]
#auth_host = 127.0.0.1
#auth_port = 35357
#auth_protocol = http
</pre>
Edit nova.conf and add the auth content inside keystone_authtoken, don't forget to comment the lines related to the last auth method, which were commented in glance section.
<pre>
vi /etc/nova/nova.conf

[keystone_authtoken]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = nova
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
</pre>
Configure nova authentication against neutron
<pre>
[neutron]
          
auth_plugin = password
auth_url = http://192.168.200.178:35357
username = neutron
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
</pre>
Restart nova services to apply changes
<pre>
openstack-service restart nova
</pre>
Check if nova works
<pre>
openstack hypervisor list
</pre>


<ins datetime="2016-02-02T18:25:21+00:00"><strong>Neutron</strong></ins>


Comment or remove the following entries at api-paste.ini and add the new version auth lines 
<pre>
vi /etc/neutron/api-paste.ini 

[filter:authtoken]
#identity_uri=http://192.168.200.178:35357
#admin_user=neutron
#admin_password=PASSWD1234
#auth_uri=http://192.168.200.178:5000/v2.0
#admin_tenant_name=services

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = neutron
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
</pre>
Configure v3 authentication for metadata service, remember comment the old auth lines
<pre>
vi /etc/neutron/metadata_agent.ini

[DEFAULT]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = neutron
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
</pre>
Configure neutron server with v3 auth
<pre>
vi /etc/neutron/neutron.conf

nova_admin_auth_url = http://192.168.200.178:5000
# nova_admin_tenant_id =1fb93c84c6474c5ea92c0ed5f7d4a6a7
nova_admin_tenant_name = services


[keystone_authtoken]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = neutron
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000

#auth_uri = http://192.168.200.178:5000/v2.0
#identity_uri = http://192.168.200.178:35357
#admin_tenant_name = services
#admin_user = neutron
#admin_password = PASSWD1234
</pre>
Configure neutron auth against nova services
<pre>
[nova]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = nova
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
</pre>
Restart neutron services to apply changes
<pre>
openstack-service restart neutron
</pre>
Test correct neutron funtionality
<pre>
openstack network list
</pre>

<ins datetime="2016-02-02T18:25:21+00:00"><strong>Cinder</strong></ins>

Edit api-paste.ini with the following content
<pre>
vi /etc/cinder/api-paste.ini 

[filter:authtoken]
paste.filter_factory = keystonemiddleware.auth_token:filter_factory
auth_plugin = password
auth_url = http://192.168.200.178:35357
username = cinder
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000
#admin_tenant_name=services
#auth_uri=http://192.168.200.178:5000/v2.0
#admin_user=cinder
#identity_uri=http://192.168.200.178:35357
#admin_password=PASSWD1234
</pre>
Restart cinder services to apply changes
<pre>
openstack-service restart cinder
</pre>
Ensure cinder is properly running
<pre>
openstack volume create --size 1 testvolume
openstack volume list
</pre>
Now, you can check if nova is working fine, create an instance and ensure it is in ACTIVE state.
<pre>
openstack server create --flavor m1.tiny --image cirros --nic net-id=a1aa6336-9ae2-4ffb-99f5-1b6d1130989c testinstance
openstack server list
</pre>
If any error occurs, review configuration files


<ins datetime="2016-02-02T18:25:21+00:00"><strong>Swift</strong></ins>


Configure proxy server auth agains keystone v3
<pre>
vi /etc/swift/proxy-server.conf

[filter:authtoken]
log_name = swift
signing_dir = /var/cache/swift
paste.filter_factory = keystonemiddleware.auth_token:filter_factory
auth_plugin = password
auth_url = http://192.168.200.178:35357
username = swift
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000

#auth_uri = http://192.168.200.178:5000/v2.0
#identity_uri = http://192.168.200.178:35357
#admin_tenant_name = services
#admin_user = swift
#admin_password = PASSWD1234
delay_auth_decision = 1
cache = swift.cache
include_service_catalog = False
</pre>
Restart swift services to apply changes
<pre>
openstack-service restart swift
</pre>
Swift commands must be issued with python-openstackclient instead of swiftclient
If done with swiftclient a -V 3 option must be used in order to avoid issues

Check if swift works fine
<pre>
openstack container create testcontainer
</pre>


<ins datetime="2016-02-02T18:25:21+00:00"><strong>Ceilometer</strong></ins>


Configure ceilometer service in order to authenticate agains keystone v3
<pre>
[keystone_authtoken]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = ceilometer
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000

[service_credentials]

os_auth_url = http://controller:5000/v3
os_username = ceilometer
os_tenant_name = services
os_password = PASSWD1234
os_endpoint_type = internalURL
os_region_name = RegionOne
</pre>
Restart ceilometer services
<pre>
openstack-service restart ceilometer
</pre>
Check ceilometer funtionality
<pre>
ceilometer statistics -m memory
</pre>
<ins datetime="2016-02-02T18:25:21+00:00"><strong>Heat</strong></ins>

Configure Heat authentication, since trusts are not stable use password auth method
<pre>
vi /etc/heat/heat.conf

# Allowed values: password, trusts
#deferred_auth_method = trusts
deferred_auth_method = password
</pre>
Configure auth_uri and keystone_authtoken section
<pre>
# From heat.common.config
#
# Unversioned keystone url in format like http://0.0.0.0:5000. (string value)
#auth_uri =
auth_uri = http://192.168.200.178:5000

[keystone_authtoken]

auth_plugin = password
auth_url = http://192.168.200.178:35357
username = heat
password = PASSWD1234
project_name = services
user_domain_name = Default
project_domain_name = Default
auth_uri=http://192.168.200.178:5000

#admin_user=heat
#admin_password=PASSWD1234
#admin_tenant_name=services
#identity_uri=http://192.168.200.178:35357
#auth_uri=http://192.168.200.178:5000/v2.0
</pre>
Comment or remove heat-dist auth entries in order to avoid conflicts with your config files
<pre>
vi /usr/share/heat/heat-dist.conf 

[keystone_authtoken]
#auth_host = 127.0.0.1
#auth_port = 35357
#auth_protocol = http
#auth_uri = http://127.0.0.1:5000/v2.0
#signing_dir = /tmp/keystone-signing-heat
</pre>
Restart heat services to apply changes
<pre>
openstack-service restart heat
</pre>
Ensure heat authentication is properly configured with a simple heat template
<pre>
heat stack-create --template-file sample.yaml teststack
</pre>
Most issues occurs in the authentication between nova and neutron services, if instances does not launch as expected, review [nova] and [neutron] sections. 


Best regards, Eduardo Gonzalez
