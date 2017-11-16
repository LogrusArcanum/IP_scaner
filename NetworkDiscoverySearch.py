from NetworkDiscoveryCore import *
import re

ntcore = NetworkDiscoveryCore()


class NetworkDiscoverySearch:
    def __init__(self):
        self.iplist = ntcore.read_csv_file()
        self.formated_inp = ntcore.format_input(self.iplist)
        print(self.formated_inp)

    def inputSearch(self):
        inp = input('Input Hostname: ')
        x = [n for n in self.formated_inp if inp in n]
        print(x)


