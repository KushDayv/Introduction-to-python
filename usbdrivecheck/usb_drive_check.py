import pyudev #installed using the command pip install pyudev on windows cmd
import subprocess

def is_device_authorized(device):
    # Check if the device is authorized to access the computer
    output = subprocess.check_output(['lsusb', '-v', '-d', device.get('ID_VENDOR_ID') + ':' + device.get('ID_MODEL_ID')]).decode()
    return 'authorized' in output

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem='usb')

for device in iter(monitor.poll, None):
    if device.action == 'add':
        print('USB device plugged in:', device)
        if is_device_authorized(device):
            print('Device is authorized to access the computer')
        else:
            print('Device is not authorized to access the computer')
    elif device.action == 'remove':
        print('USB device unplugged:', device)