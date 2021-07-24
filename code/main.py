from instabot import Bot
from config.base import USERNAME, PASSWORD

unfollowers = []

bot = Bot()

bot.login(username = USERNAME, password = PASSWORD)

non_followers = set(bot.following) - set(bot.followers)

for unfollower in non_followers:
    unfollowers.append(bot.get_username_from_user_id(unfollower))

with open("unfollowers.txt", "w") as f:
    # Writing unfollowers to a file
    for unfollower in unfollowers:
        f.writelines(f"{unfollower},\n")
