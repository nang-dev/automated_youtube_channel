import datetime
import dateutil.relativedelta
from instalooter.looters import InstaLooter, ProfileLooter
import instaloader
from instalooter.cli.login import login

# scrape_videos.py scrapes all the videos from pages we are following
def scrapeVideos(username = "",
                 password = "",
                 output_folder = "",
                 days = 1):
        
    print("Starting Scraping")

    L = instaloader.Instaloader()

    # Login or load session for loader
    L.login(username, password)  
    profile = instaloader.Profile.from_username(L.context, username)
    following = profile.get_followees()
    print(following)

    today = datetime.date.today()
    timeframe = (today, today - dateutil.relativedelta.relativedelta(days=days))

    for profile in following:
        acc = profile.username
        looter = ProfileLooter(acc, videos_only=True, template="{id}-{username}-{width}-{height}")
        if not looter.logged_in():
            looter.login(username, password)
        print("Scraping From Account: " + acc)
        try:
            numDowloaded = looter.download(output_folder, media_count=30, timeframe=timeframe)
            print("Downloaded " + str(numDowloaded) + " videos successfully")
            print("")
        except Exception as e:
            print("Skipped acc " + acc + "because of");
            print(e);


if __name__ == "__main__":
    scrapeVideos(username = "chewymemes_v3",
                 password = "",
                 output_folder = "./Memes_December_4")
