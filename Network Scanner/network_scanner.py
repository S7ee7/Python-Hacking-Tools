import scapy.all as scapy
import optparse

def get_arugments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--range", dest="network_ip", help="To enter device IP or Network Range")
    options, arguments = parser.parse_args()
    
    if not options.network_ip:
        parser.error("[-] Please specify an IP Address, -h for help")
    
    return options

def scan(network_ip):
    arp_request = scapy.ARP(pdst=network_ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = arp_broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    client_list = []
     
    for ans in answered:
        client_dict = {"ip":ans[1].psrc, "mac":ans[1].hwsrc}
        client_list.append(client_dict)
     
    return client_list

def display_clients(clients):
    print("IP Address\t\t MAC address")
    print("-" * 42)
    for client in clients:
        print(client["ip"], "\t\t", client["mac"])

options = get_arugments()
client_list = scan(options.network_ip)
display_clients(client_list)