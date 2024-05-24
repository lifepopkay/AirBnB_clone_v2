#!/usr/bin/env python3
#compress a file before sending
from fabric.api import run, local
from datetime import datetime


def do_pack():
 """Generates a .tgz archive from the contents of the web_static folder.

  Returns:
      str: The path to the generated archive if successful, None otherwise.
  """
  current = datetime.utcnow()
  file_name = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"

  #check if versions exist
  run("mkdir -p versions", shell=True)

  file_tar = local("tar -cvzf versions/{} web_static".format(file_name))

  if file_tar is not None:
      return file_name
  else:
      return None

