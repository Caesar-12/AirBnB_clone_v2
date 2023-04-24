#!/usr/bin/python3

"""
Fabric scripts that creates and generates a .tgz archive
"""

from fabric.api import *
import os
from datetime import datetime

env.hosts = ["100.25.111.142", "3.86.18.48"]
# env.user = "ubuntu"


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
    # arch_dir = "versions/{}".format(arch_name)
    local("mkdir -p versions")

    # print("Packing web_static to {}".format(arch_dir))

    try:
        local("tar -cvzf {} web_static".format(arch_dir))
        size = os.stat(output).st_size
        # print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        arch_dir = None

    return arch_dir


def do_deploy(archive_path):
    """
        Distributes archive to servers
    """

    if os.path.isfile(archive_path) is False:
        return False

    date = datetime.now()
    path_name = "/data/web_static/releases/web_static_{}{}{}{}{}{}".format(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second
            )

    # arch_file = archive_path[9:]
    try:
        put(archive_path, "/tmp/")
        if not os.path.isdir(path_name):
            run("sudo mkdir -p {}".format(path_name))
        arch_file = "/tmp/{}".format(archive_path[9:])
        run("sudo tar -xzf {} -C {}".format(arch_file, path_name))
        run("sudo rm {}".format(arch_file))
        run("sudo mv {}/web_static/* {}".format(path_name, path_name))
        run("sudo rm -rf {}/web_static".format(path_name))
        sym_path = "/data/web_static/current"
        run("rm -rf {}".format(sym_path))
        run("ln -s {} {}".format(path_name, sym_path))
        print("New version deployed!")
    except Exception:
        return False
    return True


def deploy():
    """
    Creates and distributes archives to servers
    """
    do_deploy = __import__('2-do_deploy_web_static').do_deploy
    do_pack = __import__('1-pack_web_static').do_pack

    arch_path = do_pack()

    if not arch_path:
        return False

    result = do_deploy(arch_path)

    return result
