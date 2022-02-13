import pandas as pd
import smtplib

class CLIENTS :
    @staticmethod
    def load(**arg) :
        return [{"email" : "chriswithteal@gmail.com","name":"Puppy Paws", "user":"puppypaws"},
                {"email" : "martiel@martielbeatty.com","name":"Martiel and her Boobs", "user" : "FlamingoOne"}]
    @staticmethod
    def addSubject(**ret) :
        ret['SUBJECT'] = "Women On Wheels Notification - Account Info {user}".format(**args)
        return ret

    @staticmethod
    def personalize(**arg) :
        args = CLIENTS.addSubject()
        args['TEXT'] = CLIENTS._personalize(**args)
        return f'Subject: {SUBJECT}\n\n{TEXT}'.format(**args)
    @staticmethod
    def _personalize(**arg) :
        return """
Hi {name},

Welcome to the new Women On Wheels website. You are receiving this email because you have an active membership with our organization.

Your account has been successfully transferred from the old website/system to the new one. In this email you'll find the following information

1. Where to login to your account, what your username is and how to set your password.
2. A list of Frequently Asked Questions
3. Where to get help if you get stuck

WHERE AND HOW TO LOGIN TO YOUR ACCOUNT FOR THE FIRST TIME

1. Go to https://womenonwheels.org/member-login
2. Enter your username: {user}
3. Enter THIS Password: NTJ$%100

IF YOU DO NOT WANT TO USE THE SYSTEM PASSWORD PROVIDED ABOVE, YOU MAY CHANGE IT by going to https://womenonwheels.org/lost-password/ - you will receive an email with a link to set a new password of your choice.

FREQUENTLY ASKED QUESTIONS

Q: How do I login to my account?
A: To login to your account, you got to https://womenonwheels.org/member-login

Q: Where do I go to see the site?
A: You can visit the site at https://womenonwheels.org

Q: When will I be able to register for the Ride-In™?
A: Yes, please login to your account and you’ll be able to register.

Q: Will a paper registration form still be available for the Ride-In™?
A: Yes, please login to your account to download this or you can visit the non-member registration page (no login required) at https://womenonwheels.org/ride-in

Q: If I have difficulty, how do I get help?
A: We’re here to help! Please reach out to us at membership1@womenonwheels.org

Q: If I forget my password, how do I reset it?
A: Anytime you’d like to reset your password, you can go to https://womenonwheels.org/lost-password/

Q: I logged in and my membership level is incorrect, what do I do?
A: Please reach out to us at membership1@womenonwheels.org and we’ll work with the website team to get things corrected for you asap.

Q: The renewal date on my profile is incorrect, how do I fix that?
A: Please reach out to us at membership1@womenonwheels.org and we’ll work with the website team to get things corrected for you asap.
password
Q: How do I add a profile picture and is this required?
A: No, it’s completely optional.

WHERE TO GET HELP

If you're stuck, please feel free to reach out to membership1@womenonwheels.org or call the WOW office at 402-326-9736 we'll be standing by with the assistance of the website development team to support you.


""".format(**args)
    
class EMAIL :
    @staticmethod
    def gmail(**args) :
        user = args.get("user",SenderAddress)
        pswd = args.get("pswd",password)
        ret = smtplib.SMTP("smtp.gmail.com", 587)
        ret.starttls()
        ret.login(user, pswd)
        return ret
    @staticmethod
    def bulk(server, *client_list) :
        for client in client_list:
            server.sendmail(SenderAddress, client["email"], CLIENT.personalize(**client))
        server.quit()
