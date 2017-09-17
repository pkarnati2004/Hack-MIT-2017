# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:20:19 2017

@author: Gabe Madonna
"""
from selenium import webdriver
import time

#def read_file(filename):
#    """
#    reads in file as list of lines
#    filename: string
#    returns line: list of strings from file
#    """
#    lines = []
#    with open(filename) as f: 
#        for line in f:
#            line = line.replace("\n", "")
#            lines.append(line)
#    return lines    
#
#songs_file = "C://Users//Gabe Madonna//Google Drive//songs2.txt"
#urls = read_file(songs_file)



driver = webdriver.Chrome("C:/Users/Gabe Madonna/Desktop/chromedriver_win32/chromedriver.exe" )

song = "tik tok"
artist = "kesha"
query = song + " " + artist + " lyrics"

driver.get("https://www.youtube.com/")
youtube_search_box = driver.find_element_by_id("search")
youtube_search_button = driver.find_element_by_id("search-icon-legacy")

youtube_search_box.send_keys(query)
youtube_search_button.click()

youtube_results = driver.find_element_by_id("contents").find_elements_by_css_selector("*")[:15]

for result in youtube_results[:1]:
    for inner_result in result.find_elements_by_css_selector("*"):
        print(inner_result.get_attribute("id"))
        if inner_result.get_attribute("id") == "video-title":
            title = inner_result
            break
    song_block =  inner_result
    if "lyrics" in title.text.lower() and song.lower() in title.text.lower():
        break


song_block.click()


results = driver.find_element_by_id("contents")

time.sleep(2)

url_box = driver.find_element_by_name("url")
url_box.clear()
url_box.send_keys(url)
converts = driver.find_elements_by_class_name("mainbtn")
for c in converts:
    if c.text == "convert":
        c.click()
        break
time.sleep(2)

while True:
    if len(driver.find_elements_by_class_name("btn-success")) > 0:
        continue_btn = driver.find_element_by_class_name("btn-success")
        continue_btn.click()
        break

download_btn = driver.find_element_by_class_name("btn-success")
download_btn.click()
print("downloaded " + url)
successes += 1
time.sleep(5)





























bad_urls = []
successes= 0

for url in urls:
    try:      
        driver.get("http://convert2mp3.net/en/index.php")
        time.sleep(2)
        
        url_box = driver.find_element_by_name("url")
        url_box.clear()
        url_box.send_keys(url)
        converts = driver.find_elements_by_class_name("mainbtn")
        for c in converts:
            if c.text == "convert":
                c.click()
                break
        time.sleep(2)
    
        while True:
            if len(driver.find_elements_by_class_name("btn-success")) > 0:
                continue_btn = driver.find_element_by_class_name("btn-success")
                continue_btn.click()
                break
        
        download_btn = driver.find_element_by_class_name("btn-success")
        download_btn.click()
        print("downloaded " + url)
        successes += 1
        time.sleep(5)
    except:
        bad_urls.append(url)
        print("failed ot download " + url)
    print(str(successes) + " of " + str(len(urls)) + " songs downloaded, " + str(len(bad_urls)) +" errors")
print(bad_urls)

#bad url: https://www.youtube.com/watch?v=OBwS66EBUcY
            