# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
server = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
server.starttls()
 
# Authentication
server.login("sriharsha8811@gmail.com", "7406123970")
 
# message to be sent
message = "hi hello"
 
# sending the mail
server.sendmail("sufiyatahseen12345@gmail.com", "sufiyatahseen12345@gmail.com", message)
print("sss")

# terminating the session
server.quit()
