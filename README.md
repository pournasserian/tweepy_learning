
# tweepy quick notebook


```python
# install using: pip install tweepy
import tweepy
```

### Authentication


```python
# Step 1 - Authenticate
# copy & paste these values from: https://apps.twitter.com/
consumer_key= 'DjZQINSdfCpZ54nxlG6W5g'
consumer_secret= 'bvMPkOJo65KCXKqNsmCYEXYiGCvXqh1NPI7iMNqR9Q'

access_token='278647040-sgX4F2mbN4xYcfWVmJk6qGaXg8uu7PlfsokyU231'
access_token_secret='Q3EIeuiG0PAoXzSaK6Eyd4gDMD8qTef40yNeddAriw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
```

### Reading home timeline tweets


```python
public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)
```

    RcppTOML 0.1.0 https://t.co/PEwDQ5cVW8 #rstats #DataScience
    Wpf application with real-time data in OxyPlot charts by Illya Reznykov https://t.co/nWnaALyMrm
    Starting the analysis of #McMaster tweets for a demo of analysis with #tyGraph
    @haacked also, "hurry up!"
    If they make a 2hr movie of my life, 1hr 50 mins of it will be me saying "Come on, let's go. Let's go."
    
    #parenting #fb
    Here are some steps when creating a pitch-perfect #elevatorpitch to impress the hiring manager.… https://t.co/e7gJmnEWGN
    #WeekendReading: New Windows 10 devices at CES, Microsoft Connected Vehicle Platform https://t.co/X8LtvLMkQx https://t.co/WgH8ZDTB3h
    RT @miladsafarzadeh: یک اَپ دیگه‌م ریلیز شد. آخرین زلزله‌های #ایران و نواحی با جزئیات کامل مانند محل دقیق #زلزله روی نقشه، بزرگی و عمق.
    
    ht…
    #MSFTConnect Session On Demand: Store app data w/ Azure Data Lake Store, https://t.co/06xC55MxjG no limit, hyper-sc… https://t.co/FVDWYAQ7Zx
    RT @niloofarghadiri: اين بيچاره الان در مراسم خداحافظي اوباما با نيروهاي مسلح، تو مراسم غش كرد افتاد. 
    وضعيت آمريكا https://t.co/4py43Dzi83
    Here are 5 #personalbranding techniques to try when working on your resume. https://t.co/ULgBmTJHds https://t.co/8Dmmd5PgHZ
    RT @arashmil: بچه‌های دیزاین‌وند که همکار راب‌جانوف، طراح لوگوی #اپل در ایران هستن، می‌خوان با کمک دوسداران این لوگو برای تولدش هدیه‌ای بفر…
    RT @cristilmethod: Let's go live to all of Mississippi right now https://t.co/rlgFTzHi5q
    RT @anjuan: If you're a Black person involved in open source software, then I highly recommend applying to attend! https://t.co/rMC5LtJE4u
    We are looking for speakers for Open DEVTEACH focusing on Open Source Web Innovations, Session abstracts by Jan 29t… https://t.co/HgC14EOW2Y
    Azure Backup protects against #ransomware
    https://t.co/SIUYzESLTD
    

### Get the User object for twitter...


```python
# Get the User object for twitter...
user = api.get_user('twitter')
print(user.screen_name)
print(user.followers_count)
```

    Twitter
    58171173
    

### Get friends of the User


```python
for friend in user.friends():
   print(friend.screen_name)
```

    UKMoments
    CanadaMoments
    momentsbrasil
    MomentsAU
    MomentsES
    momentsjapan
    kayvz
    TwitterU
    jointheflockEU
    verified
    TwitterStripes
    periscopetv
    TwitterParents
    btaylor
    IamDebraLee
    Marthalanefox
    hughjohnston
    TwitterPolitica
    TwitterGamingES
    TwitterDetroit
    


```python
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
```


```python
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
```


```python
myStream.filter(track=['python'])

```
