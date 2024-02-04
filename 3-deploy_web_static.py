#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an archive to my web servers,
using the function deploy
"""

from fabric.api import run, env
from os import path
from 2-do_deploy_web_static import do_deploy, do_pack
env.hosts = ['18.206.197.202', '54.237.125.178']


def deploy():
    """
    Create and distribute an archive to web servers
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    deploy_result = do_deploy(archive_path)

    return deploy_result

if __name__ == "__main__":
    deploy()
