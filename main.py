#!/usr/local/bin/python3.9
# Menu Driven Host File Editor

import shutil
import os

print("\n   ***Host File Editor will create a custom device list for Network Tools***\n")
menu_prompt = ("\n    1. List hosts\n"  
               "    2. List IP Addresses\n"
               "    3. Add a Host\n"
               "    4. Delete a Host\n"
               "    Q. Exit to Command Shell\n\n"
               "    >>>  ")

class Host:  # Host File Class
    def __init__(self, ipaddress, hostname):
        self.hostname = hostname
        self.ipaddress = ipaddress

    @staticmethod
    def add_host():
        print(' Adding to host file')
        print('  {}     {}\n'.format(ipaddress, hostname))
        with open('hosts.txt', 'a+') as f:
            f.write('{}     {}\n'.format(ipaddress, hostname))


while True:  # keep asking for input until break
    command = input(menu_prompt).lower().strip()
    if command == '1':
        print('\n Listing hosts:\n')
        host_dict = {}
        with open('hosts.txt', 'r') as file:
            for line in file:
                (val, key) = line.split()
                host_dict[key] = val

        for key in sorted(host_dict):
            print('  {}'.format(key, val))
        print("\n")

    elif command == '2':
        print('\n List IP Addresses:\n')
        ipaddr_dict = {}
        with open('hosts.txt', 'r') as file:
            for line in file:
                (val, key) = line.split()
                ipaddr_dict[key] = val
                print('  {}    {}'.format(val, key))
        print("\n")

    elif command == '3':
        print('\n Add Host Entry')
        while True:
            sub_command = input(" Press Enter to continue or 'Q' to quit: ").lower().strip()
            if sub_command != 'q':
                hostname = input(' Enter hostname: ').lower().strip()
                try:
                    if hostname == '':  # check for blank entry
                        raise NameError(' Hostname Cannot be Blank')
                    ipaddress = input(' Enter the IP Address: ').strip()
                    if ipaddress == '':  # check for blank entry
                        raise NameError(' IP Address Cannot be Blank')
                    host_address = Host(ipaddress, hostname)
                    host_address.add_host()  # call method in class
                except NameError as excpt:  # catch the exception
                    print(excpt)
            else:
                break

    elif command == '4':
        print('\n Delete a Host')
        shutil.copy('hosts.txt', 'hosts.bak')
        while True:
            sub_command = input(" Press Enter to continue or 'Q' to quit: ").lower().strip()
            if sub_command != 'q':
                delhost = input(' Enter hostname to delete: ').lower().strip()
                try:
                    if delhost == '':
                        raise NameError(' Hostname Cannot be Blank')
                    with open('hosts.txt', 'r') as file_read:
                        lines = file_read.readlines()

                        with open('hosts_temp.txt', 'w') as file_write:
                            for line in lines:
                                if delhost not in line:
                                    file_write.write(line)
                    print(' Hostname', delhost, 'will be Removed')
                    try:
                        os.remove('hosts.txt')
                    except OSError:
                        pass
                    os.rename("hosts_temp.txt", "hosts.txt")
                    # print(os.listdir())
                except NameError as delexcept:
                    print(delexcept)
            else:
                break
            shutil.copy('hosts.txt', 'custom_devices.txt')
    elif command == 'q':
        # This last portion takes the output and writes a file for another purpose...      
        with open('hosts.txt', 'r') as f:
            hlines = [line.split(maxsplit=1)[0] for line in f if line.strip()]
            print('\n\n Adding List \n\n', hlines)
            file = open("custom_devices.txt", "w")
            for i in hlines:
                file.writelines(i + '\n')
            file.close()
        break  # Exit to shell
    else:
        print(' Unrecognized Entry.')

print('\n\n  ***custom_devices.txt Updated*** \n\n')
