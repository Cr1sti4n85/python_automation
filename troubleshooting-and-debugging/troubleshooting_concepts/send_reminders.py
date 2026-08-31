import datetime
import smtplib
import sys
from email.message import EmailMessage
import csv

def usage():
    print("send_reminders: Send meeting reminders")
    print()
    print("Invocation")
    print("  send_reminders.py <date>|Meeting title|Emails")

def dow(date):
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title, name):
    message = EmailMessage()
    weekday = dow(date)
    message["Subject"] = f'Meeting reminder: "{title}"'
    message.set_content(f'''
    Hi {name}
    This is a quick mail to remind you all that we have a meeting about: "{title}"
    the {weekday} {date}.
    See you there"
    ''')
    return message

def get_name(contacts, email):
    name = ""
    with open(contacts) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == email:
                name = row[0]
    return name

def send_message(date, title, emails, contacts):
    smtp = smtplib.SMTP("localhost")
    for email in emails.split(','):
        name = get_name(contacts, email)
        message = message_template(date, title, name)
        message["From"] = "noreply@example.com"   
        message["To"] = email
        smtp.send_message(message)
    smtp.quit()
    pass

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        date, title, emails = sys.argv[1].split('|')
        send_message(date, title, emails, "contacts.csv")
        print("Successfully sent reminders to:", emails)
    except Exception as e:
        print("Failure to send email", file=sys.stderr)