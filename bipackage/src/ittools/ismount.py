import json
import os
import time


# subcommand 1
def is_mounted(folder_path: str):
    return os.path.ismount(folder_path)


# subcommand 2
def mount_server(username: str, server_address: str, mount_folder: str, password: str, version=None):
    """Mount nas server."""
    if version:
        mount_command = f"sudo mount -t cifs //{server_address} {mount_folder} -o username={username},password={password},vers={version}"
    else:
        mount_command = (
            f"sudo mount -t cifs //{server_address} {mount_folder} -o username={username},password={password}"
        )

    os.system(mount_command)
    return


# subcommand 3
def check_reconnect(base_mnt: str, config_file: str):
    """Check reconnects."""
    with open(config_file, "r") as file:
        config_file = json.load(file)

    for keys in config_file:
        folder_path = os.path.join(base_mnt, keys)

        if not is_mounted(folder_path):
            print(f"Folder {folder_path} is not mounted. Reconnecting...")
            username = config_file.get(folder_path).get("username")
            server_address = config_file.get(folder_path).get("server_address")
            version = config_file.get(folder_path).get("version")
            password = config_file.get(folder_path).get("password")

            mount_server(username, server_address, folder_path, password, version)

            time.sleep(5)

            if is_mounted(folder_path):
                print(f"Successfully connected {server_address} to {folder_path}")
            else:
                print(f"Failed to connect to {server_address}")
        else:
            print(f"Folder {folder_path} is already mounted")

    return


def _test_main():
    config_file = ""
    base = ""
    check_reconnect(base, config_file)
    return


if __name__ == "__main__":
    _test_main()
