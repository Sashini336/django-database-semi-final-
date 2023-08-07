import requests
from bs4 import BeautifulSoup
import json
import os

def extract_more_information(soup):
    more_information = []

    title_info_div = soup.find_all('div', class_='col-md-12')[3]
    br_elements = title_info_div.find_all('br')
    for br in br_elements:
        info = br.next_sibling.strip()
        more_information.append(info)

    return more_information

def extract_info(soup):
    title = None
    year = None
    millage = None
    fuel_type = None
    transmission = None
    horsepower = None
    engine_liters = None
    doors = None
    color = None

    
    title_element = soup.find('h1', class_='post-title')
    title = title_element.text.strip() if title_element else None

    article_element = soup.find('article', class_='single-vehicle-details')
    row_element = article_element.find('div', class_='row')
    col_md_6_element = row_element.find_all('div', class_='col-md-6')[5]
    row_2_element = col_md_6_element.find_all('div', class_='column')
    
    
    image_elements = col_md_6_element.find_all('div', class_='column')

    for image_element in image_elements:
        image = image_element.find('img', src=True)
        if image:
            image = image['src']
            break

        
    image_urls = []

    for div in row_2_element:
        img_tag = div.find('img')
        if img_tag and 'src' in img_tag.attrs:
            image_url = img_tag['src']
            image_urls.append(image_url)
            
            
    price_element_find = row_element.find_all('div', class_='col-md-6')[2]
    
    
    price_element = price_element_find.find('p', class_='detail-price')
    
    price = price_element.text.strip()
    
    more_information = extract_more_information(soup)

    ul_element = soup.find('div', class_='options-left').find('ul')
    if ul_element:
        li_items = ul_element.find_all('li')

        try:
            year = li_items[0].text.strip()
        except IndexError:
            pass

        try:
            millage = li_items[1].text.strip()
        except IndexError:
            pass

        try:
            fuel_type = li_items[2].text.strip()
        except IndexError:
            pass

        try:
            transmission = li_items[3].text.strip()
        except IndexError:
            pass

    ul_element_right = soup.find('div', class_='options-right').find('ul')
    if ul_element_right:
        li_items_right = ul_element_right.find_all('li')

        try:
            horsepower = li_items_right[0].text.strip()
        except IndexError:
            pass

        try:
            engine_liters = li_items_right[1].text.strip()
        except IndexError:
            pass

        try:
            doors = li_items_right[2].text.strip()
        except IndexError:
            pass

        try:
            color = li_items_right[3].text.strip()
        except IndexError:
            pass
        

    return {
        'title': title,
        'price': price,
        'year': year,
        'millage': millage,
        'fuel_type': fuel_type,
        'transmission': transmission,
        'horsepower': horsepower,
        'engine_liters': engine_liters,
        'doors': doors,
        'color': color,
        'image': image,
        'image_urls': image_urls,
        'moreInformation': more_information
    }

def scrape_single_ad(link):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = requests.get(link, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        info = extract_info(soup)
        return info

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None
    
    
def load_json():
    with open("/Users/a.petkov/Desktop/TrainingGuides/Car/data.json", 'r', encoding='utf-8') as file:
        data = json.load(file)

    scraped_data = []
    for item in data:
        link = item['path']
        info = scrape_single_ad(link)
        if info:
            scraped_data.append(info)
    return scraped_data
            

# def scrape_and_return_data(input_data):
#     scraped_data = []
#     for item in enumerate(input_data, start=1):
#         link = item['path']
#         info = scrape_single_ad(link)
#         if info:
#             scraped_data.append(info)
#     return scraped_data
