from nltk.corpus import stopwords
import re
stop=stopwords.words('english')
File=open("e:/dist/sentence.txt")
print "Analysing Sentence"
saveFile=open('e:/dist/sentence_processing.txt','w')
N=1
for i in range(N):
    line=File.next().strip()
    s=line.replace('RT','')
    a=s.replace('\\n','')
    c=re.sub(r"http\S+","",a)
    b=c.decode('unicode_escape').encode('ascii','ignore')
    b=b.strip()
    processed_tweet=' '.join(re.sub("(@[A-Za-z0-9]+)|(?:\#+[\w_]+[\w\'_\-]*[\w_]+)|(?:@[\w_]+)|(http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(?:(?:\d+,?)+(?:\.?\d+)?)"," ",b).split())
    for j in processed_tweet.split():
        if j not in stop:
                   saveFile.write(j)
                   saveFile.write(" ")
    
                   

File.close();
saveFile.close()
