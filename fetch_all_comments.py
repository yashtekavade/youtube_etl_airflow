import os
import pandas as pd
from googleapiclient.discovery import build

API_KEY = "YOUR_API_KEY"  # Replace with your YouTube API key
VIDEO_ID = "q8q3OFFfY6c"  # Replace with the target YouTube video ID

def get_youtube_service():
    return build('youtube', 'v3', developerKey=API_KEY)

def process_comments(items):
    comments = []
    for comment in items:
        snippet = comment['snippet']['topLevelComment']['snippet']
        comments.append({
            'author': snippet['authorDisplayName'],
            'comment': snippet['textOriginal'],
            'published_at': snippet['publishedAt']
        })
    return comments

def fetch_all_comments(video_id):
    youtube = get_youtube_service()
    comments_list = []
    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        textFormat='plainText'
    )
    
    while request:
        response = request.execute()
        comments_list.extend(process_comments(response['items']))
        request = youtube.commentThreads().list_next(request, response)
    
    return comments_list

def save_comments_to_csv(comments, filename='comments.csv'):
    df = pd.DataFrame(comments)
    df.to_csv(filename, index=False)
    print(f"Saved {len(comments)} comments to {filename}")

def main():
    comments = fetch_all_comments(VIDEO_ID)
    save_comments_to_csv(comments)

if __name__ == "__main__":
    main()
