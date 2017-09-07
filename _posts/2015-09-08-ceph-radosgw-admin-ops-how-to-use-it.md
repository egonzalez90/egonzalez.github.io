---
id: 1014
title: Ceph RadosGW Admin Ops, how to use it
date: 2015-09-08T13:45:40+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=1014
permalink: /ceph-radosgw-admin-ops-how-to-use-it/
dsq_thread_id:
  - "6094296968"
categories:
  - OpenStack
tags:
  - admin
  - admin ops
  - ceph
  - header
  - ops
  - query
  - radosgw
  - script
  - sign
  - understand
  - usage
  - user
---
<br></br>
Using RadosGW admin ops for the first time, can be a real headache , for this purpose i have made this post, where you will understand how to use this API.
Let's start:

For issue a request through admin ops, you need to have a signature, this signature is make it signing a header.
The header must to be composed by the current date, the request type(GET/PUT/POST/DELETE) and the request itself.
This header must be signed by SSL including the admin ops secret on this signature.
Now , you can make a request.
Sometimes, the time is not the same as the radosgw node expect, you can hack on it changing the date=$(date) value with:
If your host has two hours more than the radosgw node, substract this two hours under $(( 10#$i-2)) variable, where 2 is the two hours to substract.
<pre>
date=$(for i in $(date "+%H") ; do date "+%a, %d %b %Y $(( 10#$i-2 )):%M:%S +0000" ; done)
</pre>
Examples:

Create a user named egonzalez:

<pre>
#!/bin/bash
token=U2JCD4ZG4D1XJOI5XNF4 ## USER_TOKEN
secret=+IFgr7POzLWS0i3hQnC+dd3DOAZObHoY5NYm6m3b ## USER_SECRET
query=$1
name=$2
query3="&uid="
query2=admin/user
query4="&quota-type=user"
date=$(date)
header="PUT\n\n\n${date}\n/${query2}"
sig=$(echo -en ${header} | openssl sha1 -hmac ${secret} -binary | base64)
curl -v -H "Date: ${date}" -H "Authorization: AWS ${token}:${sig}" -L -X PUT "http://10.0.2.10/${query2}?format=json${query3}${query}&display-name=${name}" -H "Host: 10.0.2.10"
##Change IPs with your own IPs
</pre>
Output:
<pre>
[ceph@adminnode scripts]$ sh createUser.sh egonzalez EgonzalezDescription
{"user_id":"egonzalez","display_name":"EgonzalezDescription","email":"","suspended":0,"max_buckets":1000,"subusers":[],"keys":[{"user":"egonzalez","access_key":"24FUKCWD6BL9T08DQ2JA","secret_key":"mEQdhcrsqOy7q6Snvu8B5d5A2Ek9OezJH+khwYvX"}],"swift_keys":[],"caps":[]}
</pre>
See egonzalez quotas
<pre>
#!/bin/bash
token=U2JCD4ZG4D1XJOI5XNF4 ## USER_TOKEN
secret=+IFgr7POzLWS0i3hQnC+dd3DOAZObHoY5NYm6m3b ## USER_SECRET
query=$1
query3="&uid="
query2=admin/user
query4="&quota-type=user"
date=$(date)
header="GET\n\n\n${date}\n/${query2}"
sig=$(echo -en ${header} | openssl sha1 -hmac ${secret} -binary | base64)
curl -v -H "Date: ${date}" -H "Authorization: AWS ${token}:${sig}" -L -X GET "http://10.0.2.10/${query2}?quota${query3}${query}&quota-type=user" -H "Host: 10.0.2.10"
##Change IPs with your own IPs
</pre>
Output:
<pre>
[ceph@adminnode scripts]$ sh getuserquota.sh egonzalez

{"enabled": true,"max_size_kb":1000,"max_objects":1000}Status: 200 OK
</pre>
See egonzalez user information.
<pre>
#!/bin/bash
token=U2JCD4ZG4D1XJOI5XNF4 ## USER_TOKEN
secret=+IFgr7POzLWS0i3hQnC+dd3DOAZObHoY5NYm6m3b ## USER_SECRET
query=$1
query3="&uid="
query2=admin/user
date=$(date)
header="GET\n\n\n${date}\n/${query2}"
sig=$(echo -en ${header} | openssl sha1 -hmac ${secret} -binary | base64)
curl -v -H "Date: ${date}" -H "Authorization: AWS ${token}:${sig}" -L -X GET "http://10.0.2.10/${query2}?format=json${query3}${query}" -H "Host: 10.0.2.10"
##Change IPs with your own IPs
</pre>
Output:
<pre>
[ceph@adminnode scripts]$ sh userInfo.sh egonzalez
{"user_id":"egonzalez","display_name":"EgonzalezDescription","email":"","suspended":0,"max_buckets":1000,"subusers":[],"keys":[{"user":"egonzalez","access_key":"24FUKCWD6BL9T08DQ2JA","secret_key":"mEQdhcrsqOy7q6Snvu8B5d5A2Ek9OezJH+khwYvX"}],"swift_keys":[],"caps":[]}
</pre>
When you really understand how admin ops works, is not as dificult to use it, just search at the official documentation and modify the desired values.

I hope this helps:

Regards, Eduardo.