# Create your tasks here
from __future__ import absolute_import, unicode_literals

import paramiko
from celery import shared_task

# from .models import BackupFirewall
# from .ssh_commands import open_ssh_session, show_full_config, save_config_to_file
# from netobjects import


@shared_task
def fortigate_backup(firewall_id):
    '''create backup file for any FortiGate unit'''
    # create the object of the concrete firewall
    firewall = BackupFirewall.objects.get(id=firewall_id).object_backup

    # next commands is a series of functions that suppose to make backup from start till the end.
    # open new session with usage of paramiko python library
    ssh = open_ssh_session(firewall.ipv4_external_address, firewall.dns_address, firewall.login, firewall.password)
    # after opening of the session, we need to input the command to collect data and save output
    stdin = ssh.exec_command(
        "execute backup config ftp /home/stast/projects/netmon/apps/backups/static/%s/%s/%s.conf" % (
            firewall.site_name.company_name, firewall.site_name, firewall
        )
    )
    stdout = show_full_config(open_ssh_session, "show full-configuration")[1]
    # finaly create new file and input in it output that we got from the command, we used before
    save_config_to_file(firewall.site_name.company_name, firewall.site_name, firewall, stdout)


def open_ssh_session(ip_address, dns_address, login, passw):
    '''initiate open session with  explicit netobject'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # https://github.com/onyxfish/relay/issues/11
    if ip_address:  # there must be empty or ip_address or dns_addres, so script need to choose only 1 of them
        ssh.connect(ip_address, username=login, password=passw)
    else:
        ssh.connect(dns_address, username=login, password=passw)
    return ssh


def show_full_config(ssh, command):
    ''' type the given command without quotes (stdin) and save output as variable (stdout)'''
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdin, stdout, stderr


def save_config_to_file(company_dir, site_dir, file_name, stdout):
    ''' save output data into file that will be used as backup '''
    file_dir = os.path.split(__file__)[0]
    with open(os.path.join(file_dir, company_dir, site_dir, file_name), 'w') as f:
        f.write(str(stdout.read()))
