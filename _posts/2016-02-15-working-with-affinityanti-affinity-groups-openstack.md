---
id: 1152
title: Working with affinity/anti-affinity groups OpenStack
date: 2016-02-15T21:05:37+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=1152
permalink: /working-with-affinityanti-affinity-groups-openstack/
image: /wp-content/uploads/2015/09/learn-about-openstack-badge.png
categories:
  - OpenStack
tags:
  - affinity
  - anti-affinity
  - filter
  - groups
  - liberty
  - nova
  - openstack
  - rdo
  - scheduler
  - ServerGroupAffinityFilter
  - ServerGroupAntiAffinityFilter
  - working
---
In a previous post, you learned how to segregate resources with <a href="http://egonzalez.org/openstack-segregation-with-availability-zones-and-host-aggregates/" target="_blank">Availability Zones and Host Aggregates</a>, those methods allows the end user to specify where and on which types of resources their instances should be running.


At this post, you will learn how specify to nova where nova-scheduler should schedule your instances based on two policies. These policies define if instances should share the same hypervisor (affinity rule) or if not depending of user needs(anti-affinity rule).

First, you need to modify nova.conf and allow nova-scheduler to filter based on affinity rules. Add <code>ServerGroupAntiAffinityFilter</code> and <code>ServerGroupAffinityFilter</code> filters to scheduler default filter option.
<pre>
# vi /etc/nova.conf

scheduler_default_filters=RetryFilter,AvailabilityZoneFilter,RamFilter,ComputeFilter,ComputeCapabilitiesFilter,ImagePropertiesFilter,CoreFilter,ServerGroupAntiAffinityFilter,ServerGroupAffinityFilter
</pre>
Restart nova-scheduler to apply changes
<pre>
systemctl restart openstack-nova-scheduler
</pre>
Once nova-scheduler has been restarted, we can create a group of servers based on affinity policy (All instances at this group will be launched in the same hypervisor)
<pre>
nova server-group-create instancestogethergroup affinity
+--------------------------------------+------------------------+---------------+---------+----------+
| Id                                   | Name                   | Policies      | Members | Metadata |
+--------------------------------------+------------------------+---------------+---------+----------+
| 27abe662-c37e-431c-9715-0d2137fc5519 | instancestogethergroup | [u'affinity'] | []      | {}       |
+--------------------------------------+------------------------+---------------+---------+----------+
</pre>
Now create two instances, add <code>--hint group=GROUP-ID</code> option to specify the group where instances will be members. 
<pre>
nova boot --image a6d7a606-f725-480a-9b1b-7b3ae39b93d4 --flavor m1.tiny --nic net-id=154da7a8-fa49-415e-9d35-c840b144a8df --hint group=27abe662-c37e-431c-9715-0d2137fc5519 affinity1
nova boot --image a6d7a606-f725-480a-9b1b-7b3ae39b93d4 --flavor m1.tiny --nic net-id=154da7a8-fa49-415e-9d35-c840b144a8df --hint group=27abe662-c37e-431c-9715-0d2137fc5519 affinity2
</pre>
Ensure the instances are properly mapped to the group.
<pre>
nova server-group-get 27abe662-c37e-431c-9715-0d2137fc5519 
+--------------------------------------+------------------------+---------------+------------------------------------------------------------------------------------+----------+
| Id                                   | Name                   | Policies      | Members                                                                            | Metadata |
+--------------------------------------+------------------------+---------------+------------------------------------------------------------------------------------+----------+
| 27abe662-c37e-431c-9715-0d2137fc5519 | instancestogethergroup | [u'affinity'] | [u'b8b72a0a-c981-430e-a909-13d23d928655', u'8affefff-0072-47e3-8d11-2ddf26e48b82'] | {}       |
+--------------------------------------+------------------------+---------------+------------------------------------------------------------------------------------+----------+
</pre>
Once instances are running, ensure they share the same hypervisor as we specify in the affinity policy.
<pre>
# nova show affinity1 | grep hypervisor_hostname
| OS-EXT-SRV-ATTR:hypervisor_hostname  | compute2az
# nova show affinity2 | grep hypervisor_hostname
| OS-EXT-SRV-ATTR:hypervisor_hostname  | compute2az  
</pre>
Now we create an anti-affinity policy based group.
<pre>
nova server-group-create farinstancesgroup anti-affinity
+--------------------------------------+-------------------+--------------------+---------+----------+
| Id                                   | Name              | Policies           | Members | Metadata |
+--------------------------------------+-------------------+--------------------+---------+----------+
| 988a9fd2-3a97-481e-b083-fee36b33009d | farinstancesgroup | [u'anti-affinity'] | []      | {}       |
+--------------------------------------+-------------------+--------------------+---------+----------+
</pre>
Launch two instances and attach them to the anti-affinity group.
<pre>
nova boot --image a6d7a606-f725-480a-9b1b-7b3ae39b93d4 --flavor m1.tiny --nic net-id=154da7a8-fa49-415e-9d35-c840b144a8df --hint group=988a9fd2-3a97-481e-b083-fee36b33009d anti-affinity1
nova boot --image a6d7a606-f725-480a-9b1b-7b3ae39b93d4 --flavor m1.tiny --nic net-id=154da7a8-fa49-415e-9d35-c840b144a8df --hint group=988a9fd2-3a97-481e-b083-fee36b33009d anti-affinity2
</pre>
Ensure the instances are in the anti-affinity group
<pre>
nova server-group-get 988a9fd2-3a97-481e-b083-fee36b33009d 
+--------------------------------------+-------------------+--------------------+------------------------------------------------------------------------------------+----------+
| Id                                   | Name              | Policies           | Members                                                                            | Metadata |
+--------------------------------------+-------------------+--------------------+------------------------------------------------------------------------------------+----------+
| 988a9fd2-3a97-481e-b083-fee36b33009d | farinstancesgroup | [u'anti-affinity'] | [u'cfb45193-9a7c-436f-ac2d-59a7a9a854ae', u'25dc8671-0c9a-4774-90cf-7394380f91ef'] | {}       |
+--------------------------------------+-------------------+--------------------+------------------------------------------------------------------------------------+----------+
</pre>
Once instances are running, ensure they are in different hypervisors as we specify in the anti-affinity policy.
<pre>
# nova show anti-affinity1 | grep hypervisor_hostname
| OS-EXT-SRV-ATTR:hypervisor_hostname  | compute2az
# nova show anti-affinity2 | grep hypervisor_hostname
| OS-EXT-SRV-ATTR:hypervisor_hostname  | compute1az   
</pre>



Regards, Eduardo Gonzalez