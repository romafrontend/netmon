import paramiko
import os

from apps.netobjects.ssh_commands import fortigate


def open_ssh_session(ip_or_dns_address, login, passw):
    '''initiate open session with  explicit netobject'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # solution, https://github.com/onyxfish/relay/issues/11
    ssh.connect(ip_or_dns_address, username=login, password=passw)
    return ssh


def show_full_config(command):
    ''' type the given command without quotes (stdin) and save output as variable (stdout)'''
    stdin, stdout, stderr = ssh.exec_command(command)
    return stdin, stdout, stderr


def save_config_to_file(company_dir, site_dir, file_name):
    ''' save output data into file that will be used as backup '''
    file_dir = os.path.split(__file__)[0]
    with open(os.path.join(file_dir, company_dir, site_dir, file_name), 'w') as f:
        f.write(str(show_full_config()[1].read()))  # show_full_config()[1] is stdout that we defined earlier
