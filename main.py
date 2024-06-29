import requests # Without this I can't make calls to the api
import isodate # Needed to easily transform lenght to seconds
import os # I just want to clear the console
from dotenv import load_dotenv

load_dotenv()

os.system("cls")
API_KEY = os.getenv("API_KEY")

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
