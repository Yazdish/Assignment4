import getpass
import instaloader

f= open("followers.txt", "r")
old_followers = []
for who in f:
    old_followers.append(who)
f.close()

L = instaloader.Instaloader()

username = input("User Name: ")
password = getpass.getpass("Password: ")

L.login(username, password)

ProfName = input("whose profile you`d like to check? ")
profile = instaloader.profile.from_username(L.context, ProfName)

new_followers = []
for follower in profile.getfollowers():
    new_followers.append(follower)

for unfollower in old_followers:
    if unfollower not in new_followers:
        print(unfollower)

f = open("followers.txt", "w")
for follower in new_followers:
    f.write(follower + "\n")
f.close()




