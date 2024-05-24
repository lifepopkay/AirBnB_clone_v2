#!/usr/bin/python3
# This script distributes an archive to my web servers
from fabric.api import env, put, run
import os
env.hosts = ['35.153.51.52', '34.229.189.140']


def do_deploy(archive_path):

    """Distributes an archive to a web server.
    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or
        an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False

    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]

         path = "/data/web_static/releases/"
         sym_path = "/data/web_static/current"
         put(archive_path, '/tmp/')

         # Uncompress the archive to the folder
         run('mkdir -p {}/{}/'.format(path, name))
         run('tar -zxf /tmp/{} -C {}/{}'.format(file_name, path, name))
         
         # Delete the archive from the web server
         run('rm /tmp/{}'.format(file_name))

         # Delete the symbolic link /data/web_static/current
         # from the web server
         run('rm {}'.format(sym_path))

         # Create a new the symbolic link
         run('ln -s {}/{}/ {}'.format(path, name, sym_path))
         
         return True
    except Exception as e:
        return False
