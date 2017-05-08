from celery import shared_task


@shared_task
def fortigate_backup(backup_id):
    '''initiate backup from firewall to the ftp server to backup folder'''
    from .models import CoreBackup
    from .ssh_commands import open_ssh_session, create_new_folder_for_backups

    backup = CoreBackup.objects.get(id=backup_id)  # create value == backup
    firewall = backup.object_backup  # create value == object of the firewall

    # open new session with usage of paramiko python library
    ssh = open_ssh_session(firewall.ipv4_external_address, firewall.dns_address, firewall.login, firewall.password)

    # create/check folder for future save location of the file
    path_to_backup_file = create_new_folder_for_backups(
        firewall.site_name.company_name, firewall.site_name.name, firewall.model_family, firewall.model_version
    )

    # we send something like that:
    # "execute backup full-config ftp /home/company/site/backups/firewall/file.conf 1.1.1.1 company iosatcompany"
    command = "execute backup full-config ftp %s %s %s %s" % (
        path_to_backup_file,
        backup.ftp_server_address,  # FTP server address and port
        firewall.site_name.company_name.lower(),
        'iosat' + firewall.site_name.company_name.lower()
    )

    # after opening of the session, we need to input (stdin) the command that allow firewall to open ftp session
    # with our server and save config file to specific folder.
    stdin, stdout, stderr = ssh.exec_command(command)

    log = stdout.read()[:]  # thanks to 'log' later we can see the status of the task in backup object

    # close the ssh session after job had been done
    ssh.close()
    return (command, log)
