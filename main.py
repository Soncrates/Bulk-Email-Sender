import logging as log
from time import sleep

import libCommon as COMMON
import libEmail as MAIN
from libConstants import CUSTOM

mgr= "someone@gmail.com"
pswd = "pswd123"
subject = "Notification - Account Info for {user_login}"
message = CUSTOM.body

def prep() :
    file_list = COMMON.find_files("Email")
    log.info(file_list)
    return MAIN.CLIENTS.load(filename="email.csv")

def main(*client_list) :
    server = MAIN.EMAIL.gmail(user=mgr,pswd=pswd)
    log.info("begin sending emails : {}".format(len(client_list)))
    sleep(5)
    
    count=20
    for _from, _to, _subject, msg in MAIN.CLIENTS.transform(mgr,subject,message,*client_list):
        sleep(5)
        server.sendmail(_from, _to, msg)
        count=-1
        if count > 0 :
           count=20
           sleep(600)
    server.quit()

    log.info("Succesfully emailed all clients")

if __name__ == '__main__' :
   import sys
   log_file = COMMON.build_args(*sys.argv).replace('.py','') + '.log'
   #log_file = COMMON.build_path('../log',log_file)
   #COMMON.remove_file(log_file)
   #COMMON.mkdir("../log")
   log.basicConfig(filename=log_file, format=COMMON.LOG_FORMAT_APP, level=log.INFO)
   client_list = prep()
   main(*client_list)
