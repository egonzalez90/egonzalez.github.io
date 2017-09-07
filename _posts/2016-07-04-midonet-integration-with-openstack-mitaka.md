---
id: 1257
title: MidoNet Integration with OpenStack Mitaka
date: 2016-07-04T21:48:34+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=1257
permalink: /midonet-integration-with-openstack-mitaka/
dsq_thread_id:
  - "6094297116"
image: /wp-content/uploads/2015/09/learn-about-openstack-badge.png
categories:
  - Linux
  - OpenStack
  - Various
tags:
  - cloud
  - config
  - install
  - integration
  - manual
  - midokura
  - midonet
  - mitaka
  - network
  - openstack
  - packages
  - packstack
  - rdo
  - sdn
---
MidoNet is an Open Source network virtualization software for IaaS infrastructure. 
It decouples your IaaS cloud from your network hardware, creating an intelligent software abstraction layer between your end hosts and your physical network.
This network abstraction layer allows the cloud operator to move what has traditionally been hardware-based network appliances into a software-based multi-tenant virtual domain.


This definition from MidoNet documentation explains what MidoNet is and what MidoNet does.

At this I will post cover my experiences integrating MidoNet with OpenStack.
I used the following configurations:

All servers have CentOS 7.2 installed
OpenStack has been previously installed from RDO packages with multinode Packstack

<ul><li>x3 NSDB nodes (Casandra and Zookeeper services)</li></ul>
<ul><li>x2 Gateway Nodes (Midolman Agent)</li></ul>
<ul><li>x1 OpenStack Controller (MidoNet Cluster)</li></ul>
<ul><li>x1 OpenStack compute node (Midolman Agent)</li></ul>

<br></br>

<strong>NSDB NODES</strong>

Disable SElinux
<pre>
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux
</pre>
Install OpenStack Mitaka release repository
<pre>
sudo yum install -y centos-release-openstack-mitaka
</pre>
Add Cassandra repository
<pre>
cat <&lt;EOF>/etc/yum.repos.d/datastax.repo
[datastax]
name = DataStax Repo for Apache Cassandra
baseurl = http://rpm.datastax.com/community
enabled = 1
gpgcheck = 1
gpgkey = https://rpm.datastax.com/rpm/repo_key
EOF
</pre>
Add Midonet repository
<pre>
cat <&lt;EOF>/etc/yum.repos.d/midonet.repo
[midonet]
name=MidoNet
baseurl=http://builds.midonet.org/midonet-5.2/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-openstack-integration]
name=MidoNet OpenStack Integration
baseurl=http://builds.midonet.org/openstack-mitaka/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-misc]
name=MidoNet 3rd Party Tools and Libraries
baseurl=http://builds.midonet.org/misc/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key
EOF
</pre>
Clean repo cache and update packages
<pre>
yum clean all
yum update
</pre>
<strong>Zookeeper Configuration</strong>
Install Zookeeper, java and dependencies
<pre>
yum install -y java-1.7.0-openjdk-headless zookeeper zkdump nmap-ncat
</pre>
Edit zookeeper configuration file
<pre>
vi /etc/zookeeper/zoo.cfg
</pre>
Add all NSDB nodes at the configuration file
<pre>
server.1=nsdb1:2888:3888
server.2=nsdb2:2888:3888
server.3=nsdb3:2888:3888
autopurge.snapRetainCount=10
autopurge.purgeInterval =12
</pre>
Create zookeeper folder on which zookeeper will store data, change the owner to zookeeper user
<pre>
mkdir /var/lib/zookeeper/data
chown zookeeper:zookeeper /var/lib/zookeeper/data
</pre>
Create myid file at zookeeper data folder, the ID should match with the NSDB node number, insert that number as follows:
<pre>
#NSDB1
echo 1 > /var/lib/zookeeper/data/myid
#NSDB2
echo 2 > /var/lib/zookeeper/data/myid
#NSDB3
echo 3 > /var/lib/zookeeper/data/myid
</pre>
Create java folder and create a softlink to it
<pre>
mkdir -p /usr/java/default/bin/
ln -s /usr/lib/jvm/jre-1.7.0-openjdk/bin/java /usr/java/default/bin/java
</pre>
Start and enable Zookeeper service
<pre>
systemctl enable zookeeper.service
systemctl start zookeeper.service
</pre>
Test if zookeeper is working locally
<pre>
echo ruok | nc 127.0.0.1 2181
imok
</pre>
Test if zookeeper is working at NSDB remote nodes
<pre>
echo stat | nc nsdb3 2181

Zookeeper version: 3.4.5--1, built on 02/08/2013 12:25 GMT
Clients:
 /192.168.100.172:35306[0](queued=0,recved=1,sent=0)

Latency min/avg/max: 0/0/0
Received: 1
Sent: 0
Connections: 1
Outstanding: 0
Zxid: 0x100000000
Mode: follower
Node count: 4
</pre>
<strong>Cassandra configuration</strong>
Install Java and Cassandra dependencies
<pre>
yum install -y java-1.8.0-openjdk-headless dsc22
</pre>
Edit cassandra yaml file
<pre>
vi /etc/cassandra/conf/cassandra.yaml
</pre>
Change cluster_name to midonet
Configure seed_provider seeds to match all NSDB nodes
Configure listen_address and rpc_address to match the hostname of the self node
<pre>
cluster_name: 'midonet'
....
seed_provider:
    - class_name: org.apache.cassandra.locator.SimpleSeedProvider
      parameters:
          - seeds: "nsdb1,nsdb2,nsdb3"

listen_address: nsdb1
rpc_address: nsdb1
</pre>
Edit cassandra's init script in order to fix a bug in the init script
<pre>
vi /etc/init.d/cassandra
</pre>
Add the next two lines after #Casandra startup 
<pre>
case "$1" in
    start)
        # Cassandra startup
        echo -n "Starting Cassandra: "
        mkdir -p /var/run/cassandra #Add this line
        chown cassandra:cassandra /var/run/cassandra #Add this line
        su $CASSANDRA_OWNR -c "$CASSANDRA_PROG -p $pid_file" > $log_file 2>&1
        retval=$?
        [ $retval -eq 0 ] && touch $lock_file
        echo "OK"
        ;;
</pre>
Start and enable Cassandra service
<pre>
systemctl enable cassandra.service
systemctl start cassandra.service
</pre>
Check if all NSDB nodes join the cluster
<pre>
nodetool --host 127.0.0.1 status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address          Load       Tokens       Owns (effective)  Host ID                               Rack
UN  192.168.100.172  89.1 KB    256          70.8%             3f1ecedd-8caf-4938-84ad-8614d2134557  rack1
UN  192.168.100.224  67.64 KB   256          60.7%             cb36c999-a6e1-4d98-a4dd-d4230b41df08  rack1
UN  192.168.100.195  25.78 KB   256          68.6%             4758bae8-9300-4e57-9a61-5b1107082964  rack1
</pre>
<strong>Configure OpenStack Controller Nodes (On which Neutron Server is running)</strong>

Disable SElinux
<pre>
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux
</pre>
Install OpenStack Mitaka release repository
<pre>
sudo yum install -y centos-release-openstack-mitaka
</pre>
Add Midonet Repository
<pre>
cat <&lt;EOF>/etc/yum.repos.d/midonet.repo
[midonet]
name=MidoNet
baseurl=http://builds.midonet.org/midonet-5.2/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-openstack-integration]
name=MidoNet OpenStack Integration
baseurl=http://builds.midonet.org/openstack-mitaka/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-misc]
name=MidoNet 3rd Party Tools and Libraries
baseurl=http://builds.midonet.org/misc/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key
EOF
</pre>
Clean repos cache and update the system
<pre>
yum clean all
yum update
</pre>
Create an OpenStack user for MidoNet, change the password to match your own
<pre>
# openstack user create --password temporal midonet
+----------+----------------------------------+
| Field    | Value                            |
+----------+----------------------------------+
| email    | None                             |
| enabled  | True                             |
| id       | ac25c5a77e7c4e4598ccadea89e09969 |
| name     | midonet                          |
| username | midonet                          |
+----------+----------------------------------+
</pre>
Add admin role at tenant services to Midonet user
<pre>
# openstack role add --project services --user midonet admin
+-----------+----------------------------------+
| Field     | Value                            |
+-----------+----------------------------------+
| domain_id | None                             |
| id        | bca2c6e1f3da42b0ba82aee401398a8a |
| name      | admin                            |
+-----------+----------------------------------+
</pre>
Create MidoNet service at Keystone
<pre>
# openstack service create --name midonet --description "MidoNet API Service" midonet
+-------------+----------------------------------+
| Field       | Value                            |
+-------------+----------------------------------+
| description | MidoNet API Service              |
| enabled     | True                             |
| id          | 499059c4a3a040cfb632411408a2be4c |
| name        | midonet                          |
| type        | midonet                          |
+-------------+----------------------------------+
</pre>
<strong>Clean up neutron server</strong>
Stop neutron services
<pre>
openstack-service stop neutron
</pre>
Remove neutron database and recreate it again
<pre>
mysql -u root -p
DROP DATABASE neutron;
Query OK, 157 rows affected (11.50 sec)

MariaDB [(none)]> CREATE DATABASE neutron;
Query OK, 1 row affected (0.00 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'localhost' IDENTIFIED BY 'ab4f81b1040a495e';
Query OK, 0 rows affected (0.00 sec)

MariaDB [(none)]> GRANT ALL PRIVILEGES ON neutron.* TO 'neutron'@'%' IDENTIFIED BY 'ab4f81b1040a495e';
Query OK, 0 rows affected (0.00 sec)
MariaDB [(none)]> exit
Bye
</pre>
Remove plugin.ini symbolic link to ml2_conf.ini
<pre>
#rm /etc/neutron/plugin.ini 
rm: remove symbolic link ‘/etc/neutron/plugin.ini’? y
</pre>
Remove br-tun tunnel used by neutron in all the nodes
<pre>
ovs-vsctl del-br br-tun
</pre>
Install MidoNet packages and remove ml2 package
<pre>
yum install -y openstack-neutron python-networking-midonet python-neutronclient
yum remove openstack-neutron-ml2
</pre>
Make a backup of neutron configuration file
<pre>
cp /etc/neutron/neutron.conf neutron.conf.bak
</pre>
Edit neutron configuration file
<pre>
vi /etc/neutron/neutron.conf
</pre>
Most of the options are already configured by our older neutron configuration, change the ones who apply to match this configuration
<pre>
[DEFAULT]
core_plugin = midonet.neutron.plugin_v2.MidonetPluginV2
service_plugins = midonet.neutron.services.l3.l3_midonet.MidonetL3ServicePlugin
dhcp_agent_notification = False
allow_overlapping_ips = True
rpc_backend = rabbit
auth_strategy = keystone
notify_nova_on_port_status_changes = true
notify_nova_on_port_data_changes = true
nova_url = http://controller:8774/v2

[database]
connection = mysql+pymysql://neutron:ab4f81b1040a495e@controller/neutron

[oslo_messaging_rabbit]
rabbit_host = controller
rabbit_userid = guest
rabbit_password = guest

[keystone_authtoken]
auth_uri = http://controller:5000/v2.0
admin_user=neutron
admin_tenant_name=services
identity_uri=http://controller:35357
admin_password=d88f0bd060d64c33

[nova]
region_name = RegionOne
auth_url = http://controller:35357
auth_type = password
password = 9ca36d15e4824d93
project_domain_id = default
project_name = services
tenant_name = services
user_domain_id = default
username = nova

[oslo_concurrency]
lock_path = /var/lib/neutron/tmp
</pre>
At my deployment these are the options I had to change to configure midonet
<pre>
diff /etc/neutron/neutron.conf neutron.conf.bak 
33c33
< core_plugin = midonet.neutron.plugin_v2.MidonetPluginV2
---
> core_plugin = neutron.plugins.ml2.plugin.Ml2Plugin
37c37
< service_plugins = midonet.neutron.services.l3.l3_midonet.MidonetL3ServicePlugin
---
> service_plugins =router
120c120
< dhcp_agent_notification = False
---
> #dhcp_agent_notification = true
1087c1087,1088
< lock_path = /var/lib/neutron/tmp
---
> lock_path = $state_path/lock
> 
</pre>
Create midonet plugins folder
<pre>
mkdir /etc/neutron/plugins/midonet
</pre>
Create a file called midonet.ini
<pre>
vi /etc/neutron/plugins/midonet/midonet.ini
</pre>
Configure midonet.ini file to match your own configuration options
<pre>
[MIDONET]
# MidoNet API URL
midonet_uri = http://controller:8181/midonet-api
# MidoNet administrative user in Keystone
username = midonet
password = temporal
# MidoNet administrative user's tenant
project_id = services
</pre>
Create a symbolic link from midonet.ini to plugin.ini
<pre>
ln -s /etc/neutron/plugins/midonet/midonet.ini /etc/neutron/plugin.ini
</pre>
Sync and populate database tables with Midonet plugin
<pre>
su -s /bin/sh -c "neutron-db-manage --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/midonet/midonet.ini upgrade head" neutron
su -s /bin/sh -c "neutron-db-manage --subproject networking-midonet upgrade head" neutron
</pre>
Restart nova api and neutron server services
<pre>
systemctl restart openstack-nova-api.service
systemctl restart neutron-server
</pre>
Install midonet cluster package
<pre>
yum install -y midonet-cluster
</pre>
Configure midonet.conf file
<pre>
vi /etc/midonet/midonet.conf
</pre>
Add all NSDB nodes at zookeeper_hosts
<pre>
[zookeeper]
zookeeper_hosts = nsdb1:2181,nsdb2:2181,nsdb3:2181
</pre>
Configure midonet to make use of NSDB nodes as Zookeeper and cassandra hosts
<pre>
cat << EOF | mn-conf set -t default
zookeeper {
    zookeeper_hosts = "nsdb1:2181,nsdb2:2181,nsdb3:2181"
}

cassandra {
    servers = "nsdb1,nsdb2,nsdb3"
}
EOF
</pre>
Set cassandra replication factor to 3
<pre>
echo "cassandra.replication_factor : 3" | mn-conf set -t default
</pre>
Grab your admin token
<pre>
#egrep ^admin_token /etc/keystone/keystone.conf 
admin_token = 7b84d89b32c34b71a697eb1a270807ab
</pre>
Configure Midonet to auth with keystone
<pre>
cat << EOF | mn-conf set -t default
cluster.auth {
    provider_class = "org.midonet.cluster.auth.keystone.KeystoneService"
    admin_role = "admin"
    keystone.tenant_name = "admin"
    keystone.admin_token = "7b84d89b32c34b71a697eb1a270807ab"
    keystone.host = controller
    keystone.port = 35357
}
EOF
</pre>
Start and enable midonet cluster service
<pre>
systemctl enable midonet-cluster.service
systemctl start midonet-cluster.service
</pre>
Install midonet CLI
<pre>
yum install -y python-midonetclient
</pre>
Create a file at you home directory with midonet auth info
<pre>
#vi ~/.midonetrc

[cli]
api_url = http://controller:8181/midonet-api
username = admin
password = temporal
project_id = admin
</pre>

<strong>Configure Compute nodes</strong>

Disable SElinux
<pre>
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux
</pre>
Install OpenStack Mitaka release repository
<pre>
sudo yum install -y centos-release-openstack-mitaka
</pre>
Add Midonet repository
<pre>
cat <&lt;EOF>/etc/yum.repos.d/midonet.repo
[midonet]
name=MidoNet
baseurl=http://builds.midonet.org/midonet-5.2/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-openstack-integration]
name=MidoNet OpenStack Integration
baseurl=http://builds.midonet.org/openstack-mitaka/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-misc]
name=MidoNet 3rd Party Tools and Libraries
baseurl=http://builds.midonet.org/misc/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key
EOF
</pre>
Clean repos cache and update the system
<pre>
yum clean all
yum update
</pre>
Edit qemu.conf
<pre>
vi /etc/libvirt/qemu.conf
</pre>
Configure with the following options, by default all these options are commented, you can paste it all wherever you want
<pre>
user = "root"
group = "root"

cgroup_device_acl = [
    "/dev/null", "/dev/full", "/dev/zero",
    "/dev/random", "/dev/urandom",
    "/dev/ptmx", "/dev/kvm", "/dev/kqemu",
    "/dev/rtc","/dev/hpet", "/dev/vfio/vfio",
    "/dev/net/tun"
]
</pre>
Restart libvirtd service
<pre>
systemctl restart libvirtd.service
</pre>
Install nova-network package
<pre>
yum install -y openstack-nova-network
</pre>
Disable Nova Network service and restart Nova compute service
<pre>
systemctl disable openstack-nova-network.service
systemctl restart openstack-nova-compute.service
</pre>
Install Midolman agent and java packages
<pre>
yum install -y java-1.8.0-openjdk-headless midolman
</pre>
Configure midolman.conf
<pre>
vi /etc/midolman/midolman.conf
</pre>
Add all nsdb nodes as zookeeper hosts
<pre>
[zookeeper]
zookeeper_hosts = nsdb1:2181,nsdb2:2181,nsdb3:2181
</pre>
Configure each compute node with an appropiate flavor located at /etc/midolman/ folder, the have different hardware resources configured, use the one that better match your compute host capabilities
<pre>
mn-conf template-set -h local -t agent-compute-medium
cp /etc/midolman/midolman-env.sh.compute.medium /etc/midolman/midolman-env.sh
</pre>
Configure metadata, issue the following commands only once, it will automatically populate the configuration to all midonet agents
<pre>
echo "agent.openstack.metadata.nova_metadata_url : \"http://controller:8775\"" | mn-conf set -t default
echo "agent.openstack.metadata.shared_secret : 2bfeb930a90d435d" | mn-conf set -t default
echo "agent.openstack.metadata.enabled : true" | mn-conf set -t default
</pre>
Allow metadata trafic at iptables
<pre>
iptables -I INPUT 1 -i metadata -j ACCEPT
</pre>
Remove br-tun bridge
<pre>
ovs-vsctl del-br br-tun
</pre>
Start and enable midolman agent service
<pre>
systemctl enable midolman.service
systemctl start midolman.service
</pre>
<strong>Gateway nodes configuration</strong>

Disable SElinux
<pre>
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=permissive/g' /etc/sysconfig/selinux
</pre>
Install OpenStack Mitaka release repository
<pre>
sudo yum install -y centos-release-openstack-mitaka
</pre>
Add Midonet repository
<pre>
cat <&lt;EOF>/etc/yum.repos.d/midonet.repo
[midonet]
name=MidoNet
baseurl=http://builds.midonet.org/midonet-5.2/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-openstack-integration]
name=MidoNet OpenStack Integration
baseurl=http://builds.midonet.org/openstack-mitaka/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key

[midonet-misc]
name=MidoNet 3rd Party Tools and Libraries
baseurl=http://builds.midonet.org/misc/stable/el7/
enabled=1
gpgcheck=1
gpgkey=https://builds.midonet.org/midorepo.key
EOF
</pre>
Clean repos cache and update the system
<pre>
yum clean all
yum update
</pre>
Install Midolman agent and java packages
<pre>
yum install -y java-1.8.0-openjdk-headless midolman
</pre>
Configure midolman.conf
<pre>
vi /etc/midolman/midolman.conf
</pre>
Add all nsdb nodes as zookeeper hosts
<pre>
[zookeeper]
zookeeper_hosts = nsdb1:2181,nsdb2:2181,nsdb3:2181
</pre>
Configure each gateway node with an appropiate flavor located at /etc/midolman/ folder, the have different hardware resources configured, use the one that better match your gateway host capabilities
<pre>
mn-conf template-set -h local -t agent-gateway-medium
cp /etc/midolman/midolman-env.sh.gateway.medium /etc/midolman/midolman-env.sh
</pre>
Grab the metadata shared secret located at nova.conf at any of your nova nodes
<pre>
# egrep ^metadata_proxy_shared_secret /etc/nova/nova.conf 
metadata_proxy_shared_secret =2bfeb930a90d435d
</pre>
Allow metadata trafic at iptables
<pre>
iptables -I INPUT 1 -i metadata -j ACCEPT
</pre>
Start and enable midolman agent service
<pre>
systemctl enable midolman.service
systemctl start midolman.service
</pre>
<strong>Configure encapsulation and register nodes</strong>
Enter to midonet CLI from a controller node
<pre>
midonet-cli
</pre>
Create the tunnel zone with VXLAN encapsulation
<pre>
midonet> tunnel-zone create name tz type vxlan
tzone0
midonet> list tunnel-zone
tzone tzone0 name tz type vxlan
</pre>
List hosts discovered by midonet, should be all the nodes where you configured midonet agents(midolman)
<pre>
midonet> list host
host host0 name gateway2 alive true addresses fe80:0:0:0:0:11ff:fe00:1102,169.254.123.1,fe80:0:0:0:0:11ff:fe00:1101,127.0.0.1,0:0:0:0:0:0:0:1,192.168.200.176,fe80:0:0:0:5054:ff:fef9:b2a0,169.254.169.254,fe80:0:0:0:7874:d6ff:fe5b:dea8,192.168.100.227,fe80:0:0:0:5054:ff:fed9:9cc0,fe80:0:0:0:5054:ff:fe4a:e39b,192.168.1.86 flooding-proxy-weight 1 container-weight 1 container-limit no-limit enforce-container-limit false
host host1 name gateway1 alive true addresses 169.254.169.254,fe80:0:0:0:3cd1:23ff:feac:a3c2,192.168.1.87,fe80:0:0:0:5054:ff:fea8:da91,127.0.0.1,0:0:0:0:0:0:0:1,fe80:0:0:0:5054:ff:feec:92c1,192.168.200.232,fe80:0:0:0:0:11ff:fe00:1102,169.254.123.1,fe80:0:0:0:0:11ff:fe00:1101,192.168.100.141,fe80:0:0:0:5054:ff:fe20:30fb flooding-proxy-weight 1 container-weight 1 container-limit no-limit enforce-container-limit false
host host2 name compute1 alive true addresses fe80:0:0:0:0:11ff:fe00:1101,169.254.123.1,127.0.0.1,0:0:0:0:0:0:0:1,fe80:0:0:0:0:11ff:fe00:1102,192.168.100.173,fe80:0:0:0:5054:ff:fe06:161,fe80:0:0:0:5054:ff:fee3:eb48,192.168.200.251,fe80:0:0:0:5054:ff:fe8d:d22,192.168.1.93,169.254.169.254,fe80:0:0:0:48cb:adff:fe69:f07b flooding-proxy-weight 1 container-weight 1 container-limit no-limit enforce-container-limit false
</pre>
Register each of the nodes at the VXLAN zone we created before
<pre>
midonet> tunnel-zone tzone0 add member host host0 address 192.168.100.227
zone tzone0 host host0 address 192.168.100.227
midonet> tunnel-zone tzone0 add member host host1 address 192.168.100.141
zone tzone0 host host1 address 192.168.100.141
midonet> tunnel-zone tzone0 add member host host2 address 192.168.100.173
zone tzone0 host host2 address 192.168.100.173
</pre>
<strong>Create Networks at Neutron</strong>
Create an external network
<pre>
# neutron net-create ext-net --router:external
Created a new network:
+-----------------------+--------------------------------------+
| Field                 | Value                                |
+-----------------------+--------------------------------------+
| admin_state_up        | True                                 |
| created_at            | 2016-07-03T14:47:30                  |
| description           |                                      |
| id                    | dc15245e-4391-4514-b489-8976373046a3 |
| is_default            | False                                |
| name                  | ext-net                              |
| port_security_enabled | True                                 |
| provider:network_type | midonet                              |
| router:external       | True                                 |
| shared                | False                                |
| status                | ACTIVE                               |
| subnets               |                                      |
| tags                  |                                      |
| tenant_id             | 2f7ee2716b3b4140be57b4a5b26401e3     |
| updated_at            | 2016-07-03T14:47:30                  |
+-----------------------+--------------------------------------+
</pre>
Create an external subnet in the network we created before, use you own IP ranges to match your environment
<pre>
# neutron subnet-create ext-net 192.168.200.0/24 --name ext-subnet \
  --allocation-pool start=192.168.200.225,end=192.168.200.240 \
  --disable-dhcp --gateway 192.168.200.1
Created a new subnet:
+-------------------+--------------------------------------------------------+
| Field             | Value                                                  |
+-------------------+--------------------------------------------------------+
| allocation_pools  | {"start": "192.168.200.225", "end": "192.168.200.240"} |
| cidr              | 192.168.200.0/24                                       |
| created_at        | 2016-07-03T14:50:46                                    |
| description       |                                                        |
| dns_nameservers   |                                                        |
| enable_dhcp       | False                                                  |
| gateway_ip        | 192.168.200.1                                          |
| host_routes       |                                                        |
| id                | 234dcc9a-2878-4799-b564-bf3a1bd52cad                   |
| ip_version        | 4                                                      |
| ipv6_address_mode |                                                        |
| ipv6_ra_mode      |                                                        |
| name              | ext-subnet                                             |
| network_id        | dc15245e-4391-4514-b489-8976373046a3                   |
| subnetpool_id     |                                                        |
| tenant_id         | 2f7ee2716b3b4140be57b4a5b26401e3                       |
| updated_at        | 2016-07-03T14:50:46                                    |
+-------------------+--------------------------------------------------------+
</pre>
Create a tenant network and a subnet on it
<pre>
# neutron net-create demo-net
Created a new network:
+-----------------------+--------------------------------------+
| Field                 | Value                                |
+-----------------------+--------------------------------------+
| admin_state_up        | True                                 |
| created_at            | 2016-07-03T14:51:39                  |
| description           |                                      |
| id                    | 075ba699-dc4c-4625-8e0d-0a258a9aeb7d |
| name                  | demo-net                             |
| port_security_enabled | True                                 |
| provider:network_type | midonet                              |
| router:external       | False                                |
| shared                | False                                |
| status                | ACTIVE                               |
| subnets               |                                      |
| tags                  |                                      |
| tenant_id             | 2f7ee2716b3b4140be57b4a5b26401e3     |
| updated_at            | 2016-07-03T14:51:39                  |
+-----------------------+--------------------------------------+
# neutron subnet-create demo-net 10.0.20.0/24 --name demo-subnet 
Created a new subnet:
+-------------------+----------------------------------------------+
| Field             | Value                                        |
+-------------------+----------------------------------------------+
| allocation_pools  | {"start": "10.0.20.2", "end": "10.0.20.254"} |
| cidr              | 10.0.20.0/24                                 |
| created_at        | 2016-07-03T14:52:32                          |
| description       |                                              |
| dns_nameservers   |                                              |
| enable_dhcp       | True                                         |
| gateway_ip        | 10.0.20.1                                    |
| host_routes       |                                              |
| id                | b299d899-33a3-4bfa-aff4-fda071545bdf         |
| ip_version        | 4                                            |
| ipv6_address_mode |                                              |
| ipv6_ra_mode      |                                              |
| name              | demo-subnet                                  |
| network_id        | 075ba699-dc4c-4625-8e0d-0a258a9aeb7d         |
| subnetpool_id     |                                              |
| tenant_id         | 2f7ee2716b3b4140be57b4a5b26401e3             |
| updated_at        | 2016-07-03T14:52:32                          |
+-------------------+----------------------------------------------+
</pre>
Create a tenant router
<pre>
# neutron router-create router1
Created a new router:
+-----------------------+--------------------------------------+
| Field                 | Value                                |
+-----------------------+--------------------------------------+
| admin_state_up        | True                                 |
| description           |                                      |
| external_gateway_info |                                      |
| id                    | 258942d8-9d82-4ebd-b829-c7bdfcc973f5 |
| name                  | router1                              |
| routes                |                                      |
| status                | ACTIVE                               |
| tenant_id             | 2f7ee2716b3b4140be57b4a5b26401e3     |
+-----------------------+--------------------------------------+
</pre>
Attach the tenant subnet interface we created before to the router
<pre>
# neutron router-interface-add router1 demo-subnet
Added interface 06c85a56-368c-4d79-bbf0-4bb077f163e5 to router router1.
</pre>
Set the external network as router gateway
<pre>
# neutron router-gateway-set router1 ext-net
Set gateway for router router1
</pre>
Now, you can create an instance at tenant network
<pre>
# nova boot --flavor m1.tiny --image 80871834-29dd-4100-b038-f5f83f126204 --nic net-id=075ba699-dc4c-4625-8e0d-0a258a9aeb7d test1
+--------------------------------------+-----------------------------------------------------+
| Property                             | Value                                               |
+--------------------------------------+-----------------------------------------------------+
| OS-DCF:diskConfig                    | MANUAL                                              |
| OS-EXT-AZ:availability_zone          |                                                     |
| OS-EXT-SRV-ATTR:host                 | -                                                   |
| OS-EXT-SRV-ATTR:hypervisor_hostname  | -                                                   |
| OS-EXT-SRV-ATTR:instance_name        | instance-0000000a                                   |
| OS-EXT-STS:power_state               | 0                                                   |
| OS-EXT-STS:task_state                | scheduling                                          |
| OS-EXT-STS:vm_state                  | building                                            |
| OS-SRV-USG:launched_at               | -                                                   |
| OS-SRV-USG:terminated_at             | -                                                   |
| accessIPv4                           |                                                     |
| accessIPv6                           |                                                     |
| adminPass                            | q2Cq4kxePSLL                                        |
| config_drive                         |                                                     |
| created                              | 2016-07-03T15:46:19Z                                |
| flavor                               | m1.tiny (1)                                         |
| hostId                               |                                                     |
| id                                   | b8aa46f9-186c-4594-8428-f8dbb16a5e16                |
| image                                | cirros image (80871834-29dd-4100-b038-f5f83f126204) |
| key_name                             | -                                                   |
| metadata                             | {}                                                  |
| name                                 | test1                                               |
| os-extended-volumes:volumes_attached | []                                                  |
| progress                             | 0                                                   |
| security_groups                      | default                                             |
| status                               | BUILD                                               |
| tenant_id                            | 2f7ee2716b3b4140be57b4a5b26401e3                    |
| updated                              | 2016-07-03T15:46:20Z                                |
| user_id                              | a2482a91a1f14750b372445d28b07c75                    |
+--------------------------------------+-----------------------------------------------------+
# nova list
+--------------------------------------+-------+--------+------------+-------------+---------------------+
| ID                                   | Name  | Status | Task State | Power State | Networks            |
+--------------------------------------+-------+--------+------------+-------------+---------------------+
| b8aa46f9-186c-4594-8428-f8dbb16a5e16 | test1 | ACTIVE | -          | Running     | demo-net=10.0.20.11 |
+--------------------------------------+-------+--------+------------+-------------+---------------------+
</pre>
Ensure the instance gets IP and the metadata service is properly running
<pre>
# nova console-log test1
...#Snipp from the output
Sending discover...
Sending select for 10.0.20.11...
Lease of 10.0.20.11 obtained, lease time 86400
cirros-ds 'net' up at 7.92
checking http://169.254.169.254/2009-04-04/instance-id
successful after 1/20 tries: up 8.22. iid=i-0000000a
...
</pre>
If you login to the instance through VNC you should be able to ping another instances

<strong>Edge router configuration</strong>
Create a new router
<pre>
# neutron router-create edge-router
Created a new router:
+-----------------------+--------------------------------------+
| Field                 | Value                                |
+-----------------------+--------------------------------------+
| admin_state_up        | True                                 |
| description           |                                      |
| external_gateway_info |                                      |
| id                    | 5ecadb64-cb0d-4f95-a00e-aa1dd20a2012 |
| name                  | edge-router                          |
| routes                |                                      |
| status                | ACTIVE                               |
| tenant_id             | 2f7ee2716b3b4140be57b4a5b26401e3     |
+-----------------------+--------------------------------------+
</pre>
Attach the external subnet interface to the router
<pre>
# neutron router-interface-add edge-router ext-subnet
Added interface e37f1986-c6b1-47f4-8268-02b837ceac17 to router edge-router.
</pre>
Create an uplink network
<pre>
# neutron net-create uplink-network --tenant_id admin --provider:network_type uplink
Created a new network:
+-----------------------+--------------------------------------+
| Field                 | Value                                |
+-----------------------+--------------------------------------+
| admin_state_up        | True                                 |
| created_at            | 2016-07-03T14:57:15                  |
| description           |                                      |
| id                    | 77173ed4-6106-4515-af1c-3683897955f9 |
| name                  | uplink-network                       |
| port_security_enabled | True                                 |
| provider:network_type | uplink                               |
| router:external       | False                                |
| shared                | False                                |
| status                | ACTIVE                               |
| subnets               |                                      |
| tags                  |                                      |
| tenant_id             | admin                                |
| updated_at            | 2016-07-03T14:57:15                  |
+-----------------------+--------------------------------------+
</pre>
Create a subnet in the uplink network
<pre>
# neutron subnet-create --tenant_id admin --disable-dhcp --name uplink-subnet uplink-network 192.168.1.0/24
Created a new subnet:
+-------------------+--------------------------------------------------+
| Field             | Value                                            |
+-------------------+--------------------------------------------------+
| allocation_pools  | {"start": "192.168.1.2", "end": "192.168.1.254"} |
| cidr              | 192.168.1.0/24                                   |
| created_at        | 2016-07-03T15:06:28                              |
| description       |                                                  |
| dns_nameservers   |                                                  |
| enable_dhcp       | False                                            |
| gateway_ip        | 192.168.1.1                                      |
| host_routes       |                                                  |
| id                | 4e98e789-20d3-45fd-a3b5-9bcf02d8a832             |
| ip_version        | 4                                                |
| ipv6_address_mode |                                                  |
| ipv6_ra_mode      |                                                  |
| name              | uplink-subnet                                    |
| network_id        | 77173ed4-6106-4515-af1c-3683897955f9             |
| subnetpool_id     |                                                  |
| tenant_id         | admin                                            |
| updated_at        | 2016-07-03T15:06:28                              |
+-------------------+--------------------------------------------------+
</pre>
Create a port for each of the gateway nodes, interface should match with the NIC you want to use for binding the gateway nodes and a IP address for the same purposes
<pre>
# neutron port-create uplink-network --binding:host_id gateway1 --binding:profile type=dict interface_name=eth1 --fixed-ip ip_address=192.168.1.199
Created a new port:
+-----------------------+--------------------------------------------------------------------------------------+
| Field                 | Value                                                                                |
+-----------------------+--------------------------------------------------------------------------------------+
| admin_state_up        | True                                                                                 |
| allowed_address_pairs |                                                                                      |
| binding:host_id       | compute1                                                                             |
| binding:profile       | {"interface_name": "eth1"}                                                           |
| binding:vif_details   | {"port_filter": true}                                                                |
| binding:vif_type      | midonet                                                                              |
| binding:vnic_type     | normal                                                                               |
| created_at            | 2016-07-03T15:10:06                                                                  |
| description           |                                                                                      |
| device_id             |                                                                                      |
| device_owner          |                                                                                      |
| extra_dhcp_opts       |                                                                                      |
| fixed_ips             | {"subnet_id": "4e98e789-20d3-45fd-a3b5-9bcf02d8a832", "ip_address": "192.168.1.199"} |
| id                    | 7b4f54dd-2b41-42ba-9c5c-cda4640dc550                                                 |
| mac_address           | fa:16:3e:44:a8:c9                                                                    |
| name                  |                                                                                      |
| network_id            | 77173ed4-6106-4515-af1c-3683897955f9                                                 |
| port_security_enabled | True                                                                                 |
| security_groups       | 0cf3e33e-dbd6-4b42-a0bd-6679b5eed4e1                                                 |
| status                | ACTIVE                                                                               |
| tenant_id             | 2f7ee2716b3b4140be57b4a5b26401e3                                                     |
| updated_at            | 2016-07-03T15:10:06                                                                  |
+-----------------------+--------------------------------------------------------------------------------------+
</pre>
Attach each of the ports to the edge router
<pre>
# neutron router-interface-add edge-router port=7b4f54dd-2b41-42ba-9c5c-cda4640dc550
Added interface 7b4f54dd-2b41-42ba-9c5c-cda4640dc550 to router edge-router.
</pre>
At this point you have to decide if use border routers with BGP enabled or static routes.
Use one of the following links to configure your use case:
<a href="https://docs.midonet.org/docs/latest/operations-guide/content/bgp_uplink_configuration.html" target="_blank">https://docs.midonet.org/docs/latest/operations-guide/content/bgp_uplink_configuration.html</a>
<a href="https://docs.midonet.org/docs/latest/operations-guide/content/static_setup.html" target="_blank">https://docs.midonet.org/docs/latest/operations-guide/content/static_setup.html</a>


<strong>Issues I faced during configuration of Midonet</strong>

Midolman agent don't start:
It was caused because midolman-env.sh file has more RAM configured as the one of my server.
Edit the file to match your server resources 
<pre>
# egrep ^MAX_HEAP_SIZE /etc/midolman/midolman-env.sh
MAX_HEAP_SIZE="2048M"
</pre>
<br></br>
Instances doesn't boot with the following error:
<pre>
could not open /dev/net/tun: Permission denied
</pre>
I had to remove br-tun bridges at ovs, if not, ovs locks the device and midolman cannot create the tunnel beetwen compute nodes and gateway nodes.
<pre>
ovs-vsctl del-br br-tun
</pre>
<br></br>
This post is my experience integrating Midonet into OpenStack, maybe some things are not correct, if you find any issue, please advise me to fix it.
Regards, Eduardo Gonzalez
