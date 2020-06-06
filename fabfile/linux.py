# -*- coding: utf-8 -*-
import sys, os
from fabric.api import *
from fabric.contrib import files
from datetime import datetime

FABDIR=os.getcwd()

#------------------------------------------------------------------
# fab -H x.x.x.x linux.hostname
#------------------------------------------------------------------
@task
def hostname():
    '''check hostname'''
    run("hostname")

#------------------------------------------------------------------
# fab -H x.x.x.x linux.put_test
#------------------------------------------------------------------
@task
def put_test():
    put("scripts/fabtest.sh" , "/tmp/fabtest.sh", mode=755)
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


