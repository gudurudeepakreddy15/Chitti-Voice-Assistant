import webbrowser
import urllib.parse
import difflib


# ==========================================================
# WEBSITES
# ==========================================================

WEBSITES = {

    "youtube": "https://www.youtube.com",

    "chatgpt": "https://chatgpt.com",

    "google": "https://www.google.com",

    "github": "https://github.com",

    "w3schools": "https://www.w3schools.com",

    "leetcode": "https://leetcode.com",

    "geeksforgeeks": "https://www.geeksforgeeks.org",

    "linkedin": "https://www.linkedin.com",

    "instagram": "https://www.instagram.com",

    "facebook": "https://www.facebook.com",

    "whatsapp": "https://web.whatsapp.com",

    "gmail": "https://mail.google.com",

    "python": "https://www.python.org",

    "stackoverflow": "https://stackoverflow.com",

    "reddit": "https://www.reddit.com",

    "amazon": "https://www.amazon.in",

    "flipkart": "https://www.flipkart.com",

    "netflix": "https://www.netflix.com",

    "wikipedia": "https://www.wikipedia.org",

    "spotify": "https://open.spotify.com",

    "discord": "https://discord.com",

    "microsoft": "https://www.microsoft.com",

    "twitter": "https://x.com",

    "x": "https://x.com"
}


# ==========================================================
# WEBSITE ALIASES
# ==========================================================

WEBSITE_ALIASES = {

    "you tube": "youtube",
    "you to": "youtube",

    "chat gpt": "chatgpt",
    "chat g p t": "chatgpt",

    "w three schools": "w3schools",
    "w 3 schools": "w3schools",

    "geeks for geeks": "geeksforgeeks",
    "geeks for geek": "geeksforgeeks",

    "stack overflow": "stackoverflow",

    "linked in": "linkedin",

    "face book": "facebook",

    "insta": "instagram",

    "whatsapp web": "whatsapp",

    "git hub": "github",

    "lead code": "leetcode",

    "flip cart": "flipkart",

    "net flix": "netflix",

    "wiki pedia": "wikipedia",

    "spotty five": "spotify",

    "micro soft": "microsoft"
}


# ==========================================================
# NORMALIZE WEBSITE NAME
# ==========================================================

def normalize_website_name(text):

    text = text.lower().strip()

    if text in WEBSITE_ALIASES:

        return WEBSITE_ALIASES[text]

    if text in WEBSITES:

        return text

    return None


# ==========================================================
# FIND WEBSITE
# ==========================================================

def find_website(text):

    text = text.lower().strip()

    # Direct match
    website = normalize_website_name(text)

    if website:

        return website

    # Check if website name exists inside command
    for name in WEBSITES:

        if name in text:

            return name

    # Check aliases
    for alias, name in WEBSITE_ALIASES.items():

        if alias in text:

            return name

    # Fuzzy matching
    words = text.split()

    for word in words:

        matches = difflib.get_close_matches(
            word,
            WEBSITES.keys(),
            n=1,
            cutoff=0.75
        )

        if matches:

            return matches[0]

    return None


# ==========================================================
# OPEN WEBSITE
# ==========================================================

def open_website(website_name):

    website = find_website(website_name)

    if website is None:

        return False

    url = WEBSITES[website]

    webbrowser.open(url)

    return True


# ==========================================================
# OPEN URL
# ==========================================================

def open_url(url):

    if not url.startswith("http"):

        url = "https://" + url

    webbrowser.open(url)

    return True


# ==========================================================
# GOOGLE SEARCH
# ==========================================================

def google_search(query):

    query = query.strip()

    if not query:

        return False

    encoded_query = urllib.parse.quote_plus(query)

    url = (
        "https://www.google.com/search?q="
        + encoded_query
    )

    webbrowser.open(url)

    return True