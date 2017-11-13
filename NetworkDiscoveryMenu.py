from NetworkDiscoveryCore import *

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