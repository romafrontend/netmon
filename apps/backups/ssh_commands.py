import paramiko
import os


def open_ssh_session(ip_address, dns_address, login, passw):
    '''initiate open session with  explicit netobject'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # https://github.com/onyxfish/relay/issues/11
    if ip_address:  # there must be empty or ip_address or dns_addres, so script need to choose only 1 of them
        ssh.connect(ip_address, username=login, password=passw)
    else:
        ssh.connect(dns_address, username=login, password=passw)
    return ssh


def create_new_folder_for_backups(company_dir, site_dir, model_family, model_version):
    #  for example path_to_backup_file = '/home/corpname/SiteName/backups/family_version'
    path_to_backup_file = "/".join(
        "/home", str(company_dir).lower(), site_dir, "backups", model_family) + "_" + model_version

    # check that we have specific folders that had been created in path_to_backup_file
    if not os.path.exists(path_to_backup_file):
        os.makedirs(path_to_backup_file)

    return path_to_backup_file


# def save_config_to_file(company_dir, site_dir, file_name, stdout):
#     ''' save output data into file that will be used as backup '''

#     with open(os.path.join(path_to_backup_file, str(file_name)), 'w') as f:
#         f.write(str(stdout.read()))
