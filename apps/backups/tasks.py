# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

# import ssh_commands
# from .models import BackupFirewall
# from netobjects.ssh_commands import fortinet  # list of commands


@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def fortigate_backup(firewall_id):
    firewall = BackupFirewall.objects.get(id=firewall_id).object_backup

    # next commands is a series of functions that suppose to make backup from start till the end.
    # open new session with usage of paramiko python library
    open_ssh_session = fortigate.open_ssh_session(
        firewall.ipv4_external_address, firewall.dns_address, firewall.login, firewall.password
    )
    # after opening of the session, we need to input the command to collect data
    show_full_config = fortigate.show_full_config(open_ssh_session, fortinet.commands)
    # finaly create new file and input in it output that we got from the command, we used before
    fortigate.save_config_to_file(firewall.site_name.company_name, firewall.site_name, firewall, show_full_config)
