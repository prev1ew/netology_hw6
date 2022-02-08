"""
NOTE: в Украине яндекс заблокирован (да, нашел оправдание)
поэтому сделано через гугл драйв
PS: в яндексе дикая документация с которой без 100 грамм не розберешься (мне жалко других студентов)
"""

import os
import pickle
# import sys

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
# from base64 import urlsafe_b64decode, urlsafe_b64encode
# # for dealing with attachement MIME types
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage
# from email.mime.audio import MIMEAudio
# from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
from googleapiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']


def gdrive_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('drive', 'v3', credentials=creds)


def upload_file_to_gdrive(service, path, file_metadata):
    media = MediaFileUpload(path, mimetype=guess_mime_type(path)[0])
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print(f'File ID: {file.get("id")}')


service = gdrive_authenticate()
upload_file_to_gdrive(service, 'test.html', {'name': 'test.html'})

# # ------------------------
#
#
# import requests
#
#
# class YaUploader:
#     def __init__(self, token: str):
#         self.token = token
#
#     def upload(self, file_path: str):
#         with open(file_path) as f:
#             requests.post()
#
#
#
# path_to_file = 'test.html'
# token = ''
# uploader = YaUploader(token)
# result = uploader.upload(path_to_file)
