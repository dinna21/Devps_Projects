import smtplib
# We nned to define the server
server = smtplib.SMTP("smtp.gmail.com",587)
# Then we need to call the start the server 
server.ehlo()
# We need email and the password for the server 
server.login('mail@gmail.com','password123')
with open('password.txt','r') as f:
    password = f.read()
server.login()