import api # Create a file named `api.py` and put `API_KEY = "your_api_key"` inside of it
import requests
import isodate
import os

os.system("cls")
API_KEY = api.API_KEY

def parseDuration(duration):
    return int(isodate.parse_duration(duration).total_seconds())

def main():
    input("Press [ENTER] to receive your random number...")
    os.system("cls")

    searchUrl = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&order=date&part=id&type=video&maxResults=1"
    response = requests.get(searchUrl).json()

    if response.get("items"):
        latestVideo = response["items"][0]["id"]["videoId"]
        videoUrl = f"https://www.googleapis.com/youtube/v3/videos?key={API_KEY}&id={latestVideo}&part=contentDetails"
        videoResponse = requests.get(videoUrl).json()

        if videoResponse.get("items"):
            duration = videoResponse["items"][0]["contentDetails"]["duration"]

            print(parseDuration(duration))
        else:
            print("Details of the video could not be obtained")
    else:
        print("No recent videos could be found")

    main()

main()
