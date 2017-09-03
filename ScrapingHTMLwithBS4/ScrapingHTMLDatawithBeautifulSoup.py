
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def extract_tag(url):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	# Retrieve all of the span tags
	tags = soup("span")
	return tags


def main():
	sum = 0
	url = input("please type the url")
	tags = extract_tag(url)
	count = 0
	for tag in tags:
		sum = sum + int(tag.contents[0])
		count = count +1
	print(sum)
	print(count)

if __name__ == "__main__":
	main()




