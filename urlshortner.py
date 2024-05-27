import pyshorteners

url = input("Enter the url which you wish to shorten:")
def shortened_url(url):
    short_url = pyshorteners.Shortener()
    print("Short URL:",short_url.tinyurl.short(url))
    
shortened_url(url)

