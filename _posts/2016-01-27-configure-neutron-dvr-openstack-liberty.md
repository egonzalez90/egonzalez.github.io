---
id: 1124
title: Configure Neutron DVR OpenStack Liberty
date: 2016-01-27T20:13:38+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=1124
permalink: /configure-neutron-dvr-openstack-liberty/
dsq_thread_id:
  - "6094297081"
image: /wp-content/uploads/2015/09/learn-about-openstack-badge.png
categories:
  - OpenStack
tags:
  - --configure
  - distributed
  - dvr
  - fip
  - l3
  - liberty
  - neutron
  - openstack
  - packstack
  - qrouter
  - rdo
  - routers
  - snat
  - virtual
---
Distributed Virtual Routers aka DVR were created to avoid single point of failure on neutron nodes.
When using standard routers, all the traffic is passing out through Neutron servers. Inside network servers, router namespaces are created routing all traffic and NAT forwarding between instances and public networks. When a network node falls down, instance traffic will no longer be available until a new namespace is created and executed in another network node.
Distributed routers is a way to avoid the SPOF neutron nodes were. When using DVR, router namespaces, are directly created inside compute nodes where all instance and l3 traffic are routed.

If you want to know more about DVR check this awesome links:
<a href="http://blog.gampel.net/2014/12/openstack-neutron-distributed-virtual.html" target="_blank">http://blog.gampel.net/2014/12/openstack-neutron-distributed-virtual.html</a>
<a href="http://blog.gampel.net/2014/12/openstack-dvr2-floating-ips.html" target="_blank">http://blog.gampel.net/2014/12/openstack-dvr2-floating-ips.html</a>
<a href="http://blog.gampel.net/2015/01/openstack-DVR-SNAT.html" target="_blank">http://blog.gampel.net/2015/01/openstack-DVR-SNAT.html</a>

A previous OpenStack Liberty installation is required, mine was done with RDO packstack.

<strong><ins datetime="2016-01-27T18:47:58+00:00">Configure all Neutron Servers</ins></strong>

Edit ml2 configuration file with the following:

<pre>
# vi /etc/neutron/plugins/ml2/ml2_conf.ini

mechanism_drivers = openvswitch,l2population
type_drivers = flat,vlan,vxlan
tenant_network_types = vxlan
vni_ranges = 10:100
vxlan_group = 224.1.1.1
enable_security_group = True
</pre>
Edit neutron configuration file, enable DVR and uncomment dvr_base_mac option
<pre>
# vi /etc/neutron/neutron.conf

router_distributed = True
dvr_base_mac = fa:16:3f:00:00:00
</pre>
Configure l3 agent to use dvr_snat
<pre>
# vi /etc/neutron/l3_agent.ini

agent_mode = dvr_snat
</pre>
Restart neutron server
<pre>
systemctl restart neutron-server
</pre>
<strong><ins datetime="2016-01-27T18:47:58+00:00">Configure all Compute Nodes</ins></strong>

Install ml2 package 
<pre>
yum install openstack-neutron-ml2
</pre>
Edit openvswitch agent file as below:
<pre>
# vi /etc/neutron/plugins/ml2/openvswitch_agent.ini 

l2_population = True
arp_responder = True
enable_distributed_routing = True
</pre>
Enable DVR and select an interface driver to be used by l3 agent
<pre>
# vi /etc/neutron/l3_agent.ini

interface_driver = neutron.agent.linux.interface.OVSInterfaceDriver
agent_mode = dvr
</pre>
Edit ml2 configuration file as below:
<pre>
# vi /etc/neutron/plugins/ml2/ml2_conf.ini

type_drivers = flat,vlan,vxlan
tenant_network_types = vxlan
mechanism_drivers = openvswitch,l2population
vni_ranges = 10:100
vxlan_group = 224.1.1.1
enable_security_group = True
</pre>
Start and enable metadata agent in compute nodes
<pre>
systemctl start neutron-l3-agent neutron-metadata-agent
systemctl enable neutron-l3-agent neutron-metadata-agent
</pre>
Create an external bridge with an external IP associated on it
<pre>
# vi /etc/sysconfig/network-scripts/ifcfg-br-ex

DEVICE=br-ex
DEVICETYPE=ovs
TYPE=OVSBridge
BOOTPROTO=static
IPADDR=192.168.100.4                                                          
NETMASK=255.255.255.0
GATEWAY=192.168.100.1
ONBOOT=yes
</pre>    
Modify an unused interface connected with the same network as the IP configured with br-ex, edit the interface to be used as OVS port by br-ex
<pre>
# vi /etc/sysconfig/network-scripts/ifcfg-eth1
DEVICE=eth1
TYPE=OVSPort
DEVICETYPE=ovs
OVS_BRIDGE=br-ex
ONBOOT=yes
</pre>
Restart network service to apply changes on the interfaces and openvswith-agent
<pre>
systemctl restart network
systemctl restart neutron-openvswitch-agent
</pre>
Create an external network and a subnet on it
<pre>
neutron net-create external_network --provider:network_type flat --provider:physical_network extnet  --router:external --shared
neutron subnet-create --name public_subnet --enable_dhcp=False --allocation-pool=start=192.168.100.100,end=192.168.100.150 --gateway=192.168.100.1 external_network 192.168.100.0/24
</pre>
Create a router and associate external network as router gateway
<pre>
neutron router-create router1
neutron router-gateway-set router1 external_network
</pre>
Create an internal network, a subnet and associate an interface to the router
<pre>
neutron net-create private_network
neutron subnet-create --name private_subnet private_network 10.0.1.0/24
neutron router-interface-add router1 private_subnet
</pre>
Boot 2 instances
<pre>
nova boot --flavor m1.tiny --image cirros --nic net-id=154da7a8-fa49-415e-9d35-c840b144a8df test1
nova boot --flavor m1.tiny --image cirros --nic net-id=154da7a8-fa49-415e-9d35-c840b144a8df test2
</pre>
Create 2 floating ips and associate it to instances
<pre>
neutron floatingip-create external_network
neutron floatingip-create external_network
nova floating-ip-associate test1 192.168.100.101
nova floating-ip-associate test2 192.168.100.102
</pre>
Test if all works as expected pinging floating ips
<pre>
# ping 192.168.100.101
# ping 192.168.100.102
</pre>
As you can see, in network nodes, a snat namespace is created
<pre>
# sudo ip netns
qdhcp-154da7a8-fa49-415e-9d35-c840b144a8df
snat-77fef58a-6d0c-4e96-b4b6-5d8e81ebead3
</pre>
In compute nodes, a fip namespace per instance with floating ip associated running on the compute node are created and a qrouter namespace are created.
<pre>
# sudo ip netns
fip-4dfdabb0-d2d6-4d4a-8c00-84df834eec8b
qrouter-77fef58a-6d0c-4e96-b4b6-5d8e81ebead3
</pre>

Best regards, Eduardo Gonzalez