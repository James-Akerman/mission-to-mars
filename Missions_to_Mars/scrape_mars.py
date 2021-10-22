#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape():
    results_list = []
    
    # Scrape data from the 'Red Planet Science' website
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://redplanetscience.com/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_='article_teaser_body').get_text()
    browser.quit()
    #Append result to results list
    results_list.append([news_title,news_p])
    
    # Scrape data from the 'Space Images Mars' website
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    featured_image = soup.find('img', class_='headerimage fade-in')
    featured_image_url = url + featured_image['src']
    browser.quit()
    #Append result to results list
    results_list.append(featured_image_url)
    
    # Scrape data from the 'Galaxy Facts Mars' website
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    planet_profile_table = tables[0]
    planet_profile_table = planet_profile_table.rename(columns={0:"Mars",1:"Earth"})
    planet_profile_table_html_string = planet_profile_table.to_html()
    #Append result to results list
    results_list.append(planet_profile_table_html_string)
    
    # Scrape data from the 'Mars Hemispheres' website
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://marshemispheres.com/"
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    hemispheres = soup.find_all('div', class_='item')
    browser.quit()
    hemisphere_image_urls = []
    
    for hemisphere in hemispheres:
        hemisphere_image_src = hemisphere.find('img', class_='thumb')['src']
        hemisphere_image_url = url + hemisphere_image_src
        hemisphere_title = hemisphere.find('h3').get_text()
        hemisphere_image_urls.append({'title':hemisphere_title, 'image_url':hemisphere_image_url})
    #Append result to results list
    results_list.append(hemisphere_image_urls)
    
    return results_list
