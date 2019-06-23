# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:15:43 2019

@author: user
"""
# We need 4 things
# 1. Our keys - kept in our own twitter_credentials
# 2. stream - which is the channel from which all tweets start coming in
# 3. Listener  - listening to the stream kind of like ear to the ground
# 4. OAuthhandler - to use our keys and autheticate our application
from tweepy.streaming import StreamListener
# This contains the authentication for handling tweets
from tweepy import OAuthHandler
# establises the road/channel for data that we need to listen to
from tweepy import Stream
#our own file containing the credentials 
import twitter_credentials
# Now let us go to stdOutListner and see what to do
 
# # # # TWITTER STREAMER # # # #
class TwitterStreamer():
    """
    Class for streaming and processing live tweets.
    """
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        # create a listner object
        listener = StdOutListener(fetched_tweets_filename)
        # autheticate ourselves with these keys
        auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        # create a pipe and connect the pipe to the listener
        # by first creating a pipe i.e Stream - auth it and passing the lsitener to it
        stream = Stream(auth, listener)
        # Now I want to only listens to certain tweets i.e hash tags - so put that filer in into the
        # stream
        # This line filter Twitter Streams to capture data by the keywords: 
        stream.filter(track=hash_tag_list)


# # # # TWITTER STREAM LISTENER # # # #
# This inherits from StreamListner  and allows us to print tweets
# this inherits 2 methods 
# on_data i.e when we get data do somethings
# on_error do something
# for now just print the data that comes in when data is received
# and print a status code when you have an error code
# but before we listen we need to be logged in and create a stream
# all that is nicely put in a class called TwitterStremer
# Lets see what this does.
    
class StdOutListener(StreamListener):
    """
    This is a basic listener that just prints received tweets to stdout.
    """
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename

    # this over riden method gets data and is used for processing 
    # currently we will print out the interest
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
          

    def on_error(self, status):
        print(status)

 
if __name__ == '__main__':
 
    # Authenticate using config.py and connect to Twitter Streaming API.
    # There are more like keyboards
    # the output that you see is a large json object
    hash_tag_list = ["kohli", "dhoni", "K L Rahul", "Hardik Pandya"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)
# when you run this you get a bunch of data all as json object
# wordpad tweets.txt
# go to http://json.parser.online.fr/ and paste the json object
# you can see this in a pretty readable format
# you can then extracts nodes from the json object for processing it

