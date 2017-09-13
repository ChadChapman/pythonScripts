#! python3
#beautiful soup parse 

import requests, bs4

responseObj = requests.get('http://whatever.com')
try:
	responseObj.raise_for_status()
	
except Exception as excp:
	print('Exception thrown --> %s' % (excp))
	
soupText = bs4.BeautifulSoup(responseObj.text)

#or to get from an HTML file on local machine:
# localFile = open('localFileName.html')
# localFileSoup = bs4.BeautifulSoup(localFile)

#can select by elements also, these are just basics, others available
#returns Tag objects
#selectedElement = soup.select('div') 
#also by: #id, .class, 
	#div span - all spans within divs
	#div > span - all spans with div direct parents
	#input[name] - input with given name
	#input[type=button]
	
#access as list: returnList[0].getText()
#look at entire Tag object: str(returnList[0])
#HTML pieces of Tag object as dictionary: returnList.[0].attrs

