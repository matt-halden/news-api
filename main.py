import requests
from send_email import send_email

# API Key from newsapi.org, added "&language=en" to url to add that endpoint in the NewsAPI docs
topic = "tesla"
api_key = "5b552bb0035242d9a79f228899187725"
url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
        "from=2024-03-23&sortBy=publishedAt&" \
        "apiKey=5b552bb0035242d9a79f228899187725&" \
        "language=en"

# Return as json() to get Dictionary!
request = requests.get(url)
content = request.json()

# Access article Titles
body = ""
for article in content["articles"][0:20]:
    # Check if title or description is None and replace it with an empty string
    title = article["title"] if article["title"] is not None else ""
    description = article["description"] if article["description"] is not None else ""
    body += ("Subject: Today's News"
             + "\n" + title + "\n" + description
             + "\n" + article["url"] + 2*"\n")

    # if article["title"] is not None:
        # body += article["title"] + "\n" + article["description"] + 2*"\n"

# Encode body to right format for SMTP lib
body = body.encode("utf-8")
send_email(message=body)
print("done")
