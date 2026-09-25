import platform
import os
import json
import socket
import getpass

def collect_os_parameters():
    os_name = platform.system()
    os_data = {
        "os_identification": {
            "system_name": os_name,
            "release_version": platform.release(),
            "detailed_version": platform.version(),
            "architecture": platform.architecture()[0]
        },
        "hardware_parameters": {
            "machine_type": platform.machine(),
            "processor_family": platform.processor(),
            "logical_cpu_cores": os.cpu_count()
        },
        "network_parameters": {
            "hostname": socket.gethostname()
        },
        "user_environment": {
            "current_user": getpass.getuser()
        },
        "python_environment": {
            "python_compiler": platform.python_compiler(),
            "python_version": platform.python_version()
        }
    }

    if os_name == 'Windows':
        os_data['os_identification']['windows_specific'] = platform.win32_ver()
    elif os_name == 'Darwin':
        os_data['os_identification']['mac_specific'] = platform.mac_ver()
    elif os_name == 'Linux':
        os_data['os_identification']['libc_version'] = platform.libc_ver()

    return os_data


def save_to_json(data, filename="os_info.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Параметры ({data['os_identification']['system_name']}) собраны и сохранены в '{filename}'")

system_parameters = collect_os_parameters()
save_to_json(system_parameters)