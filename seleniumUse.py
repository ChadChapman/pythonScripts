#! python3
# selenium use cases and examples

from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://website/url/goes/here')

#find an element by class name
try:
	classNameElement = browser.find_element_by_class_name('className')
	#prints 
	print('Found element with that class name, of <%s> tag type.' 
	% (classNameElement.tag_name))
	
except:
	 
	print('No element found with that class name.')
	
#click a link
try:
	linkedElement = browser.find_element_by_link_text('linkTextHere')
	print('link found, about to click')
	#now follow the link
	linkedElement.click() 

except:
	print('link with that text was not found')
	
#fill and submit a form (gmail)
try:
	usernameElement = browser.find_element_by_id('login-username')
	usernameElement.send_keys('usernameString')
	passwordElement = browser.find_element_by_id('login-passwd')
	passwordElement.send_keys('passwordString')
	passwordElement.submit()

except:
	print('form not filled and submitted')
	
#keys unable to be in string are similar to: Keys.ENTER, Keys.DELETE,
#	Keys.TAB, Keys.F1, Keys.BACK_SPACE, Keys.DOWN, etc	
#example
htmlElement = browser.find_element_by_tag_name('html')
# go to bottom
htmlElement.send_keys(Keys.END)
# go to top
htmlElement.send_keys(Keys.HOME)

#browser button clicks
browser.back()
browser.forward()
browser.refresh()
browser.quit()




	
