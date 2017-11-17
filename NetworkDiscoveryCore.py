import socket
import csv
import os


class NetworkDiscoveryCore:
    default_file_path = 'C:/Users/mmikec/Desktop/scripts/ALL_IP.csv'
    def __init__(self):
        if os.path.exists(self.default_file_path):  # Open file or create
            self.wr_file = open(self.default_file_path, 'r+', newline='')
        else:
            self.wr_file = open(self.default_file_path, 'w', newline='')

    def open_file(self, file_path):  # Open file for read/write when class define
        if os.path.exists(file_path):  # Open file or create
            wr_file = open(file_path, 'r+', newline='')
        else:
            wr_file = open(file_path, 'w', newline='')
        return wr_file

    def input_path(self):
        self.file_path = input('Input path: ')
        if os.path.exists(self.file_path):  # Open file or create
            print('File exist!')
        else:
            try:
                self.default_file_path = self.file_path
                print('Cnange default_file_path to :' + self.default_file_path)
                self.wr_file = open(self.default_file_path, 'w', newline='')
            except FileNotFoundError:
                print('Invalid input, Try again')

    def input_ip(self):  # Input ip range
        self.subnet = input('Input subnet: ') or '192.168.1.'
        print('Using default: ', self.subnet)
        try:
            self.start_ip = int(input('Input start_ip ip: '))
            self.stop_ip = int(input('Input stop_ip ip: '))
        except ValueError:
            self.start_ip = 1
            self.stop_ip = 25

    def close_file(self):  # Close file
        self.wr_file.close()

    def perform_net_discovery(self):  # Define network discovery
        self.input_ip()
        self.open_file(self.default_file_path)
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
        self.close_file()

    def write_csv_file(self, ip):  # Write ip in .csv
        self.open_file(self.default_file_path)
        writer = csv.writer(self.wr_file, delimiter=' ')
        format_ip = self.format_input(ip)
        writer.writerow(format_ip)
        print(format_ip)
        self.close_file()

    def format_input(self, input):
        input = str(input)
        format_inp = input.replace('[', '').replace(']', '').replace("'", ''). \
            replace('(', '').replace(')', '').replace(', ,', '-').replace(' ', '').replace('->', ' ')
        return format_inp

    def read_csv_file(self):  # Define read function
        iplist = []
        re_file = open(self.default_file_path, 'r')
        reader = csv.reader(re_file)
        for row in reader:
            iplist += row
        self.close_file()
        return(iplist)

    @staticmethod
    def print_localhost_ip():  # Print localhost ip and Hostname
        print('This Pc ip:')
        ip1 = socket.gethostbyname(socket.gethostname())
        hostname = socket.getfqdn()
        print(hostname, '', ip1)
