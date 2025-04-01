import os
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


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
            media_body=googleapiclient.http.MediaFileUpload(video_file, mimetype="video/*")
        )
        response = request.execute()
        print(f'Video uploaded successfully: {response["id"]}')
    except googleapiclient.errors.HttpError as e:
        print(f'An error occurred: {e}')


def main():
    video_file = 'short_video.mp4'  
    title = "Exciting New Short Video" 
    description = "This is a YouTube Short video with awesome content! #shorts #fun #entertainment"
    hashtags = ['shorts', 'fun', 'entertainment', 'viral', 'comedy', 'video', 'youtubeshorts', 'new', 'explore', 'creative']
    
   
    youtube = authenticate_youtube_api()


    upload_video(youtube, video_file, title, description, hashtags)

if __name__ == "__main__":
    main()
