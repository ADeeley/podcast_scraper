#------------------------------
# Podcast scraper v 0.1
# by Adam Deeley
# ------------------------------

import urllib.request
import shutil
import os
from bs4 import BeautifulSoup

# tests if the directory exists, if not Python creates the dirctory.
if not os.path.exists("c:\\users\\adam\\music\\podcasts\\"):
    os.mkdir("c:\\users\\adam\\music\\podcasts\\")

destination_dir = "c:\\users\\adam\\music\\podcasts\\"
source = "http://10ghost.net/ProgrammingThrowdown/"
links = []
clean_links =[]

# pulls html from the link provided
html = urllib.request.urlopen(source)
soup = BeautifulSoup(html, "html.parser")

# finds all the links in the soup
for link in soup.findAll("a"):
    links.append(link.get("href"))

    
# cleans up the links and provides a new list (clean_links) with only the links with
# the file extension or phrase given
for link in links:
    if ".mp3" in link:
        clean_links.append(link)
        
# asks user to confirm if all files are to be downloaded. If user types a file name
# then this will be deleted from list, typing “go” starts the download, “abort” quits
# the session.
while True:
 
    choice = input("To proceed with the download, type 'go'.Tto quit, type 'quit'." 
                         "For more options type 'more'. \n> ")    
    if choice == "go":
        break
    elif choice == "quit":
        raise SystemExit
    else:
        pass
        
# loops through each link in links and downloads the .mp3  file using shutil
# currently out of loop during design.
podcast_flo = urllib.request.urlopen(source+clean_links[0]) # file like object
destination_flo = open(destination_dir+clean_links[0], "wb") # file like object
shutil.copyfileobj(podcast_flo, destination_flo)
podcast_flo.close()
destination_flo.close()
destination_flo.close()
  