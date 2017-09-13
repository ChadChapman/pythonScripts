#! python3
# downloadTxt will download content from the chosen page to a file on
# the local machine. Then uses Beautiful Soup 4 to parse.

# results and beautiful soup are not in py3 stdlib 
import results

responseObj = requests.get('http://url.to.somewhere/theFile.txt')
# always check this after a requests.get()
#	begin here
try:
	responseObj.raise_for_status()
	
except Exception as excp:
	print('Exception thrown --> %s' % (excp))
#	end here

# still have to write to file in binary as far as I know so far 
# make a new file, write binary to it 
dloadFile = open('DownloadedContentFile.txt', 'wb')
# break writing up into 1-kilobyte chunks
for kb in responseObj.iter_content(1000):
	dloadFile.write(kb)
	
dloadFile.close()
