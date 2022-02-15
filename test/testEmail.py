
from sys import path
path.append("../")

import logging as log
import unittest
import libCommon as COMMON
from libConstants import CUSTOM
import libEmail as TEST

test_from = "marketing.womenonwheels@gmail.com"
password = "HotBikerBabes@2020"
client_list =  [{"user_email" : "chriswithteal@gmail.com","first_name":"Puppy","last_name":"Paws", "user_login":"puppypaws"},
                {"user_email" : "martiel@martielbeatty.com","first_name":"Martiel", "last_name":"and Staff", "user_login" : "FlamingoOne"}]
test_subject="Hello user {user_login}"
test_body=CUSTOM.body[:700]

class TestEmailSend(unittest.TestCase) :
    def testPersonalize(self) :
        #check log file
        TEST.CLIENTS.personalize(user_login="BobOne",first_name="Bobby",last_name="Smith",
                                 SUBJECT="test",TO="me",FROM="you",message=test_body)
    def testReadFiles(self) :
        _file_list = COMMON.find_files("Email")
        log.debug(_file_list)
    def testTransform(self) :
        _client_list = TEST.CLIENTS.load(filename="email.csv")
        if len(_client_list) > 3 :
            _client_list = _client_list[:3]
        for client in _client_list :
            log.debug(client)
        for client in TEST.CLIENTS._transform(test_from,test_subject,*_client_list) :
            pass
            #scheck log file
    def testBulkSend(self) :
        server = TEST.EMAIL.gmail(user=test_from,pswd=password)
        for _from, _to, msg in TEST.CLIENTS.transform(test_from,test_subject,test_body,*client_list):
            server.sendmail(_from, _to, msg)
        server.quit()

if __name__ == '__main__' :
   import sys
   log_file = COMMON.build_args(*sys.argv).replace('.py','') + '.log'
   #log_file = COMMON.build_path('../log',log_file)
   #COMMON.remove_file(log_file)
   #COMMON.mkdir("../log")
   log.basicConfig(filename=log_file, format=COMMON.LOG_FORMAT_TEST, level=log.DEBUG)
   unittest.main()

