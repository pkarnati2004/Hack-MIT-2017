# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 11:20:19 2017

@author: Gabe Madonna
"""
from selenium import webdriver
import time

def download_song(song, artist = ""):
    print("Finding song...")
    
    driver = webdriver.Chrome("C:/Users/Gabe Madonna/Desktop/chromedriver_win32/chromedriver.exe" )
    driver.set_window_position(10, 700)
    query = (song + " " + artist + bool(len(artist)) * " " + "lyrics").replace(" ", "+")
    driver.get("https://www.youtube.com/results?search_query=" + query)
    
    time.sleep(3)
    youtube_results = driver.find_elements_by_id("dismissable")[:15]
#    for result in youtube_results:
#        print(result)
#    for inner_result in result.find_elements_by_css_selector("*"):
#        print(inner_result.get_attribute("id"))
#        if inner_result.get_attribute("id") == "video-title":
#            title = inner_result
#            break
#    song_block =  inner_result
#    if "lyrics" in title.text.lower() and song.lower() in title.text.lower():
#        break
    youtube_results[0].click()
    print("Found song")
    print("Downloading song...")
    url = driver.current_url
    
    if download_url(url):
        print("Downloaded")
    else:
        print("failed to download")
    driver.close()
    driver.quit()
    return None

def download_url(url):
#    try:   
    driver = webdriver.Chrome("C:/Users/Gabe Madonna/Desktop/chromedriver_win32/chromedriver.exe" )
    driver.get("http://convert2mp3.net/en/index.php")
    driver.set_window_position(10, 700)
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
    
    time.sleep(5)
    download_btn = driver.find_element_by_class_name("btn-success")
    download_btn.click()
    time.sleep(5)
    return True
#    except:
#        driver.close()
#        driver.quit()
#        return False

download_song("time", "hans zimmer")
            