from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
html = page.read().decode("utf-8")
# print(html)

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
# print(title)

import re

# print(re.findall("ab*c", "abc")) 
# print(re.findall("ab*c", "abcac"))
# print(re.findall("ab*c", "ABC"))
# print(re.findall("ab*c", "ABC", re.IGNORECASE))
# print(re.findall("a.c", "abc"))
# print(re.findall("a.c", "abbc"))
# print(re.findall("a.*c", "abbc"))

match_results = re.search("ab*c", "ABC", re.IGNORECASE)
# print(match_results.group())

string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*?>", "RHINOS", string)
# print(string)

#      Exercise: Scrape data from a website
url = "http://olympus.realpython.org/profiles/dionysus"
html_page = urlopen(url)
html = html_page.read().decode("utf-8")

# Liste med det info man gerne vil søge på
targets = ["Favorite Color: ", "Name: ", "Hometown: ", "Favorite animal: "]
for string in targets:
    # Iterer henover listen og find start indexet af texten vi prøver at finde
    string_start_idx = html.find(string)
    text_start_idx = string_start_idx + len(string)

    # find fra texten hen til nærmeste < og brug det til at udregne enden af textens index
    next_html_tag_offset = html[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    # Isoler texten i html stregen og fjern eventuelle mellemrum og lineskift osv.
    raw_text = html[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \t\n\r")
    # print svarene
    print(clean_text)

from bs4 import BeautifulSoup

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
print(soup.title.string)

# Exercise: Parse HTML with Beautiful Soup
url = "http://olympus.realpython.org"
page = urlopen(url + "/profiles")
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

# finder alle links der har noget med profilerne
links = soup.find_all("a")
for link in links:
    # tilføj til hvad der kommer efter "href" til base linket
    link_url = url + link["href"]
    # print svar
    print(link_url)


import mechanicalsoup

browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
login_page = browser.get(url)
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles = browser.submit(form, login_page.url)
print(profiles.url)


# dice roll scraping
browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of your dice roll is: {result}")

import time

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(2)
