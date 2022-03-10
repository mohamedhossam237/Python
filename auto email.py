import smtplib
from email.message import EmailMessage
  
msg= EmailMessage()
msg['Subject']='happy birthday'
msg['from']='Aysha'
msg['To']='aydasameh22@gmail.com'
msg.set_content("Test Email from Aysha")

server =smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login("ayda3854@gmail.com", "Aydasameh997899787657890")
server.send_message(msg)
server.quit()