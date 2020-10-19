from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
import time
import csv 
import requests
import re
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions
import kinter as k

def contruct_url(zip_code):
	url = "https://www.fandango.com/"
	url = url + str(zip_code)
	url = url + "_movietimes?mode=general&q="
	url = url + str(zip_code)
	url = url + "&filter=open-theaters"	

	return url

def find_times_helper(movie, zip_code, dr,web_url,start_t,end_t):
	results = {}
	dr.get(web_url)

	time.sleep(2)
	dr.find_element_by_xpath('//*[@id="covid-modal"]/div/div/div[2]/button').click()

	theater_name_wrap = dr.find_elements_by_class_name("fd-theater")
	for x in theater_name_wrap:
		theater_name = (x.find_element_by_class_name("fd-theater__header"))\
						.find_element_by_tag_name('a').get_attribute("text")

		movies_in_theater = (x.find_element_by_tag_name("ul"))\
							.find_elements_by_class_name("fd-movie")

		for m in movies_in_theater:
			try:
				movie_name = ((m.find_element_by_class_name("dark")).get_attribute("text")).upper()
				if movie_name == movie:
					# print("Theater name: " + theater_name)
					# print(movie_name)

					try:
						time_list = m.find_elements_by_class_name("fd-movie__btn-list-item")
						for t in time_list:
							show_time = t.text
							reformatted_time = reformat_times(reformat_show_time(show_time))
							print(reformatted_time,start_t,end_t)
							if theater_name not in results:
								if (reformatted_time >= start_t and reformatted_time <= end_t) or (start_t == end_t):
									results[theater_name] = [show_time]
							else:
								if (reformatted_time >= start_t and reformatted_time <= end_t) or (start_t == end_t):
									results[theater_name].append(show_time)
							# print(show_time)
					except NoSuchElementException:
						pass
			except NoSuchElementException: 
				pass
	return results

def find_times(movie, zip_code,start_t,end_t):
	test = "https://www.fandango.com/94587_movietimes?mode=general&q=94587&filter=open-theaters"
	movie_theaters_nearby = []
	movie_times = []
	web_url = contruct_url(zip_code)

	chromedriver_location = "/Users/thomaswan/desktop/Project/movie/chromedriver"
	browser = webdriver.Chrome(chromedriver_location)

	return find_times_helper(movie,zip_code, browser,web_url,\
		reformat_times(start_t),reformat_times(end_t)) 

def reformat_show_time(movie_t):
	if movie_t == "":
		return ""

	movie_t = str(movie_t)
	time_return = ""
	if(movie_t[len(movie_t)-1] == 'p'):
		time_return = movie_t[:len(movie_t)-1] + "PM"
	else:
		time_return = movie_t[:len(movie_t)-1] + "AM"

	return time_return

def reformat_times(time_change):
	time_change1 = time_change
	index_of_colon = time_change.find(':')
	hour = time_change[:index_of_colon]
	minutes = time_change[index_of_colon+1: len(time_change)-2]
	meridiem = time_change[len(time_change)-2:len(time_change)]

	if(hour == "12"):
		if(meridiem == "AM"):
			if(minutes == "00"):
				return 0
			else:
				return int(minutes)

		elif(meridiem == "PM"):
			if(minutes == "00"):
				return int(24 * 100)
			else:
				return int(str(24)+minutes)
 
	else:
		if(meridiem == "AM"):
			if(minutes == "00"):
				time_change = str(int(hour) * 100)
			else:
				time_change = hour + minutes
		elif(meridiem == "PM"):
			if(minutes == "00"):
				time_change = str((int(hour)+12) * 100)
			else:		
				time_change = str(int(hour)+12) + minutes
	return int(time_change)


# def main():
# 	print(reformat_times("1:01PM"))
# 	print(reformat_times( "11:00AM"))

# 	print(reformat_show_time("8:00p"))
# # 	find_times(user_movie, user_zip_code)


# if __name__ == "__main__":
# 	main()




