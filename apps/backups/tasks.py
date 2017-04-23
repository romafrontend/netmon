# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task

from ssh_commands.fortinet import fortigate
from .models import BackupFirewall
from netobjects.ssh_commands import fortinet  # list of commands


@shared_task
def fortigate_backup(firewall_id):
    firewall = BackupFirewall.objects.get(id=firewall_id).object_backup

    open_ssh_session = fortigate.open_ssh_session(
        firewall.ipv4_external_address, firewall.dns_address, firewall.login, firewall.password
    )
    show_full_config = fortigate.show_full_config(open_ssh_session, fortinet.commands)
    fortigate.save_config_to_file(firewall.site_name.company_name, firewall.site_name, firewall, show_full_config)
