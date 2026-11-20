
import requests
from bs4 import BeautifulSoup
import csv

print("Starting web scraper...")

url = "https://books.toscrape.com/catalogue/page-1.html"

response = requests.get(url, timeout=15)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

book_data = []

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip()
    availability = book.find(
        "p", class_="instock availability"
    ).text.strip()

    book_data.append([title, price, availability])

with open("books_data.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(["Book Title", "Price", "Availability"])
    writer.writerows(book_data)

print("Scraping completed successfully!")
print("Total books collected:", len(book_data))
print("Data saved in books_data.csv")
