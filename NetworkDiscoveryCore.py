import socket
import csv
import os

class NetworkDiscoveryCore:

    def __init__(self):  # Open file for read/write when class define
        self.file_path = '/home/mile/Documents/ALL_IP.csv'
        if os.path.exists(self.file_path):  # Open file or create
            self.wr_file = open(self.file_path, 'r+', newline='')
        else:
            self.wr_file = open(self.file_path, 'w', newline='')

    def input_path(self):
         self.file_path = input('Input path: ')
         if os.path.exists(self.file_path):  # Open file or create
            print('File exist!')
         else:
            try:
                self.wr_file = open(self.file_path, 'w', newline='')
            except FileNotFoundError:
                print('Invalid input, Try again')

    def input_ip(self):  # Input IP range
        self.subnet = input('Input subnet: ') or '192.168.1.'
        print('Using default: ', self.subnet)
        try:
            self.start_ip = int(input('Input start_ip ip: '))
            self.stop_ip = int(input('Input stop_ip ip: '))
        except ValueError:
            self.start_ip = 1
            self.stop_ip = 256

    def close_file(self):  # Close file
        self.wr_file.close()

    def perform_net_discovery(self):  # Define network discovery
        self.input_ip()
        print(self.start_ip, self.stop_ip)
        for i in range(self.start_ip, self.stop_ip):
            ip = self.subnet + str(i)
            try:
                ip1 = socket.gethostbyaddr(ip)
                self.write_csv_file(ip1)
            except socket.herror:
                pass
            except socket.gaierror:
                print('Invalid input')
                break

    def write_csv_file(self, IP):  # Write ip in .csv
        writer = csv.writer(self.wr_file, delimiter=' ')
        ip = str(IP)
        format_ip = ip.replace('[', '').replace(']', '').replace("'", ''). \
            replace(' ', '').replace('(', '').replace(')', '').replace(',,', '->')
        writer.writerow(format_ip)
        print(format_ip)

    def read_csv_file(self):  # Define read function
        re_file = open(self.file_path, 'r')
        reader = csv.reader(re_file)
        for row in reader:
            print(row)

    def print_localhost_ip(self):  # Print localhost ip and Hostname
        print('This Pc IP:')
        ip1 = socket.gethostbyname(socket.gethostname())
        hostname = socket.getfqdn()
        print(hostname, '', ip1)
