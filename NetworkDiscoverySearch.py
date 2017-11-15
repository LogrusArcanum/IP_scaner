from NetworkDiscoveryCore import *

ntcore = NetworkDiscoveryCore


class NetworkDiscoverySearch:
    def __init__(self):
        self.iplist = []
        self.iplist.append(ntcore.read_csv_file)
        # print(iplist)

    def inputSearch(self):
        inp = input('Input Hostname: ')
        for item in self.iplist:
            if inp in self.iplist:
                print(item)
                break
