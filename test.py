import requests

API_KEY = "AIzaSyDyoZ13tvOSmoLKy_tPb3r06EQ89KdthQQ"
video_id = "dQw4w9WgXcQ"  # Example Video ID
url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)