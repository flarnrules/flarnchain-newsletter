
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import FC_NEWSLETTER_AUTHOR, FC_NEWSLETTER_PASSWORD
from database_handler import connect_to_database, fetch_emails, close_connection
from database_handler import main as fetch_emails_from_database

# Read the HTML file that contains the email payload
with open ('../newsletters/newsletter_template.html', 'r') as file:
    html_template = file.read()

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
message["Subject"] = "This is the subject"
message["From"] = email_from
message["To"] = ", ".join(email_to)

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

    print()
    print(f"Sending email to - {email_to}")

    # Create the email message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Your Subject Here"
    message["From"] = email_from
    message["To"] = ", ".join(email_to)

    part_html = MIMEText(html_template, "html")
    message.attach(part_html)

    TIE_server.sendmail(email_from, email_to, message.as_string())
    print(f"Email successfully sent to - {email_to}")

except Exception as e:
    print(e)

finally:
    try:
        TIE_server.quit()
    except:
        print("Server connection already closed.")

