import csv
import smtplib
import logging as log

class CLIENTS :
    
    @staticmethod
    def load(**arg) :
        fields = []
        rows = []
        ret = arg.get('filename',"email.csv")
        with open(ret, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            for row in csvreader:
                row = dict(zip(fields,row))
                rows.append(row)
        return rows

    @staticmethod
    def personalize(message,**args) :
        ret = message.format(**args).encode('ascii','ignore')
        log.debug(ret)
        return ret
    
    @staticmethod
    def _transform(_from, subject, *client_list) :
        default = {"FROM": _from}
        for client in client_list:
            default['TO'] = client['user_email']
            default['SUBJECT'] = subject.format(**client)
            client.update(default)
            log.debug(client)
            yield client
            
    @staticmethod
    def transform(SenderAddress,subject,body,*client_list) :
        for client in CLIENTS._transform(SenderAddress,subject,*client_list):
            msg = CLIENTS.personalize(body, **client)
            yield client["FROM"], client["TO"], msg

class EMAIL :
    @staticmethod
    def gmail(**args) :
        user = args.get("user")
        pswd = args.get("pswd")
        ret = smtplib.SMTP("smtp.gmail.com", 587)
        ret.starttls()
        ret.login(user, pswd)
        return ret
