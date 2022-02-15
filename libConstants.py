class CUSTOM:
    subject = "Notification - Account Info for {user_login}"
    body ="""From: {FROM}
To: {TO}
Subject: {SUBJECT}
Hi {first_name} {last_name}

Welcome to our new website. You are receiving this email because you have an active membership with our organization.

Your account has been successfully transferred from the old website/system to the new one. In this email you'll find the following information

1. Where to login to your account, what your username is and how to set your password.
2. A list of Frequently Asked Questions
3. Where to get help if you get stuck

WHERE AND HOW TO LOGIN TO YOUR ACCOUNT FOR THE FIRST TIME

1. Go to https://custom.org/member-login
2. Enter your username: {user_login}
3. Enter THIS Password: xxxxxx

IF YOU DO NOT WANT TO USE THE SYSTEM PASSWORD PROVIDED ABOVE, YOU MAY CHANGE IT by going to https://custom.org/lost-password/ - you will receive an email with a link to set a new password of your choice.

FREQUENTLY ASKED QUESTIONS

Q: How do I login to my account?
A: To login to your account, you got to https://custom.org/member-login

Q: Where do I go to see the site?
A: You can visit the site at https://custom.org

Q: If I have difficulty, how do I get help?
A: We’re here to help! Please reach out to us at membership1@custom.org

Q: If I forget my password, how do I reset it?
A: Anytime you’d like to reset your password, you can go to https://custom.org/lost-password/

Q: I logged in and my membership level is incorrect, what do I do?
A: Please reach out to us at membership1@custom.org and we’ll work with the website team to get things corrected for you asap.

Q: The renewal date on my profile is incorrect, how do I fix that?
A: Please reach out to us at membership1@custom.org and we’ll work with the website team to get things corrected for you asap.
password
Q: How do I add a profile picture and is this required?
A: No, it’s completely optional.

WHERE TO GET HELP

If you're stuck, please feel free to reach out to membership1@custom.org or call the WOW office at 402-326-9736 we'll be standing by with the assistance of the website development team to support you.


"""
