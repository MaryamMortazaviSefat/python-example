import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

if soup.title:
    page_title = soup.title.string  
else:
    "عنوان پیدا نشد"


print("عنوان صفحه وب:", page_title)

#---------------------------------------------------------------------

book_titles = []
for item in soup.select(".product_pod h3 a"):
    book_titles.append(item.get("title"))


print("\nلیست عنوان کتاب‌ها:")
for title in book_titles:
    print("-", title)

#---------------------------------------------------------------------

image_links = []
for img in soup.select(".product_pod img"):
    src = img.get("src")
    if src.startswith("../"):
        src = "http://books.toscrape.com/" + src.replace("../", "")
    image_links.append(src)

print("\nلینک‌های تصاویر:")
for link in image_links:
    print("-", link)