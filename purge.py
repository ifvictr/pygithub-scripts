#===BEGIN CONFIG===
#What's your username? Yes, the one you log into your account with.
USERNAME = ""
#What about your password? Don't worry, you're safe here.
PASSWORD = ""
#Do you want to purge your followers, following, or starred? 0 = followers (not supported), 1 = following, 2 = starred repositories, 3 = repos, 4 = gists
MODE = 0
#===END CONFIG===

import github
import sys

api = github.Github(USERNAME, PASSWORD)
auser = api.get_user()
if MODE == 0: #Purge followers (currently not supported)
    print "Can't do this, GitHub API doesn't let us yet... :("
elif MODE == 1: #Purge following
    for user in auser.get_following():
        auser.remove_from_following(user)
        print "Unfollowed @%s." % user.login
elif MODE == 2: #Purge starred repositories
    for repo in auser.get_starred():
        auser.remove_from_starred(repo)
        print "Unstarred repo %s/%s." % (repo.owner.login, repo.name)
elif MODE == 3: #Purge repos
    for repo in auser.get_repos():
        repo.delete()
        print "Deleted repo %s/%s." % (repo.owner.login, repo.name)
elif MODE == 4: #Purge gists
    for gist in auser.get_gists():
        gist.delete()
        print "Deleted gist %s/%s." % (gist.owner.login, gist.id)
else: #Not valid
    print "Unknown mode specified, terminating..."
    sys.exit(1)
