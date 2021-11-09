import tweepy
import datetime, time, schedule
from PIL import Image, ImageDraw, ImageFont
import pytz
'''
Set the basic values,
new_time : timezone to check tweets
font : font desired for the image
size : font size
'''
def start_values(new_time, font, size):
    global days, timezone, font_type, last_checked
    timezone = pytz.timezone(new_time)
    font_type = ImageFont.truetype(font,size)

    with open('Days.txt', 'r') as getDays:
        days = int(getDays.readline())
        last_checked = getDays.readline()
        #If it's not the first time running it
        if len(last_checked)>0:
            last_checked = int(last_checked)
        else:
            last_checked = datetime.datetime.now(tz=timezone).day-1
    #Draws the start number
    draw_number(1090, 280)

'''
Twitter api authorization, get your tokens in https://developer.twitter.com/
'''
def twitter_auth(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

'''
Adds a day to the days file, and the last date checked, then draws it
'''
def add_day():
    global days
    with open('Days.txt', 'w') as file:
        file.write(str(days+1)+'\n')
        file.write(str(last_checked))
    with open('Days.txt', 'r') as file:
        days = int(file.readline())
    draw_number(1090, 280)
'''
Draws the number in the original picture and replaces the old one,
updates the twitter banner
'''
def draw_number(x,y):
    image = Image.open('img/Original_TwitterBanner.png')
    draw = ImageDraw.Draw(image)
    # Position to center text if number has less then 3 digits
    position = 50/len(str(days)) if len(str(days)) < 3 else 0
    draw.text(xy=(x+position,y),text=str(days), fill=(35,35,35), font=font_type)
    image.save('img/banner.png')
    api.update_profile_banner('img/banner.png')

'''
Checks the user tweets and looks for #100DaysOfCode in the tweets made in that day
'''
def check_tweets():
    global last_checked
    current_day = datetime.datetime.now(tz=timezone).day
    #Checks last day checked to not be the same
    if(last_checked != current_day):
        #Gets user tweets
        tweets = api.user_timeline(username, count=5, exclude_replies = True, include_rts = False, tweet_mode = "extended")
        for tweet in tweets:
            tweetText = tweet.full_text.upper()
            tweetTime = tweet.created_at - datetime.timedelta(hours=timeoff_set)
            #Check if tweet is in the same day of the current day and if it contains #100DaysOfCode
            if current_day - tweetTime.day  < 1 and '#100DaysOfCode'.upper() in tweetText:
                print(tweetText, tweetTime)
                last_checked = datetime.datetime.now(tz=timezone).day
                add_day()
                break

'''
Add your twitter tokens in the empty string spaces
DO NOT UPLOAD YOUR TOKENS KEEP THEM PRIVATE
'''
if __name__ == '__main__':
    print("Starting 100-Days-Banner")
    days = timezone = font_type = last_checked = None
    # Add Credentials
    username = 'Ingrid_E_'
    timeoff_set = 5
    cKey = ""
    cSecrete = ""
    aToken = ""
    aSecrete = ""
    auth = twitter_auth(cKey,
                        cSecrete,
                        aToken,
                        aSecrete)
    api = tweepy.API(auth)
    start_values('Etc/GMT+5', 'font/CONSOLA.TTF', 90)
    schedule.every(1).minutes.do(check_tweets)
    while True:
        schedule.run_pending()
        time.sleep(1)