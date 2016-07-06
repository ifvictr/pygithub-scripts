#===BEGIN CONFIG===
#What's your username? Yes, the one you log into your account with.
USERNAME = ""
#What about your password? Don't worry, you're safe here.
PASSWORD = ""
#How often do you want to check? Default is every 30 minutes.
CHECK_INTERVAL = 60 * 30
#===END CONFIG===

import github
import time

api = github.Github(USERNAME, PASSWORD)
auser = api.get_user(USERNAME)
nuser = api.get_user()
while True:
    for event in auser.get_public_received_events():
        if event.type == "WatchEvent" and not nuser.has_in_starred(event.repo):
            print "%s starred the repository %s/%s, and so will I." % (event.actor.login, event.repo.owner.login, event.repo.name)
            nuser.add_to_starred(event.repo)
    time.sleep(CHECK_INTERVAL)
