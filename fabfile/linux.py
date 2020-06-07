# -*- coding: utf-8 -*-
import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

FABDIR=os.getcwd()

#------------------------------------------------------------------
# fab -H x.x.x.x linux.test
#------------------------------------------------------------------
@task
def test():
    '''test'''
    local("pwd")
    run("hostname")
    sudo("cat /etc/sudoers")


#------------------------------------------------------------------
# fab -H x.x.x.x linux.put_test
#------------------------------------------------------------------
@task
def put_test():
    put("scripts/fabtest.sh" , "/tmp/fabtest.sh")
    run("chmod 755 /tmp/fabtest.sh")
    run("ls -l /tmp")
    run("/tmp/fabtest.sh > /tmp/fabtest.txt")
    run("cat /tmp/fabtest.txt")
    run("rm -f /tmp/fabtest.txt")

#------------------------------------------------------------------
# fab -H x.x.x.x linux.get_test
#------------------------------------------------------------------
@task
def get_test():
    run("hostname > /tmp/fabtest.txt")
    get("/tmp/fabtest.txt", "tmp/fabtest.txt")
    local("cat  tmp/fabtest.txt")
    local("rm -f tmp/fabtest.txt")

#------------------------------------------------------------------
# fab -H x.x.x.x linux.vi_test
#------------------------------------------------------------------
@task
def vi_test():
    open_shell("vi ~/test.txt && exit")


