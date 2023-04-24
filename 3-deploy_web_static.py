#!/usr/bin/python3
"""
Contains deploy function for deployment
"""


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
