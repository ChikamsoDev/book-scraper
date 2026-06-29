import requests
import csv
from bs4 import BeautifulSoup
import time

def main():
    # open file once   
    with open("full_site.csv", "w", newline= "", encoding="utf-8") as file:
        # write header
        writer = csv.writer(file)
        writer.writerow(["title", "price"])
        # loop pages 1-50 
        for n in range(1, 51):
            # fetch page using .get
            response = requests.get(f"https://books.toscrape.com/catalogue/page-{n}.html", timeout=10)
            # check status
            response.raise_for_status()
            # parse with BeautifulSoup
            soup = BeautifulSoup(response.text, "lxml")
            # find all articles
            all_articles = soup.find_all("article", class_="product_pod")
            # loop articles
            for article in all_articles:
                # extract title and price
                price = article.find("p", class_="price_color")
                anchor_tag = article.find("h3").find("a")
                title = anchor_tag["title"]
                # write row
                writer.writerow([title, price.text])
                print(f"{title} | {price.text}")
            # after each iteration finishes a page it stalls for 1 sec because if it doesn't it comes off as a bot attack but if it finishes 1 page per second it acts like a human scrapping this process is called polite scraping
            time.sleep(1)
            
if __name__ == "__main__":
    main()