from celery import shared_task


@shared_task
def create_site_folder_and_subfolders(corp_folder, site_folder, *subfolders):
    '''we already have the corp user/folder in linux server, now we need to create site folder
    for each site and also all subfolders like 'backups', 'documents' and etc '''
    import os
    from django.conf import settings

    path_to_site_folder = "/%s/customers/%s/%s" % (settings.STATIC_ROOT, corp_folder, site_folder)

    if not os.path.exists(path_to_site_folder):
        for sub_dir in subfolders:
            path_to_subdir = path_to_site_folder + "/" + sub_dir
            os.makedirs(path_to_subdir)  # create subfolder and all folders in it's path
