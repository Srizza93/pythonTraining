import tweepy
import random

# Get Twitter followers

auth = tweepy.OAuthHandler('YRun9Z8DYsG9z1sRIJlRX2tBi', 'ms5we5o2mp9CZMaOJTa3cXXNcwAObDHwYFCU2AcbnsfwMqE8j1')
auth.set_access_token('1395661604-5yXDKW3Ff5hCVAsfmmqyNnJ3xZBefSzksOzE3In', 'BFpAAtSTqrr05tGH3DhsogsuldmoUsuxGbw9O1ZvbIroY')
API = tweepy.API(auth)

'''users = API.followers()
print([u.name for u in users])
print(len(users))'''
'''try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
'''

followers = API.followers()

# Pick one at random

randomIndex = random.randint(0, len(followers) -1)
randomFollower = followers[randomIndex]
print(randomFollower.screen_name)

# Tweet at the random follower

tweet = "@{} you are the random follower of the day. TURN UP!".format(randomFollower.screen_name)

status = API.update_status(tweet)
print(tweet)
print("Thank's for tweeting!")

# Automation

# Study CRON
# With CRON you can set up the daily time you want to run the program,
# to do this you need to have your computer switched on while the program run.

# To avoid switching on tour computer, you can rent a server for 10$ for two months.
# madeUpByPeople.com/do
