from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import pandas 
from datetime import date

def get_html_from_source():
    url = "https://covidtracking.com/data/download"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    # Create a request with headers
    request = urllib.request.Request(url, headers=headers)

    # Open the URL with the request
    content = urllib.request.urlopen(request)

    # Process the content using BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")
    
    only_href = [tag['href'] for tag in soup.find_all('a', href=lambda href: href and href.lower().endswith(".csv"))] 
    formatted_url = []
    for url in only_href:
        formatted_url.append("https://covidtracking.com/" + url)
 
    return formatted_url

def download_zips_and_unzip():
    urls_list = get_html_from_source()
    curr_date = 'covid__history/'
    os.makedirs(curr_date, exist_ok=True)
    
    for url in urls_list:
        try:
            response = requests.get(url)
            split_name = str(url).split('/')
            zip_name_compress = curr_date+ split_name[-1]
    
            with open(zip_name_compress, 'wb') as zip_file:
                zip_file.write(response.content)

        except requests.RequestException as e:
            print(f"Error downloading or processing URL {url}: {e}")
            
        except (OSError, ValueError):
            continue   
        
        except Exception as e:
            print(f"An error occurred: {e}")
            
            
download_zips_and_unzip()