from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import mimetypes
import base64
import csv

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://mail.google.com/']

def create_message_with_attachment(sender, to, subject, message_text, file):
  message = MIMEMultipart()
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  msg = MIMEText(message_text, 'html')
  message.attach(msg)

  content_type, encoding = mimetypes.guess_type(file)  
  if content_type is None or encoding is not None:
    content_type = 'application/octet-stream'
  main_type, sub_type = content_type.split('/', 1)
  if main_type == 'text':
    fp = open(file, 'rb')
    msg = MIMEText(fp.read(), _subtype=sub_type)
    fp.close()
  elif main_type == 'image':
    fp = open(file, 'rb')
    msg = MIMEImage(fp.read(), _subtype=sub_type)
    fp.close()
  elif main_type == 'audio':
    fp = open(file, 'rb')
    msg = MIMEAudio(fp.read(), _subtype=sub_type)
    fp.close()
  else:
    fp = open(file, 'rb')
    msg = MIMEBase(main_type, sub_type)
    msg.set_payload(fp.read())
    fp.close()
  filename = os.path.basename(file)
  msg.add_header('Content-Disposition', 'attachment', filename=filename)
  message.attach(msg)
  return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_message(service, user_id, message):
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print(f"Message Id: %s {message['id']} ")
    return message
  except Exception as error:
    print("An error occurred: " + str(error))


def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'keys.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    #CHANGE THISSS
    #Assuming the list.csv contains the names and emails of all the recievers
    file = open('list.csv')
    csvreader = csv.reader(file)
    rows = []
    final_message = """<html><body>
<pre>
Greetings to all!

We are so glad that you have participated at WASPCON '2021 which was conducted on 9th and 10th October,2021. Thank you for supporting our event by attending and contributing. We hope you enjoyed the experience and received beneficial information which motivated you to pursue cyber security.

Here are your perks that we promised you for your participation! 
1. Participation Certificate (find in the attachment)

2. Wanderlooms Coupon 
- Website: <a href="https://www.wanderlooms.com/">Wanderlooms </a>(30% discount on all its merchandise)
- Coupon Code: Wasp30
- Deadline: 31-12-2021

3. GFG coupons ( You may have already received from GFG on your emails)

Happy Learning!

Regards,
OWASP VITCC

PS: The names are taken from the VIT Chennai events. If there are any changes to the name, please revert back to us on or before 20.10.2021 23:59 (Wednesday).
</pre></body></html>
"""
    final_msg = MIMEText(final_message, 'html')
    for row in csvreader:
            rows.append(row)
    rows.pop(0)
    for i in rows:
        #CHANGE THISSS
        path = "./attachments/" + i[0].upper() + ".png"
        message = create_message_with_attachment('owasp@vit.ac.in', i[1], 'WaspCon 2021', final_message, path)
        send_message(service, "me", message)

if __name__ == '__main__':
    main()