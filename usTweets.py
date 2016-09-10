from twitter import  Twitter, OAuth, TwitterHTTPError, TwitterStream                                                          
try:
    import json
except ImportError:
    import simplejson as json
config = {}                                                                                                                   
execfile("config.py" , config)
oauth = OAuth(config["ACCESS_TOKEN"], config["ACCESS_SECRET"], config["CONSUMER_KEY"], config["CONSUMER_SECRET"])
twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.filter(track = "@twitter", country = "United States", countrycode = "US" )
tweet_count =  882
for tweet in iterator:
    tweet_count -= 1
    print json.dumps(tweet)  
    if tweet_count <= 0:
            break 
