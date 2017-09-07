---
id: 1160
title: Ansible ini_file module, simplifying your DevOps life
date: 2016-02-24T20:00:37+00:00
author: Editor
layout: post
guid: http://egonzalez.org/?p=1160
permalink: /ansible-ini_file-module-simplifying-your-devops-life/
categories:
  - Linux
  - Various
tags:
  - --configure
  - ansible
  - config
  - file
  - idiot
  - ini
  - ini_file
  - openstack
  - style
---
If you don't read docs, one day you'll realize that your an idiot as i am|was.

A few days back, I've realized that i was using wrong all Ansible modules power since i started with it. What happened?

Most of the time i use Ansible is related to OpenStack configuration jobs. Almost, all OpenStack projects use INI formatted files for their configuration files.
When i started using Ansible, I searched on Google how to configure any kind of file with Ansible modules. Almost all blogs/forums that i saw, talked about lineinfile module. So i used these guidelines on my next few months, now i realize that i was using in the wrong way Ansible modules.

Ansible have a module called ini_file, you change values inside INI formatted files in a easy way , you don't need to use complicated regular expressions to change a value in a file.

Here you have ini_file module usage docs: <a href="http://docs.ansible.com/ansible/ini_file_module.html" target="_blank">http://docs.ansible.com/ansible/ini_file_module.html</a>

We are going to change Neutron user password in his dump config file, so we create a simple task on which we can see how ini_file module can be used.
<pre>
- hosts: localhost
  tasks:
  - name: Change neutron user password
    ini_file:
      dest: ~/neutron.conf
      section: keystone_authtoken
      option: password
      value: 12345
</pre>
Once the task has been applied, we can see how the values are applied in a proper ini style.
<pre>
cat neutron.conf
[keystone_authtoken]
password = 12345
</pre>
How many times you need to make a change in an INI formatted configuration file with Ansible and used lineinfile module?
If the answer is many times, it's OK, you are a dump like me.


Regards, Eduardo Gonzalez