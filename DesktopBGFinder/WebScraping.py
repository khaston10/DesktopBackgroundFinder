import requests
import bs4
import random
from os.path import basename

wordBank = ["balloon", "dog", "wing", "paraglider"]


def select_random_word():

    rand_int = random.randint(0, len(wordBank)-1)
    print('Key Word: ' + wordBank[rand_int])
    return wordBank[rand_int]


# Step 1: Build a function to open Google Images and Imgur Images based on a word
random_word = select_random_word()
query_path = 'https://imgur.com/search?q=' + random_word
results = requests.get(query_path, 'html.parser')


# Print information about results, this should print all the HTML code.
print('The HTML code is: ' + str(len(results.text)) + ' lines long. I think?')
#print(results.text)

# Step 2: Create a Beautiful Soup object and print to screen the information on the images
soup_object = bs4.BeautifulSoup(results.text, features="html.parser")
images = soup_object.select('img')
print('There are: ' + str(len(images)) + ' images on this page.')

# Step 3: Download the images to a file.
for img in images:

