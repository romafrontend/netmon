import paramiko
import os


# initiate open session with firewall
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # solution, https://github.com/onyxfish/relay/issues/11
ssh.connect('197.220.220.66', username='admin', password='iosat%2276')

# type the command "show full-configuration" without quotes and save output as variable
stdin, stdout, stderr = ssh.exec_command("show full-configuration")
bakup_data = stdout.read()

file_dir = os.path.split(__file__)[0]
with open(os.path.join(file_dir, 'backup.conf'), 'w') as f:
    f.write(str(bakup_data))
