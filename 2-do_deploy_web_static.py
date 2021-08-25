#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents
    of the web_static folder and deploys an archive to your web
    servers
"""
from fabric.api import run, put, env
from datetime import datetime
from os.path import isfile, basename
env.host = ['34.138.28.3', '34.138.208.167']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not isfile(archive_path):
        return False
    filename = basename(archive_path)
    try:
        no_ext = filename.split(".")[0]
        put(archive_path, "/tmp/")
        extract_path = "/data/web_static/releases/{}".format(no_ext)
        run("mkdir -p {}".format(extract_path))
        run("tar xzf /tmp/{} -C {}".format(filename, extract_path))
        run("rm /tmp/{}".format(filename))
        run("mv {0}/web_static/* {0}/".format(extract_path))
        run("rm -rf {0}/web_static/")
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(extract_path))
        return True
    except:
        return False
