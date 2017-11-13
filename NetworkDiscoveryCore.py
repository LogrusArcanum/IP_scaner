import socket
import csv
import os

class NetworkDiscoveryCore:
    def __init__(self):             #### Open file for read/write when class define
        self.file_path = '/home/mile/Documents/ALL_IP.csv'
        if os.path.exists(self.file_path):                           # Open file or create
            self.wr_file = open(self.file_path, 'r+', newline='')
        else:
            self.wr_file = open(self.file_path, 'w', newline='')

    def input_path(self):
         self.file_path = input('Input path: ')
         if os.path.exists(self.file_path):                           # Open file or create
            print('File exist!')
         else:
            try:
                self.wr_file = open(self.file_path, 'w', newline='')
            except FileNotFoundError:
                print('Invalid input, Try again')

    def input_ip(self):             #### Input IP range
        self.subnet = input('Input subnet: ') or '192.168.1.'
        print('Using default: ', self.subnet)
        try:
            self.start = int(input('Input start ip: '))
            self.stop = int(input('Input stop ip: '))
        except ValueError:
            self.start = 1
            self.stop = 256

    def close_file(self):           #### Close file
        self.wr_file.close()
    #################################### NET_DISC ###############################
    def perform_net_discovery(self):  # Defibe network discovery
        self.input_ip()
        print(self.start, self.stop)
        for i in range(self.start, self.stop):
            ip = self.subnet + str(i)
            try:
                IP1 = socket.gethostbyaddr(ip)
                self.write_csv_file(IP1)
            except socket.herror:
                pass
            except socket.gaierror:
                print('Invalid input')
                break
    #################################### CSV ###################################
    def write_csv_file(self, IP):  # Define writing function METHOD 1
        writer = csv.writer(self.wr_file, delimiter=' ')
        ip = str(IP)
        format_ip = ip.replace('[', '').replace(']', '').replace("'", '').replace(' ', '').replace('(','').replace(')', '').replace(',,', '->')
        writer.writerow(format_ip)
        print(format_ip)

    def read_csv_file(self):  # Define read function
        re_file = open(self.file_path, 'r')
        reader = csv.reader(re_file)
        for row in reader:
            print(row)
    #################################### Localhost print ########################
    def print_localhost_ip(self):
        print('This Pc IP:')
        IP1 = socket.gethostbyname(socket.gethostname())    # local IP adress of your computer
        HN1 = socket.getfqdn()  # Hostname local
        print(HN1,'',IP1)

class NetworkDiscoveryMenu(NetworkDiscoveryCore):
    def main_menu(self):
        print('''
        1.  Open File
        2.  Network Discovery
        3.  Read csv File
        ''')

    def main_menu_choice(self):
        exit_menu = True
        choice_input = input("> ")
        while exit_menu:
            if choice_input == '1':
                self.input_path()
            elif choice_input == '2':
                self.perform_net_discovery()
            elif choice_input == '3':
                self.read_csv_file()
            elif choice_input == '0':
                exit_menu = False
                break
            elif choice_input == 'm':
                self.main_menu()
            else: print('Error')
            choice_input = input("> ")



