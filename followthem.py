#===BEGIN CONFIG===
#What's your username? Yes, the one you log into your account with.
USERNAME = ""
#What about your password? Don't worry, you're safe here.
PASSWORD = ""
#How long do you want to pause at a time? Default is 30 seconds.
PAUSE_DURATION = 30
#How many users do you want to follow at a time before we pause? Default is every 50 users.
FOLLOW_AT_A_TIME = 50
#Which user do you want to start following at? If you want to enable this, specify their user id. By default, SINCE_ID is -1 (disabled).
START_ID = -1
#Which user do you want to stop following at? If you want to enable this, specify their user id. By default, FINISH_ID is -1 (disabled).
FINISH_ID = -1
#===END CONFIG===

import github
import sys
import time

api = github.Github(USERNAME, PASSWORD)
auser = api.get_user()
if START_ID > 0:
    since = START_ID - 1
else:
    since = 0
print "Script will start following users with user id %d and beyond." % since
while True:
    count = 0
    for user in api.get_users(since):
        auser.add_to_following(user)
        print "Followed @%s." % user.login
        since = user.id
        if count == (FOLLOW_AT_A_TIME - 1):
            break
        if user.id == FINISH_ID:
            print "Reached specified finish id, exiting script..."
            sys.exit(0)
        count += 1
    print "Pausing for %d seconds..." % PAUSE_DURATION
    time.sleep(PAUSE_DURATION)
