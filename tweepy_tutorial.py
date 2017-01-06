#Import the necessary methods from tweepy library
import tweepy
import json

# Step 1 - Authenticate
consumer_key= 'DjZQINSdfCpZ54nxlG6W5g'
consumer_secret= 'bvMPkOJo65KCXKqNsmCYEXYiGCvXqh1NPI7iMNqR9Q'

access_token='278647040-sgX4F2mbN4xYcfWVmJk6qGaXg8uu7PlfsokyU231'
access_token_secret='Q3EIeuiG0PAoXzSaK6Eyd4gDMD8qTef40yNeddAriw'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):
        tweet = json.loads(data)

        print(tweet['text'])
        
        return True

    def on_error(self, status):
        print(status)


#This handles Twitter authetification and the connection to Twitter Streaming API
l = StdOutListener()
stream = tweepy.Stream(auth, l)

#This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
stream.filter(track = ["من", 'تو','است','ما','یک','او','و','ی'], languages=["fa"])