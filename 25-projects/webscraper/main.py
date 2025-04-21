import requests
from bs4 import BeautifulSoup as bs

github_user = input("Input GitHub User: ")
url = "https://github.com/" + github_user
r = requests.get(url)
soup = bs(r.content, "html.parser")

img_tag = soup.find("img", class_="avatar-user")

if img_tag and "src" in img_tag.attrs:
    profile_image = img_tag["src"]
    print("Profile image URL:", profile_image)
else:
    print("❌ Profile image not found. The username may be incorrect or GitHub layout has changed.")
