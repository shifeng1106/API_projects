# -*- coding: utf-8 -*-
"""api.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1F3pTqXTBsjsuz8HW8WjzwhVq-kt6Gt63
"""

#Import libraries 

import pandas as pd
import numpy as np
import requests 
import time 

#KEYS
API_KEY = 'AIzaSyCsIJbk1Hqymq3BRCKmguoDZHLniD66CwM'
CHANNEL_ID = 'UCW8Ews7tdKKkBT6GdtQaXvQ'

response['items'][1]

video_id = response['items'][0]['id']['videoId']

def get_video_details(video_id):

  url_stats = 'https://www.googleapis.com/youtube/v3/videos?id='+video_id+'&part=stastics&key='+API_KEY
  response_stats = requests.get(url_stats).json()
  view_counts = response_stats['items'][0]['statistics']['viewCount']
  like_counts = response_stats['items'][0]['statistics']['likeCount']
  dislike_counts = response_stats['items'][0]['statistics']['dislikeCount']
  comment_counts = response_stats['items'][0]['statistics']['commentCount']
  
  return view_counts,like_counts , dislike_counts,comment_counts

#Make API call
def get_videos(df):
  pageToken = ''
  url = 'https://www.googleapis.com/youtube/v3/search?key='+API_KEY+'&channelId'+CHANNEL_ID+'&part=snippet,id&order=date&maxResults=10000'+pageToken
  response = requests.get(url).json()
  time.sleep(2)

  for video in response['items']:
    
    if video['id']['kind'] == 'youtube#video':
      video_id = video['id']['videoId']
      video_title = video['snippet']['title']
      video_title = str(video_title).replace('&amp;','')
      upload_date = video['snippet']['publishedAt']
      upload_date = str(upload_date).split('T')[0]

  view_counts,like_counts , dislike_counts,comment_counts = get_video_details(video_id)
  
  df = df.append({'video_id' : video_id, 'video_title':video_title, 
                    'upload_date' :upload_date,'view_counts':view_counts,
                    'like_counts':like_counts,
                    'dislike_counts':dislike_counts,
                    'comment_counts':comment_counts}, ignore_index = True)




  return df

df = pd.DataFrame(columns = ['video_id', 'video_title', 'upload_date', 'view_counts', 'like_counts', 'dislike_counts', 'comment_counts'])
df = get_videos(df)
df