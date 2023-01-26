import optparse
import subprocess
import re

# this is a reader that will take network interface and mac address
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="network_interface", help="This place is for network interface")
    parser.add_option("-m", "--mac", dest="new_mac", help="This place is for MAC address")
    options, arguments = parser.parse_args()
    
    if not options.network_interface:
        parser.error("[-] Specify an network interface, type -h for help")
        
    if not options.new_mac:
        parser.error("[-] Specify MAC address, type -h for help")
        
    return options

# these are system commands that will change the mac address for a network interface
def mac_changer(network_interface, new_mac):
    subprocess.call("ifconfig" + network_interface + " down", shell=True)
    subprocess.call("ifconfig" + network_interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig" + network_interface + " up", shell=True)
    print("[+] Changing MAC address for " + network_interface + " to " + new_mac)
    
# filtering mac address
def get_mac(network_interface):
    ifconfig_result = subprocess.check_output("ifconfig " + network_interface, shell=True).decode("UTF-8")
    mac_address = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    return mac_address[0]

options = get_arguments()
mac_changer (options.network_interface, options.new_mac)
mac_address = get_mac(options.network_interface)

if mac_address == options.new_mac:
    print("[+] MAC address has changed succesfully")
else:
    print("[-] something went wrong...")

    
    
    
    
    
    

