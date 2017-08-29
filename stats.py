import sys
import json
import collections
import time
import praw
import logger

reload(sys)
sys.setdefaultencoding('unicode_escape')

def const(value):
    return lambda: value

def start(reddit):
    print "Logged in as user: ", reddit.user.me()
    total = 0
    count = collections.defaultdict(const(0))
    while True:
        try:
            subreddit = reddit.subreddit('all')
            comments = subreddit.stream.comments()
            for comment in comments:
                count[comment.subreddit] += 1
                total += 1
                print "%s:  %f%%  %d/%d"%(comment.subreddit, count[comment.subreddit]*100.0/total, count[comment.subreddit], total)
        except KeyboardInterrupt:
            print "Stopping..."
            logger.dump(count)
            break
        except Exception as e:
            print "Error..."
            logger.log(e)
            time.sleep(15)

if __name__ == '__main__':
    config = json.loads(open('config.json').read())
    reddit = praw.Reddit(client_id=config["client_id"],
                         client_secret=config["client_secret"],
                         user_agent=config["user_agent"],
                         username=config["username"],
                         password=config["password"])
    #sample_bot
    reddit.read_only = True
    start(reddit)