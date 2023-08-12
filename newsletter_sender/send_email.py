
import smtplib
import ssl
from settings import FC_NEWSLETTER_AUTHOR, FC_NEWSLETTER_PASSWORD
from database_handler import connect_to_database, fetch_emails, close_connection
from database_handler import main as fetch_emails_from_database


# Setup port number and server number
smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server
email_from = FC_NEWSLETTER_AUTHOR
email_to = fetch_emails_from_database()
password = FC_NEWSLETTER_PASSWORD

# Content of message
message = "hi"
simple_email_context = ssl.create_default_context()


try:
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, password)
    print("Connected to server")

    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

except Exception as e:
    print(e)

finally:
    TIE_server.quit()
