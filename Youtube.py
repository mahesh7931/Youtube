
import pandas as pd
from googleapiclient.discovery import build
api_key = 'AIzaSyBk32nVUgKJPF9-ekBeY_JdRYfTjb38_AQ'
youtube = build('youtube', 'v3', developerKey=api_key)

#my playlist ID
playlist_id='PL_uyOi8hwHev0-7bk3PD3-cd9RaqhECRA' 



#Fetching Video id of Which we want to get detail 
def get_video_ids(youtube, playlist_id):
    
    request = youtube.playlistItems().list(
                part='contentDetails',
                playlistId = playlist_id,
                maxResults = 10)
    response = request.execute()
    
    video_ids = []

    #appending Each ID in list

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
       
    return video_ids

#calling Video ID Function    
VideoID=get_video_ids(youtube, playlist_id)


#Getting details of video
def get_video_details(youtube, video_ids):
    video_title = []
    video_Published_Date=[]
    video_Like=[]
    video_view=[]
    request = youtube.videos().list(
              part='snippet,statistics',
              id=','.join(video_ids))
    response = request.execute()
    
                               
                               
    for video in response['items']:
                               video_title.append(video['snippet']['title'])
                               video_Published_Date.append(video['snippet']['publishedAt']) 
                               video_Like.append(video['statistics']['likeCount'])
                               video_view.append(video['statistics']['viewCount'])

    #creating data Frame for store the details                            
    dxf=pd.DataFrame()
    
    dxf['VideoID']=VideoID[0:]  
    dxf['Title']=video_title[0:]
    dxf['PublishDate']=video_Published_Date[0:]
    dxf['Like']=video_Like[0:]
    dxf['View']=video_view[0:]
    

    #writing Dataframe to CSV File
    dxf.to_csv('file2.csv')    

get_video_details(youtube,VideoID)    