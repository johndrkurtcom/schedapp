from __future__ import with_statement
from fabric.api import local, settings, abort, run, cd, env
from fabric.operations import reboot
from fabric.contrib.console import confirm

env.hosts = ['sched.drkurt.com']

env.user = 'ec2-user'

def prepare_deploy():
	local("gunicorn manage:app")
	
def updateApp():
	local("git add . && git commit -m 'auto update'")
	local("git push web master")

def deploy():
	code_dir = '/home/ec2-user/m3aawgApp.git/app'
	updateApp()
	with cd(code_dir):

		run("source venv/bin/activate")
		run("pkill gunicorn")
		run("sudo pip install -r requirements.txt")
		run("gunicorn manage:app")
