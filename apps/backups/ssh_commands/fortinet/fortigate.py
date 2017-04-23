import paramiko
import os


def open_ssh_session(ip_address, dns_address, login, passw):
    '''initiate open session with  explicit netobject'''
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # solution, https://github.com/onyxfish/relay/issues/11
    if ip_address:  # there must be empty or ip_address or dns_addres, so script need to choose only 1 of them
        ssh.connect(ip_address, username=login, password=passw)
    else:
        ssh.connect(dns_address, username=login, password=passw)
    return ssh


def show_full_config(ssh, commands):
    ''' type the given command without quotes (stdin) and save output as variable (stdout)'''
    stdin, stdout, stderr = ssh.exec_command(commands['show_full_conf']['command'])
    return stdin, stdout, stderr


def save_config_to_file(company_dir, site_dir, file_name, stdout):
    ''' save output data into file that will be used as backup '''
    file_dir = os.path.split(__file__)[0]
    with open(os.path.join(file_dir, company_dir, site_dir, file_name), 'w') as f:
        f.write(str(stdout.read()))
