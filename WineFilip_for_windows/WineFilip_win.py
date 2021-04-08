from selenium import webdriver

options = webdriver.ChromeOptions() 
options.add_argument("--user-data-dir=ChromeUser/") #Path to your chrome profile
options.add_argument('--disable-blink-features=AutomationControlled')

chromedriver = "path_with_driver/chromedriver"
browser = webdriver.Chrome(chromedriver, options=options)

browser.get('https://old.systembolaget.se/webblansering')

logged_in = False
while not logged_in:
	browser.implicitly_wait(10)

	

	login_box = browser.find_element_by_class_name("sb-nav-row2-container")
	print(login_box)
	browser.implicitly_wait(10)

	try:
		if not "LOGGA IN" in login_box.text:
			print(login_box.text)
			logged_in = True
	except:
		logged_in = True

booked = False

if logged_in:
			
	while not booked:

		browser.implicitly_wait(10)
		#wine_list = browser.find_element_by_class_name("weblaunch-list")
		wines = browser.find_elements_by_class_name("weblaunch-item")
		for wine in wines:
			#print("wine checked")
			if "Corton-Charlemagne" in wine.text and "Coche-Dury" in wine.text:
				print(wine.text)
				button = wine.find_element_by_tag_name("button")
				if button.is_enabled():
					print("wine booked")
					button.click()
					booked = True
					break
				else:
					print("not ready, tries again")
					browser.refresh()
					break


#browser.quit()