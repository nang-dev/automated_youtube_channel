from moviepy.editor import VideoFileClip, concatenate_videoclips
from moviepy.video.fx.resize import resize
import os
from os.path import isfile, join
import random
import shutil 
from collections import defaultdict

VideoFileClip.resize = resize

def extractAcc(filepath):
    try:
        s = filepath.split("/")[-1].split("-")
        acc = "-".join(s[1:(2+(len(s) - 4))])
        return acc
    except:
        return ""

# generateTimeRange converts float seconds to a range of form @MM:SS
def generateTimeRange(duration, clipDuration):
    preHour = int(duration / 60)
    preMin = int(duration % 60)
    preTime = str(preHour // 10) + str(preHour % 10) + ":" + str(preMin // 10) + str(preMin % 10)

    duration += clipDuration
    postHour = int(duration / 60)
    postMin = int(duration % 60)
    postTime = str(postHour // 10) + str(postHour % 10) + ":" + str(postMin // 10) + str(postMin % 10)

    #return "@" + preTime + " - " + "@" + postTime
    return "@" + preTime
    
# makeCompilation takes videos in a folder and creates a compilation with max length totalVidLength
def makeCompilation(path = "./",
                    introName = '',
                    outroName = '',
                    totalVidLength = 10*60,
                    maxClipLength = 20,
                    minClipLength = 5,
                    outputFile = "output.mp4"):

    allVideos = []
    seenLengths = defaultdict(list)
    totalLength = 0
    for fileName in os.listdir(path):
        
        filePath = join(path, fileName);
        if isfile(filePath) and fileName.endswith(".mp4"):
            print(fileName)
            if os.stat(filePath).st_size < 5000:
                continue

            # Destination path  
            clip = VideoFileClip(filePath)
            clip = clip.resize(width=1920)
            clip = clip.resize(height=1080)
            duration = clip.duration
            print(duration)
            if duration <= maxClipLength and duration >= minClipLength:
                allVideos.append(clip)
                seenLengths[duration].append(fileName)
                totalLength += duration
    
    print("Total Length: " + str(totalLength))

    random.shuffle(allVideos)

    duration = 0
    # Add intro vid
    videos = []
    if introName != '':
        introVid = VideoFileClip("./" + introName)
        videos.append(introVid)
        duration += introVid.duration
    
    description = ""
    # Create videos
    for clip in allVideos:
        timeRange = generateTimeRange(duration, clip.duration)
        acc = extractAcc(clip.filename)
        description += timeRange + " : @" + acc + "\n"
        duration += clip.duration 
        videos.append(clip)
        print(duration)
        if duration >= totalVidLength:
            # Just make one video
            break
    
    # Add outro vid
    if outroName != '':
        outroVid = VideoFileClip("./" + outroName)
        videos.append(outroVid)

    finalClip = concatenate_videoclips(videos, method="compose")

    audio_path = "/tmp/temoaudiofile.m4a"

    #print(description)
    # Create compilation
    finalClip.write_videofile(outputFile, threads=8, temp_audiofile=audio_path, remove_temp=True, codec="libx264", audio_codec="aac")

    return description
    
if __name__ == "__main__":
    makeCompilation(path = "/Users/nathanan/Documents/YOUTUBE/AutomatedChannel/Videos/Memes/",
                    introName = "intro_vid.mp4",
                    outroName = '',
                    totalVidLength = 10*60,
                    maxClipLength = 20,
                    outputFile = "outputseq.mp4")
