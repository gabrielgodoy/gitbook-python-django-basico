# Can also be written:
# from urllib import request
# Same as saying import request method from urllib module
import urllib.request  # Fetches data from websites
import random  # random module

# Give me a random number between 1 and 100
x = random.randrange(1, 100)


# print(x) # some random number

# Downloads an image based on url parameter
def downloadImage(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)


downloadImage('http://www.sample-videos.com/csv/Sample-Spreadsheet-10-rows.csv')
