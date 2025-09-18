from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.iranketab.ir/"
driver=webdriver.Chrome()
driver.get(url)

WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.CLASS_NAME, "book-item__title"))
)

html=driver.page_source
soup = BeautifulSoup(html, "html.parser")

#---------------------------------------------------------------------

if soup.title:
    page_title = soup.title.string  
else:
    "عنوان پیدا نشد"


print("عنوان صفحه وب:", page_title)

#---------------------------------------------------------------------

book_titles = []
for item in soup.select(".book-item__title"):
    book_titles.append(item.get_text(strip=True))


print("\nلیست عنوان کتاب‌ها:")
for title in book_titles:
    print("-", title)

#---------------------------------------------------------------------

image_links = []
for img_tag in soup.select(".book-item__image img"):
    src = img_tag.get("src")
    if src and src.startswith("/"):
        src = "https://www.iranketab.ir" + src  
    image_links.append(src)


print("\nلینک‌های تصاویر:")
for link in image_links:
    print("-", link)