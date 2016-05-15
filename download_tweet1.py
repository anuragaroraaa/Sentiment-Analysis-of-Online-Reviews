from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os


#consumer key, consumer secret, access token, access secret.
ckey="hrSYXHVjIPHzFAsMPpJ2RgW0M"
csecret="yGxoJwCZIsdgVWKlNyP3T2V5t9BlG0VmzUGdRmNvld8zo2j3AS"
atoken="3992271614-7dn4iV2rSWPUGVyS9Mm4NzjieshcpG6h70cUK6u"
asecret="1c1jdylXTZCGrDVVZNdBi5xP27nUThDhMPaZPUMDKSUv7"
fg = open("twitDB46.csv", "w")
fg.truncate()
fg.close()
num_tweets=0
class listener(StreamListener):

    
    def on_data(self, data):

            tweet=data.split(',"text":"')[1].split('","source')[0]
            print"Downloading Tweets..."
            #saveThis=str(time.time())+'::'+tweet
            global num_tweets
            num_tweets += 1
            saveFile=open('twitDB46.csv','a')
            if num_tweets < 51:
                saveFile.write(tweet)
                
                saveFile.write('\n')
                return True
            else:
                return False           
                    
            saveFile.close()
            return(True)
                    
    def on_error(self, status):
            print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
rfile=open('query_term.txt', 'r')
#query_term="bye"
query_term=rfile.read()
#os.remove('twitDB46.csv')
os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"
twitterStream.filter(track=[query_term])
os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"
execfile('analysis.py')

    
