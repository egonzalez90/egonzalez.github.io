---
id: 887
title: Fix Keystone malformed endpoint url 500 Openstack
date: 2015-02-04T17:34:56+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=887
permalink: /fix-keystone-malformed-endpoint-url-500-openstack/
categories:
  - OpenStack
tags:
  - "500"
  - database
  - delete
  - endpoint
  - entry
  - error
  - fix
  - http
  - keystone
  - malformed
  - openstack
---
&nbsp;

How to fix error malformed endpoint url (HTTP 500) in Openstack
<h2><span style="color: #ff0000;">DON'T DO IT IN A PRODUCTION ENVIRONMENT</span></h2>
1st - Delete the malformed endpoint in the database.
<blockquote>mysql -u root -p

# use keystone;

# select * from endpoint;

# delete from endpoint where service_id="ENDPOINT_ID";</blockquote>
2nd - Recreate the endpoint with the keystone endpoint-create command.

&nbsp;

&nbsp;

&nbsp;