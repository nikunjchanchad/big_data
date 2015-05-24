import tweepy
import pandas as pd
import matplotlib.pyplot as plt



consumer_key = "e5y3bEkSNqv571ZJdnosGragb" 
consumer_secret = "vPIBsIOn2wlzpxoPAyEKSibovbNVGUYtw83E56gE3TA4nQg8I1"

auth = tweepy.OAuthHandler(consumer_key=consumer_key, consumer_secret=consumer_secret)

api = tweepy.API(auth)


def print_tweet(tweet):
    print "@%s - %s (%s)" % (tweet.user.screen_name, tweet.user.name, tweet.created_at)
    print tweet.text

results = []
for tweet in tweepy.Cursor(api.search, q='', geocode='40.8020712,-124.1636729,10mi').items(1000):
    results.append(tweet)

print "Number of Tweets: ", len(results)                                                                                                                            
for tweet in results:
    print_tweet(tweet)


#tweet=results[2]

'''
for param in dir(tweet):
    if not param.startswith("_"):
        print "%s : %s" % (param, eval("tweet." + param))



'''
'''
def process_results(results):
    id_list = [tweet.id for tweet in results]
    data_set = pd.DataFrame(id_list, columns=["id"])
'''

    # Processing Tweet Data
'''
    data_set["text"] = [tweet.text for tweet in results]
    data_set["created_at"] = [tweet.created_at for tweet in results]
    data_set["retweet_count"] = [tweet.retweet_count for tweet in results]
    data_set["favorite_count"] = [tweet.favorite_count for tweet in results]
    data_set["source"] = [tweet.source for tweet in results]

    # Processing User Data
    data_set["user_id"] = [tweet.author.id for tweet in results]
    data_set["user_screen_name"] = [tweet.author.screen_name for tweet in results]
    data_set["user_name"] = [tweet.author.name for tweet in results]
    data_set["user_created_at"] = [tweet.author.created_at for tweet in results]
    data_set["user_description"] = [tweet.author.description for tweet in results]
    data_set["user_followers_count"] = [tweet.author.followers_count for tweet in results]
    data_set["user_friends_count"] = [tweet.author.friends_count for tweet in results]
    data_set["user_location"] = [tweet.author.location for tweet in results]

    return data_set
data_set = process_results(results)

sources = data_set["source"].value_counts()[:5][::-1]

plt.barh(xrange(len(sources)), sources.values)
plt.yticks(np.arange(len(sources)) + 0.4, sources.index)
plt.show()
'''
