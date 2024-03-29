import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import FC_NEWSLETTER_AUTHOR, FC_NEWSLETTER_PASSWORD
from database_handler import main as fetch_emails_from_database

# Read the HTML file that contains the email payload
with open ('../newsletters/132.html', 'r') as file:
    html_template = file.read()
print(html_template)

# Setup port number and server number
smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server
email_from = FC_NEWSLETTER_AUTHOR
email_to = fetch_emails_from_database()
password = FC_NEWSLETTER_PASSWORD

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##          Create Multipart message             ##
## This can be improved and pull variables in    ##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

message = MIMEMultipart("alternative")
message["Subject"] = "Flarnchain Newsletter #132 - A New Paradigm"
message["From"] = email_from
message["To"] = "Flarnchain Subscribers"

##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##         End of the multipart message          ##
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

simple_email_context = ssl.create_default_context()

try:
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, password)
    print("Connected to server")

    print(f"Sending email to - {', '.join(email_to)}")

    part_html = MIMEText(html_template, "html")
    message.attach(part_html)

    # Send the email using BCC, without setting the "To" field in the header
    TIE_server.sendmail(email_from, email_to, message.as_string())
    print(f"Email successfully sent to - {', '.join(email_to)}")
    print(f"Email sent to {len(email_to)} recipients successfully.")

except Exception as e:
    print(e)

finally:
    try:
        TIE_server.quit()
    except:
        print("Server connection already closed.")