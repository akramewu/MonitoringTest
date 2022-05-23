import smtplib, ssl
username= 'akramewu@gmail.com'
recipient_email='akramulislam.de@gmail.com'
password= 'abgfsfnfddcbndey'
port = 465  # For SSL
# Create a secure SSL context
message = """\
Subject: Hi there

This message is sent from Tester Email."""
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(username, password)
    # TODO: Send email here
    server.sendmail(username, recipient_email, message)