# Fully Automated Youtube Channel

Code to run a fully automated youtube that can scrape content, edit a compilation, and upload to youtube daily. \
Read about it here: https://medium.com/@nathan_149/making-a-fully-automated-youtube-channel-20f2fa57e469

# Instructions

1. [Download](https://github.com/nathan-149/automated_youtube_channel/archive/refs/heads/master.zip) the Github Repository

2. Download and install [Python3](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/) if necessary.

3. Install libraries with `pip3 install -r requirements.txt` or `python3 -m pip install -r requirements.txt` .

4. Get setup and create a Project with the Youtube API: https://developers.google.com/youtube/v3/quickstart/python
Be sure to follow it carefully, as it won't work if you don't do this part right.
Download your OATH file and name it as "googleAPI.json" in your project folder.

6. Create an instagram account and follow accounts you want to scrape from

7. Open config.py in a text editor and fill in instagram credentials

- Note that you can edit variables inside main.py in a text editor and things such as MAX_CLIP_LENGTH.

8. In terminal/cmd, run `instalooter login` and `instaloader --login {YOUR_USERNAME}`. Follow the instructions to login.

9. Run `python3 main.py` in your computer terminal (terminal or cmd). You have to sign in to your Youtube Account through the link the script will give you. It's going to ask you: "Please visit this URL to authorize this application:..." so you copy that link, paste it in your browser, and then sign into your Google account. Then paste the authentication code you get back into your terminal. It will then say "Starting Scraping" and sign into your instagram account.

10. Enjoy your fully automated youtube channel! :) Note that for uploading public videos, you have to complete an audit for the Youtube API. See the note in the [Google Documentation](https://developers.google.com/youtube/v3/docs/videos/insert). Without this, you can only post private videos, but they approve everyone. Have fun!
