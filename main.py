import time

from ppadb.client import Client as AdbClient


delay_between_takes = 3 # in seconds
total_amount_of_takes = 10
shutter_speed = 10 #in seconds


def connect():
    client = AdbClient(host="127.0.0.1", port=5037)

    devices = client.devices()

    if len(devices) == 0:
        print('No devices')
        quit()

    device = devices[0]

    print(f'Connected to {device}')

    return device, client

if __name__ == '__main__':
    device, client = connect()

    for i in range(total_amount_of_takes):
        device.shell('input keyevent 25')
        time.sleep(shutter_speed+delay_between_takes)
