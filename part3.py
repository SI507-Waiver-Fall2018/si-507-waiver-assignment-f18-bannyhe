# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

# Print out the header line
print("Michigan Daily - Most Read Stories")
# Make html request to url
url = "https://www.michigandaily.com"
html = requests.get(url).text
# Parse the information by BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Create a dictionary to store information of stories
storyInfo = {}

# Get titles and links to stories
for link in soup.find_all(class_="pane-mostread"):
    for a in link.find_all("a", href=True):
        storyInfo[a.contents[0]] = a["href"]

# Use the story link to get the author and overwrite the link with the author
for story in storyInfo:
    soup = BeautifulSoup(requests.get(url + storyInfo[story]).text, "html.parser")
    for a in link.find_all("a"):
        storyInfo[story] = a.contents[0]

# Print out the most read stories
for storyTitle, author in storyInfo.items():
    print(storyTitle)
    print(" by", author)
