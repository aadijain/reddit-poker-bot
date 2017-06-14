import praw
import auth

reddit = praw.Reddit(client_id=auth.client_id,
                     client_secret=auth.client_secret,
                     user_agent=auth.user_agent,
                     username=auth.username,
                     password=auth.password)

print(reddit.user.me())