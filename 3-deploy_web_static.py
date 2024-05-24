#!/usr/bin/python3
# creates and distributes an archive to your web servers

from fabric.api import *
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
env.hosts = ['35.153.51.52', '34.229.189.140']

def deploy():
    
    # Call the do_pack() function 
    # and store the path of the created archive
    file_created = do_pack()
    if file_created is None:
        return False
    else:
       new_arh = do_deploy(file_created)
       return new_arh
