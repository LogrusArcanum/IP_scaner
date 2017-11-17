from NetworkDiscoveryCore import *
from NetworkDiscoverySearch import *

class NetworkDiscoveryMenu(NetworkDiscoveryCore):
    def main_menu(self):
        print('''
        1.  Open File
        2.  Network Discovery
        3.  Read csv File
        4.  Print localhost hostname ip
        5.  Search Hostname/IP
        0.  Exit
        m.  Menu
        ''')
        self.main_menu_choice()

    def main_menu_choice(self):
        exit_menu = True
        choice_input = input("> ")
        while exit_menu:
            if choice_input == '1':
                self.input_path()
            elif choice_input == '2':
                self.network_discovery_submenu()
            elif choice_input == '3':
                print(self.read_csv_file())
            elif choice_input == '4':
                self.print_localhost_ip()
            elif choice_input == '5':
                NetworkDiscoverySearch().inputSearch()
            elif choice_input == '0':
                exit_menu = False
                print('Confirm exit: ')
                break
            elif choice_input == 'm':
                self.main_menu()
            else:
                print('Error')
            choice_input = input("> ")

    def network_discovery_submenu(self):
        print('''
        1.  Auto Network Discovery
        2.  Custom Network Discovery
        0.  Exit
        m.  Menu
        ''')
        self.network_discovery_submenu_choice()

    def network_discovery_submenu_choice(self):
        choice_input = input("  > ")
        exit_menu = True
        while exit_menu:
            if choice_input == '1':
                self.auto_network_discovery()
            elif choice_input == '2':
                self.perform_net_discovery()
            elif choice_input == 'm':
                self.network_discovery_submenu()
            elif choice_input == '0':
                exit_menu = False
                self.main_menu()
                break
            else:
                print('Invalid Input!')
                break
            choice_input = input("  > ")

    def auto_network_discovery(self):
        print('Auto Network Discovery...')
