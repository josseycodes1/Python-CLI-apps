import smtplib
from email.mime.text import MIMEText

# Get email details from user input
email = input("Enter your email: ")
reciever_email = input("Enter receiver's email: ")
subject = input("Enter the subject: ")
message = input("Enter the message: ")

# Format the email content
text = f"Subject: {subject}\n\n{message}"

# Set up the SMTP server (Gmail) with SSL
try:
    print("Connecting to the server...")

    # Use SSL on port 465 for Gmail
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    # Login to Gmail
    password = input("Enter your email password or app password: ")
    server.login(email, password)

    print("Sending the email...")

    # Send the email
    server.sendmail(email, reciever_email, text)

    # Confirmation message
    print(f"Email has been sent to {reciever_email}")

    # Close the connection
    server.quit()

    print("Connection closed.")

except smtplib.SMTPException as e:
    print(f"SMTP error: {e}")
except Exception as e:
    print(f"Error: {e}")
