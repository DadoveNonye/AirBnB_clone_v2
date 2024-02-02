#!/usr/bin/python3
"""
A Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""

from fabric.api import put, run, env
from os.path import exists
env.hosts = ['18.206.197.202', '54.237.125.178']

def do_deploy(archive_path):
    """
    Deploy the archive to the web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive_name, archive_no_ext))
        run('rm /tmp/{}'.format(archive_name))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_no_ext))
         return True
    except:
        return False
