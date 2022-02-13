from sys import path
path.append("../")

import libCommon as COMMON
import logging as log
import unittest
import script as TEST

class TestEmailSend(unittest.TestCase) :
    def dep_setUp(self) : 
        self.team_list_MLA = load_response("./test_input/team_list_MLA.html")
    def testshowMessage(self) :
        obj = TEST.CLIENTS.personalize(user='Bob',name="Bobby")
        log.info(obj)
    def testBulkSend(self) :
        SenderAddress = "marketing.womenonwheels@gmail.com"
        password = "HotBikerBabes@2020"
        server = TEST.EMAIL.gmail(user=SenderAddress,pswd=password)
        client_list = TEST.CLIENTS.load()
        TEST.EMAIL.bulk(server,*client_list)

if __name__ == '__main__' :
   import sys
   log_file = COMMON.build_args(*sys.argv).replace('.py','') + '.log'
   log_file = COMMON.build_path('../log',log_file)
   COMMON.remove_file(log_file)
   COMMON.mkdir("../log")
   log.basicConfig(filename=log_file, format=COMMON.LOG_FORMAT_TEST, level=log.DEBUG)
   unittest.main()
