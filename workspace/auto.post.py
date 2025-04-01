import os
import time
import schedule
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.http import MediaFileUpload


CLIENT_SECRET_FILE = 'credentials.json'  
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]


def authenticate_youtube_api():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    youtube = googleapiclient.discovery.build(API_NAME, API_VERSION, credentials=creds)
    return youtube


def upload_video(youtube, video_file, title, description, hashtags, privacy_status="public"):
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': hashtags,  
            'categoryId': '22', 
        },
        'status': {
            'privacyStatus': privacy_status,
        }
    }

    try:
        print(f'Uploading video: {video_file}')
        request = youtube.videos().insert(
            part="snippet,status",
            body=request_body,
            media_body=MediaFileUpload(video_file, mimetype="video/*")
        )
        response = request.execute()
        print(f'Successfully uploaded video: {response["id"]}')
    except googleapiclient.errors.HttpError as e:
        print(f'Error during video upload: {e}')


def post_video_at_scheduled_time():
  
    video_file = 'short_video.mp4'  
    title = "Exciting YouTube Short!" 
    description = "This is an exciting YouTube Short! #shorts #fun #comedy"
    hashtags = ['shorts', 'comedy', 'viral', 'entertainment', 'funny', 'trending', 'video']

   
    youtube = authenticate_youtube_api()

    # Upload the video
    upload_video(youtube, video_file, title, description, hashtags)


def schedule_auto_post():
   
    schedule.every().day.at("09:00").do(post_video_at_scheduled_time) 

    while True:
        schedule.run_pending()
        time.sleep(60)  

if __name__ == "__main__":
    schedule_auto_post()
