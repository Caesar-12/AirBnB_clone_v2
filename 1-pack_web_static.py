#!/usr/bin/python3

"""
Fabric scripts that generates a .tgz archive
"""

from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """
    function to create arhive
    """

    date = datetime.now()
    arch_dir = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date.year,
        date.month,
        date.day,
        date.hour,
        date.minute,
        date.second
        )
    #arch_dir = "versions/{}".format(arch_name)
    if not os.path.isdir("versions"):
        os.mkdirs("versions")

    print("Packing web_static to {}".format(arch_dir))

    try:
        local("tar -cvzf {} web_static".format(arch_dir))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        arch_dir = None

    return arch_dir
