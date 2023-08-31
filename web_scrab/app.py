import csv
import requests
from bs4 import BeautifulSoup

# Replace this placeholder URL with the actual Amazon product URL
url = 'https://www.amazon.com/dp/B07H65KP63'

def scrape_product_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extracting product information
        product_title_element = soup.find('span', {'id': 'productTitle'})
        product_title = product_title_element.get_text(strip=True) if product_title_element else "N/A"

        product_price_element = soup.find('span', {'id': 'priceblock_ourprice'})
        product_price = product_price_element.get_text(strip=True) if product_price_element else "N/A"
        
        product_rating_element = soup.find('span', {'class': 'a-icon-alt'})
        product_rating = product_rating_element.get_text(strip=True) if product_rating_element else "N/A"
        
        # Create a dictionary with the extracted information
        product_info = {
            'Title': product_title,
            'Price': product_price,
            'Rating': product_rating
        }
        
        return product_info
    else:
        print("Failed to fetch the page.")
        return None

# Call the function to scrape the product page
product_data = scrape_product_page(url)

if product_data:
    # Writing the scraped data to a CSV file
    csv_filename = "product_info.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        fieldnames = ["Title", "Price", "Rating"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(product_data)

    print("Scraped data has been saved to", csv_filename)




