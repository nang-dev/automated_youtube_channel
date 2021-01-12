from scrape_videos import scrapeVideos
from make_compilation import makeCompilation
from upload_ytvid import uploadYtvid
import schedule
import time
import datetime
import os
import shutil

# FILL THESE OUT
IG_USERNAME = "chewymemes_v3" 
IG_PASSWORD = "mmm12345"

INTRO_VID = 'intro_vid.mp4' # SET AS '' IF YOU DONT HAVE ONE
OUTRO_VID = ''
TOTAL_VID_LENGTH = 13*60
MAX_CLIP_LENGTH = 18
MIN_CLIP_LENGTH = 4

num_to_month = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "June",
    7: "July",
    8: "Aug",
    9: "Sept",
    10: "Oct",
    11: "Nov",
    12: "Dec"
} 

def routine():
    now = datetime.datetime.now()
    print(now.year, now.month, now.day, now.hour, now.minute, now.second)
    title = "BEST DANK MEMES COMPILATION V" + str(now.month) + "." + str(now.day) + " (VIDEOS)"
    videoDirectory = "/tmp/Memes_" + num_to_month[now.month].upper() + "_" + str(now.year) + "_V" + str(now.day) + "/"
    outputFile = "./" + num_to_month[now.month].upper() + "_" + str(now.year) + "_v" + str(now.day) + ".mp4"
    metadataFile = "./metadata-" + num_to_month[now.month].upper() + "_" + str(now.year) + "_v" + str(now.day) + ".txt"
    description = ""
    print(outputFile)

    if not os.path.exists(videoDirectory):
        os.makedirs(videoDirectory)
    """
    # Step 1: Scrape Videos
    print("Scraping Videos...")
    scrapeVideos(username = IG_USERNAME,
                 password = IG_PASSWORD,
                 output_folder = videoDirectory,
                 days=1)
    print("Scraped Videos!")
    """
    f = open(metadataFile, "w")
    f.write(title + "\n\n")
    description = "Enjoy the memes :) \n\n" \
    "like and subscribe to @Chewy for more \n\n" \
    "The memes in the compilation are reposts from various private instagram meme accounts.\n" \
    "this episode's were from: \n"
    f.write(description)

    # Step 2: Make Compilation
    print("Making Compilation...")
    description += makeCompilation(path = videoDirectory,
                    introName = INTRO_VID,
                    outroName = OUTRO_VID,
                    totalVidLength = TOTAL_VID_LENGTH,
                    maxClipLength = MAX_CLIP_LENGTH,
                    minClipLength = MIN_CLIP_LENGTH,
                    outputFile = outputFile)
    print("Made Compilation!")
    
    description += "\n\nCopyright Disclaimer, Under Section 107 of the Copyright Act 1976, allowance is made for 'fair use' for purposes such as criticism, comment, news reporting, teaching, scholarship, and research. Fair use is a use permitted by copyright statute that might otherwise be infringing. Non-profit, educational or personal use tips the balance in favor of fair use.\n\n"
    description += "#memes #dankmemes #compilation #funny #funnyvideos \n\n"
    f.write(description + "\n\n")
    f.close()
    
    # Step 3: Upload to Youtube
    print("Uploading to Youtube...")
    uploadYtvid(VIDEO_FILE_NAME=outputFile,
                title=title,
                description=description)
    print("Uploaded To Youtube!")
    
    # Step 4: Cleanup
    print("Removing temp files!")
    # Delete all files made:
    #   Folder videoDirectory
    shutil.rmtree(videoDirectory, ignore_errors=True)
    #   File outputFile
    try:
        os.remove(outputFile)
    except OSError as e:  ## if faile,d, report it back to the user ##
        print ("Error: %s - %s." % (e.filename, e.strerror))
    print("Removed temp files!")

def attemptRoutine():
    try:
        routine()
    except OSError as err:
        print("Routine Failed on " + "OS error: {0}".format(err))
        time.sleep(60*60)
        routine()

attemptRoutine()
schedule.every().day.at("19:05").do(attemptRoutine)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one min

