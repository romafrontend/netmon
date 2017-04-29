# Create your tasks here
from __future__ import absolute_import, unicode_literals

from celery import shared_task
import paramiko

from .models import BackupFirewall


def open_ssh_session(self, ip_address, dns_address, login, passw):
    '''initiate open session with  explicit netobject'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # https://github.com/onyxfish/relay/issues/11
    if ip_address:  # there must be empty or ip_address or dns_addres, so script need to choose only 1 of them
        ssh.connect(ip_address, username=login, password=passw)
    else:
        ssh.connect(dns_address, username=login, password=passw)
    return ssh


@shared_task
def test_save_to_file(file_name):
    with open(file_name, 'w') as file:
        file.write('test message')


@shared_task
def fortigate_backup(firewall_id):
    '''create backup file for any FortiGate unit'''
    # create the object of the concrete firewall
    firewall = BackupFirewall.objects.get(id=firewall_id).object_backup

    # open new session with usage of paramiko python library
    ssh = open_ssh_session(firewall.ipv4_external_address, firewall.dns_address, firewall.login, firewall.password)
    # after opening of the session, we need to input(stdin) the command that will make firewall to open ftp session
    # with our server and save config file in specific folder.
    stdin, stdout, stderr = ssh.exec_command(
        "execute backup config ftp /home/stast/projects/netmon/apps/backups/static/%s/%s/%s.conf" % (
            firewall.site_name.company_name, firewall.site_name, firewall
        )
    )
