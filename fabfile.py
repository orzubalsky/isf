from fabric.api import env, task, sudo, prompt, cd

env.hosts = ['184.172.15.233', ]

#####
#
# tasks that will need to be done repeatedly.
#
#####


@task
def update_sourcecode():
    with cd('/home/pnguye/webapps/portfolio_production/website'):
        sudo('git pull', user='')

@task
def update_project_settings():
    filename = prompt( 'Enter name of local settings file:',
                       default='website/settings/server.py' )
    destination = '/home/pnguye/webapps/portfolio_production/website/settings/server.py'
    put(filename,destination,use_sudo=True)
    sudo('chown pnguye:webdev %s' % destination)

@task
def run_buildout():
    with cd('/home/pnguye/webapps/portfolio_production/website/'):
        sudo('./bin/buildout -c server.cfg',user='pnguye')

@task
def update_db():
    with cd('/home/pnguye/webapps/portfolio_production/website/'):
        sudo('./bin/django syncdb',user='pnguye')
        sudo('./bin/django migrate',user='pnguye')
    
@task
def update_static_files():
    # run the django command to update static files
    # then push them all to rackspace
    pass

@task
def restart_wsgi():
    with cd('/opt/projects/ts'):
        sudo('touch bin/django.wsgi')

@task
def deploy():
    update_sourcecode()

    update = prompt( 'Do you want to update the server settings file with a local file? (y/n)',
                     default='y', validate=r'^[yYnN]$' )
    if update.upper() == 'Y':
        update_project_settings()

    update = prompt( 'Do you want to re-run the buildout? (y/n)',
                     default='y', validate=r'^[yYnN]$' )
    if update.upper() == 'Y':
        run_buildout()

    update_db()
    update_static_files()
    restart_wsgi()
