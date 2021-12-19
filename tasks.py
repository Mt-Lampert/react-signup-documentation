from invoke import task
import shutil

@task
def hugo(c):
    """ re-build the website from scratch """
    shutil.rmtree('public')
    c.run("hugo")