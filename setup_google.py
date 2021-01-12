import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

# setup_google.py allows user to log into 
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)