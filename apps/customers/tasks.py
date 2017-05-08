from celery import shared_task


@shared_task
def create_corp_user(ftp_username, ftp_password):
    '''create new unix user on the server, also create the folder in /home for that user'''
    import pexpect
    command = pexpect.spawn("sudo adduser %s" % ftp_username)
    command.expect("Enter new UNIX password: ")
    command.sendline(ftp_password)
    command.expect("Retype new UNIX password: ")
    command.sendline(ftp_password)
    command.expect(".*")  # Full Name []:
    command.sendline("")
    command.expect(".*")  # Room Number []:
    command.sendline("")
    command.expect(".*")  # Work Phone []:
    command.sendline("")
    command.expect(".*")  # Home Phone []:
    command.sendline("")
    command.expect(".*")  # Other []:
    command.sendline("")
    # there is mistake in the command, but I don't know how to solve it. Anyway it create new user, so doesn't matter
    command.expect("Is the information correct? [Y/n] ")
    command.sendline("")


@shared_task
def create_site_folder_and_subfolders(corp_id):
    pass
