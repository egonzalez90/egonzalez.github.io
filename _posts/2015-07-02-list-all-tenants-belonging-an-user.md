---
id: 982
title: 'List all tenants belonging an user  Keystone v2'
date: 2015-07-02T14:29:33+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=982
permalink: /list-all-tenants-belonging-an-user/
categories:
  - OpenStack
tags:
  - all
  - bash
  - belong
  - curl
  - GET
  - how
  - inside
  - keystone
  - keystoneclient
  - keystonev2
  - list
  - openstack
  - python
  - role
  - script
  - tenant
  - tenants
  - to
  - Token
  - user
  - users
  - v2
---
&nbsp;

Here is a simple script to list all tenants belonging an user:

&nbsp;
<pre><code>#!/bin/bash

echo -n "Username : " ; read usercheck

for userid in $(keystone user-list | grep -w $usercheck | awk '{print$2}')
	do
	for tenant in $(keystone tenant-list | awk 'NR&gt;3 &amp;&amp; /^|/ {print$2}')
	do
		for tenantid in $(keystone user-role-list --user $userid --tenant $tenant | awk 'NR&gt;3 &amp;&amp; /^|/ {print$8}')
		do
			keystone tenant-list | grep $tenantid | awk '{print$4}'
		done
	done
done
</code></pre>
&nbsp;
Also you can run all in a simple cmd line:
&nbsp;
<pre><code>
echo -n "user name "; read usercheck; for userid in $(keystone user-list | grep $usercheck | awk '{print$2}'); do echo $userid | for tenant in $(keystone tenant-list | awk 'NR&gt;3 &amp;&amp; /^|/ {print$2}'); do echo $tenant | for tenantid in $(keystone user-role-list --user $userid --tenant $tenant | awk 'NR>3 && /^|/ {print$8}'); do keystone tenant-list | grep $tenantid | awk '{print$4}'; done ; done ; done

</code></pre>
&nbsp;
If you are a developer, probably you need to list all tenants in a HTTP request, for this purpose you can use curl to the port 5000 of keystone
&nbsp;
<pre><code>
curl -i -X GET http://KEYSTONEIP:5000/v2.0/tenants -H "User-Agent: python-keystoneclient" -H "X-Auth-Token: USERTOKEN"
</code></pre>
&nbsp;
I have saved the user token in a OS_VARIABLE called OS_TOKEN, if you don't do that, you should input all the token in the HTTP request.
For example: 
&nbsp;
<pre><code>
curl -i -X GET http://192.168.1.11:5000/v2.0/tenants -H "User-Agent: python-keystoneclient" -H "X-Auth-Token: $OS_TOKEN"
</code></pre>