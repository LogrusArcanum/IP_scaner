from NetworkDiscoveryCore import *
import re

ntcore = NetworkDiscoveryCore()


class NetworkDiscoverySearch:
    def __init__(self):
        self.iplist = ntcore.read_csv_file()

    def inputSearch(self):
        for item in self.iplist:
            self.formated_inp = ntcore.format_input(item)
            if inp in self.formated_inp:
                print(item)
