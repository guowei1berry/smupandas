import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import datetime

logging_path = '/home/ftpsensor_user/daily_compiled/aggregation/logging.txt'
now = datetime.datetime.now()
current_date = now.date()

def send_email(from_email, to_email, subject, body,attachment_paths=None, smtp_server='smtp.gmail.com', smtp_port=587, username='oneberrysmucoolschools@gmail.com', password='YOURSECRETKEYHERE'):

# Email account credentials
# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# username = 'oneberrysmucoolschools@gmail.com'
# password = 'YOURSECRETKEYHERE'

# Email content
# from_email = 'oneberrysmucoolschools@gmail.com'
# to_email = 'du.guowei@oneberry.com'
# subject = 'Test Email'
# body = 'This is a test email sent from a Python script!'

# Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file if provided
    if attachment_paths:
        for attachment_path in attachment_paths:
    # if attachment_path:
            match =os.path.basename(attachment_path).split('/')[-1]
            try:
                with open(attachment_path, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', f'attachment; filename={match}')
                    msg.attach(part)
            except Exception as e:
                print(f'Failed to attach file: {e}')

    try:
        # Set up the server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(username, password)  # Login to the email server

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        print('Email sent successfully!')

    except Exception as e:
        print(f'Failed to send email: {e}')
        with open(logging_path, "a") as f:
            print(f'Failed to send email: {e} on {current_date}')

    # finally:
    #     server.quit()  # Close the connection to the server
