import sys
import json
import time
import praw
import logger

reload(sys)
# sys.setdefaultencoding('unicode_escape')

config = json.loads(open('config.json').read())
reddit = praw.Reddit(client_id=config["client_id"],
                     client_secret=config["client_secret"],
                     user_agent=config["user_agent"],
                     username=config["username"],
                     password=config["password"])
me = reddit.user.me()

def main():
    print "Logged in as user: ", me
    while True:
        try:
            1/0
            submission = reddit.submission('6h6amv')
            submission.comments.replace_more(limit=0)
            comments = submission.comments.list()
            # subreddit = reddit.subreddit('all')
            # comments = subreddit.stream.comments()
            for index, comment in enumerate(comments):
                print index, comment.subreddit, comment.author, comment.body
        except KeyboardInterrupt:
            break
        except Exception as e:
            # traceback.print_exc()
            logger.log(e)
            time.sleep(15)

if __name__ == '__main__':
    main()