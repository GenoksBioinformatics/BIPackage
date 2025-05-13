from bipackage import check_gzip_validity, check_reconnect, is_mounted, md5sumchecker, mount_server




def _test_is_mounted():
    is_mounted(folder_path="")
    return


def _test_mount_server():
    mount_server(username="", server_address="", mount_folder="", password="")
    return


def _test_check_reconnect():
    check_reconnect(base_mnt="", config_file="")
    return


def _test_md5sumchecker():
    md5sumchecker(input_directory="", file_extension="", num_processes=2)
    return


def _test_check_gzip_validity():
    check_gzip_validity(file_path="")
    return
