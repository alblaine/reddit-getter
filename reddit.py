
# coding: utf-8

# ### This notebook uses Python and the Reddit API to get data from a subreddit forum.

# #### Step 1: Create a Reddit account at https://www.reddit.com/.

# #### Step 2: Create and register your new app.
# Instructions:
# * Go to this site: https://ssl.reddit.com/prefs/apps/
# * Provide information to register a new app. If you don't know what callback url to use, provide http://www.google.com
# * Save your app
# * Keep this tab open. You are going to need some information about your app to continue

# #### Step 3: write Python code to connect to the Reddit API. Put the id and secret information from your new app here.

import praw

# you have to create an app and put in your own data
reddit = praw.Reddit(client_id='your id here',
                     client_secret='your secret here',
                     user_agent='your user-agent here')


# #### Step 4: create a subreddit instance. Put the subreddit forum name inside the parentheses.

# create a subreddit instance with subreddit forum name in parentheses
subreddit = reddit.subreddit('ccna')


# #### Step 5: get the data in json format and write it to a text file called 'data.txt'. This file will be saved in whatever directory this notebook file is in.


import json
list_of_posts = []
comment_section = {}
comment_info ={}


# specify which fields you want to get from Reddit posts
fields = ('title', 'url', 'selftext', 'score', 'created_utc', 'num_comments')

# to get the most data you can, set limit=none. 
for submission in reddit.subreddit('dataviz').hot(limit=500):

    for index, comment in enumerate(submission.comments):
        post = vars(submission)
        value = comment.body
        key = "comment"
        comment_info[key] = value
        comment_section.update(comment_info)

        labeled_post = {field:post[field] for field in fields}
        labeled_post.update(comment_section)
        list_of_posts.append(labeled_post)


posts_string = json.dumps(list_of_posts)

# convert the data to json format
posts_converted = json.loads(posts_string)


# write the data to files named 'data.txt' and 'comments.txt' in the same directory
with open('posts.txt', 'w') as outfile:
    json.dump(posts_converted, outfile)
