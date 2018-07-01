# web-scrapping
Program to scrap the flowersofindia website for my personal use

############## PROBLEM CONTEXT ################################################

Phase - 1 - I am visiting valley of flowers shortly. i wanted to extract the information of all the flowers seen in that place locally so that i could refer to it as a field guide even when internet is not there. I specifically wanted common name, botanical name, description and the images if possible so that i could identify the flowers using this as a field guide. I want to extract the entire text information into a CSV
Phase - 2 Want to mark the flower colors against each flower too. This would be useful to filter.
############## DESIGN DETAILS ############################################

Used scrapy tool to extract the text and images. To run this program, you need to have scrapy installed.

############## HOW TO RUN ################################################

1. From the spider folder, run scrapy crawl vof -o valley_of_flowers.csv
2. It refers to the settings.py file for images. You can change the directory location if you want the images to be stored somewhere else. The following setting are important
ITEM_PIPELINES = {
  'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_STORE = 'tmp/images/'
