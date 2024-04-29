import re
from lib.configure import PLACEHOLDER
from lib.configure import getCustomUrl as URL
from lib.configure import getSite as SITE

# Site URLs
URLS = {
    1: URL(),
    2: "https://api.mojang.com/users/profiles/minecraft/%s",
    3: "https://api.twitter.com/i/users/username_available.json?username=%s",
    4: "https://www.instagram.com/accounts/web_create_ajax/attempt/",
    5: "https://steamcommunity.com/id/%s",
    6: "https://steamcommunity.com/groups/%s",
    7: "https://soundcloud.com/%s",
    8: "https://passport.twitch.tv/usernames/%s",
    9: "https://mixer.com/api/v1/channels/%s",  # Mixer is defunct, consider removing
    10: "https://github.com/%s",
    11: "https://about.me/%s",
    12: "https://youtube.com/c/%s",
    13: "http://pastebin.com/u/%s",
    14: "https://facebook.com/%s",
    15: "https://linkedin.com/in/%s",
    16: "https://tiktok.com/@%s",
    17: "https://snapchat.com/add/%s",
    18: "https://reddit.com/user/%s",
    19: "https://pinterest.com/%s",
    20: "https://discord.com/users/%s"
}

def replace(word):
    # Finds and replaces matches of the name variable with the actual word to insert in URL
    if SITE() == 1:
        x = re.sub(PLACEHOLDER, word, URLS[1])
        return x
    else:
        return URLS[SITE()] % word
