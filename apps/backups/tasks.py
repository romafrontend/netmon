from celery import shared_task


@shared_task
def device_backup(corp_folder, site_folder, device_folder, backup_id):
    '''initiate backup from network device via ftp server to backup folder'''
    from django.conf import settings
    from .models import CoreBackup
    from .common_scripts import open_ssh_session, create_backup_folder
    from datetime import datetime

    backup = CoreBackup.objects.get(id=backup_id)  # == backup
    netobject = backup.object_backup  # == object of the firewall

    path_to_backup_file = create_backup_folder(settings.STATIC_ROOT, corp_folder, site_folder, device_folder)

    ssh = open_ssh_session(netobject.ipv4_external_address, netobject.dns_address, netobject.login, netobject.password)

    if 'FortiGate' in str(netobject):
        file_name = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S') + '.conf'  # it's like 20170101_120101.conf
        # we send something like that:
        # execute backup full-config ftp /home/netmon/staticfiles/comp/site/backups/firewall/file.conf 1.1.1.1 user pas
        command = "execute backup full-config ftp %s/%s %s %s %s" % (
            path_to_backup_file, file_name, settings.SERVER_EXTERNAL_IP, settings.FTP_USER_LOGIN,
            settings.FTP_USER_PASSWORD
        )
        # after opening of the session, we need to input (stdin) the command that allow firewall to open ftp session
        # with our server and save config file to specific folder.
        stdin, stdout, stderr = ssh.exec_command(command)
        log = stdout.read()
        # close the ssh session after job had been done

        ssh.close()
        return (command, log)

    elif 'Cisco' in str(netobject):
        ssh = ssh.invoke_shell()  # Use invoke_shell to establish an 'interactive session'

        list_of_commands = [
            "config terminal" + '\n',
            "ip ftp username %s" % settings.FTP_USER_LOGIN + '\n',
            "ip ftp password %s" % settings.FTP_USER_PASSWORD + '\n',
            "end" + '\n',
            "copy running-config ftp" + '\n',
            settings.SERVER_EXTERNAL_IP + '\n',
            path_to_backup_file, "backup_cfg_for_router" + '\n'
        ]
        output = ''
        for command in list_of_commands:
            ssh.send(command)
            output += ssh.recv(1000)

        return (output)
