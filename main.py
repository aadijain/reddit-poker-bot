import sys
import json
import time
import praw
import logger

COMMENT_ID = ''
SUBREDDIT_ID = ''

reload(sys)
sys.setdefaultencoding('unicode_escape')


def start(reddit):
    global COMMENT_ID
    print "Logged in as user: ", reddit.user.me()
    logger.log(reddit.user.me(), "Login by: ")
    while True:
        try:
            subreddit = reddit.subreddit('bottest')
            comments = subreddit.stream.comments()
            for comment in comments:
                COMMENT_ID = comment.id
                if comment.author == reddit.user.me():
                    continue
                st = comment.body
                print st
                if str(st) == 'GO!':
                    logger.log('TRIGGERED')
                    comment.reply('TRIGGERED')
        except KeyboardInterrupt:
            print "Stopping..."
            logger.log('Manual Stop of ' + str(reddit.user.me()))
            break
        except praw.exceptions.APIException as e:
            print "Praw API Error..."
            logger.log(e, COMMENT_ID)
            if str(e.field) == 'ratelimit':
                time.sleep(5*60)
            else:
                time.sleep(15)
        except Exception as e:
            print "Error..."
            logger.log(e)
            time.sleep(15)

if __name__ == '__main__':
    config = json.loads(open('config.json').read())
    redditBOT = praw.Reddit(client_id=config["client_id"],
                            client_secret=config["client_secret"],
                            user_agent=config["user_agent"],
                            username=config["username"],
                            password=config["password"])
    #sample_bot
    start(redditBOT)