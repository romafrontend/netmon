import subprocess
import os
import pexpect


def create_sub_folder(sub_folder, ftp_login, ftp_password, name_for_site_folder):
    '''create site_folder and subfolders'''
    path_to_backup_file = "/home/%s/%s/%s" % (ftp_login, name_for_site_folder, sub_folder)

    if not os.path.exists(path_to_backup_file):
        # first we need to enter as specific ftp user, because otherwise we can't create/edit user's folders
        site_command = pexpect.spawn("su %s -c 'mkdir ~/%s'" % (ftp_login, sub_folder))
        site_command.expect("Password: ")
        site_command.sendline(ftp_password)

        # if os.getlogin() == ftp_login:
        #     answer = os.getlogin()[:]
        #     # now we create the subfolders
        #     os.makedirs(path_to_backup_file)

        #     # give corp user permitions to own the whole site folder
        #     subprocess.run(
        #         ['chown', ftp_login, ':', ftp_login, '-R', "~"]
        #     )
        #     subprocess.run(['chmod', '-R', '744', path_to_site])

        #     return answer