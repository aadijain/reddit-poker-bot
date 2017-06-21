import sys
import json
import traceback
import time
import praw

reload(sys)
sys.setdefaultencoding('unicode_escape')

config = json.loads(open('config.json').read())
reddit = praw.Reddit(client_id=config["client_id"],
                     client_secret=config["client_secret"],
                     user_agent=config["user_agent"],
                     username=config["username"],
                     password=config["password"])
me = reddit.user.me()

def extract():
    while True:
        try:
            # submission = reddit.submission('6h6amv')
            # submission.comments.replace_more(limit=0)
            # comments = submission.comments.list()
            subreddit = reddit.subreddit('all')
            comments = subreddit.stream.comments()
            for index, comment in enumerate(comments):
                print index, comment.subreddit, comment.author, comment.body
        except KeyboardInterrupt:
            break
        except:
            traceback.print_exc()
            time.sleep(15)

def main():
    print "Logged in as user: ", me
    extract()

if __name__ == '__main__':
    main()