import paramiko
import os


def open_ssh_session(ip_address, dns_address, login, passw):
    '''initiate open session with  explicit netobject'''
    ssh = paramiko.SSHClient()
    # https://github.com/onyxfish/relay/issues/11
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if ip_address:  # there must be empty or ip_address or dns_addres, so script need to choose only 1 of them
        ssh.connect(ip_address, username=login, password=passw)
    else:
        ssh.connect(dns_address, username=login, password=passw)
    return ssh


def create_backup_folder(STATIC_ROOT, corp_folder, site_folder, device_folder):
    '''create folder for future save location of the file'''
    path_to_backup_file = "%s/customers/%s/%s/backups/%s" % (STATIC_ROOT, corp_folder,
                                                             site_folder, device_folder)
    if not os.path.exists(path_to_backup_file):
        os.makedirs(path_to_backup_file)
    return path_to_backup_file


# def save_config_to_file(path_to_backup_file, file_name, stdout):
#     ''' save output data into file that will be used as backup '''

#     with open(os.path.join(path_to_backup_file, str(file_name)), 'w') as f:
#         f.write(str(stdout.read()))

