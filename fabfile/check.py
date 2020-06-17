# -*- coding: utf-8 -*-
import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

#------------------------------------------------------------------
# fab -H x.x.x.x check.hostname
#------------------------------------------------------------------
@task
def hostname():
    '''check hostname # fab -H x.x.x.x check.hostname'''
    run("hostname")

#------------------------------------------------------------------
# fab -H x.x.x.x check.centos8
#------------------------------------------------------------------
@task
def centos8():
    '''check centos8 # fab -H x.x.x.x check.centos8'''
    run("hostname")
    run("cat /etc/redhat-release")
    run("cat /proc/cpuinfo |grep processor |wc -l")
    run("df -h")
    # Network
    run("ip a |grep inet")
    run("ip r")
    run("netstat -rn")
    run("chronyc sources")
    run("snmpwalk -v 2c -c xxxx localhost sysname")
    run("cat /etc/resolv.conf")
    # User
    sudo("cat /etc/passwd")
    sudo('cat /etc/sudoers |egrep -v "^#|^$" ')
    # Etc
    sudo('cat /etc/ssh/sshd_config |egrep -v "^#|^$" ')
    run("systemctl list-unit-files -t service |grep enabled")
    run("cat /etc/sysconfig/selinux |grep SELINUX=")



