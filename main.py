import requests
from send_email import send_email

# API Key from newsapi.org
api_key = "5b552bb0035242d9a79f228899187725"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-03-23&sortBy=publishedAt&apiKey=5b552bb0035242d9a79f228899187725"

# Return as json() to get Dictionary!
request = requests.get(url)
content = request.json()

# Access article Titles
for article in content["articles"]:
    print(article['title'])

send_email("test message again")