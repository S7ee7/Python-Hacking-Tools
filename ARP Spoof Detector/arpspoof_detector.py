import scapy.all as scapy


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)
 
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = arp_broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered[0][1].hwsrc 
 
def process_packet(packet):
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
        try:
            real_mac = get_mac(packet[scapy.ARP].psrc)
            response_mac = packet[scapy.ARP].hwsrc
            if response_mac != real_mac:
                print("[+] Under Attack!")
        except IndexError:
            pass
        
sniff("eth0")


