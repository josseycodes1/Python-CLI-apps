import smtplib

email = input("SENDER MAIL ")
reciever_email = input("RECIEVER MAIL ")

subject = input("SUBJECT: ")
message = input("MESSAGE: ")

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com", 465)
server.starttls()

server.login(email, "")

server.sendmail(email, reciever_email, text)

print("Email has been sent to " + reciever_email)