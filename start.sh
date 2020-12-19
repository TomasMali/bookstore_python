#!/bin/bash



/Library/Frameworks/Python.framework/Versions/3.8/bin/python3  /Users/tomas/Desktop/tomas/frontend.py






server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("tomasmali08@gmail.com", "..Tomi92")

email_user = "pireetona"

server.sendmail("tomasmali08@gmail.com",  "pireetona@gmail.com", "Hello how are you")



server.quit()
