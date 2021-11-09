# 100DaysOfCode - Automatic Banners 👩‍💻
Adds a number to your twitter banner indicating the number of days you have in the #100DaysOfCode challenge

![image](https://user-images.githubusercontent.com/62229851/140855989-313c8db3-79a5-488d-bb16-b6f321529e95.png)

# Set Up

Create a banner picture with a space for the numbers to be at.

![Original](https://github.com/Ingrid-E/RealTime-100DaysOfCode-TwitterBanner/blob/main/img/Original_TwitterBanner.png)

Change x and y position where the number will be drawn.

```python
def draw_number(x,y):
    image = Image.open('img/Original_TwitterBanner.png')
    draw = ImageDraw.Draw(image)
    # Position to center text if number has less then 3 digits
    position = 50/len(str(days)) if len(str(days)) < 3 else 0
    draw.text(xy=(x+position,y),text=str(days), fill=(35,35,35), font=font_type)
    image.save('img/banner.png')
    api.update_profile_banner('img/banner.png')
```
In __main__ add your information

```python
    username = ""
    cKey = ""
    cSecrete = ""
    aToken = ""
    aSecrete = ""
```
To get the Twitter Tokens you need to apply for a Twitter Developer account https://developer.twitter.com/

When your done you just run the script, and keep it running!

```
> python 100-Banners.py
```

# Follow me in twitter!
@Ingrid_E_

Dont forgive to give a ⭐
