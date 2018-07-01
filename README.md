# web-scrapping
Program to scrap website for my personal use. 

############## PROBLEM CONTEXT ################################################

Phase - 1 - I am visiting valley of flowers shortly. i wanted to extract the information of all the flowers seen in that place locally so that i could refer to it as a field guide even when internet is not there. I specifically wanted common name, botanical name, description and the images if possible so that i could identify the flowers using this as a field guide. I want to extract the entire text information into a CSV
Phase - 2 Want to mark the flower colors against each flower too. This would be useful to filter.

############## TOOL DETAILS ############################################

Used scrapy tool to extract the text and images. To run this program, you need to have scrapy installed.

############## HOW TO RUN ################################################

1. From the spider folder, run scrapy crawl vof -o valley_of_flowers.csv
2. It refers to the settings.py file for images. You can change the directory location if you want the images to be stored somewhere else. The following setting are important
ITEM_PIPELINES = {
  'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_STORE = 'tmp/images/'

############## REFERENCE ################################################
The following sites helped me learn web scrapping using scrapy well. A big shoutout of thanks to the ones responsible for these websites
https://codereview.stackexchange.com/questions/172174/scrapy-crawler-to-parse-data-recursively
https://www.pyimagesearch.com/2015/10/12/scraping-images-with-python-and-scrapy/
https://www.analyticsvidhya.com/blog/2017/07/web-scraping-in-python-using-scrapy/
https://doc.scrapy.org/en/latest/index.html
https://doc.scrapy.org/en/latest/topics/media-pipeline.html
https://www.digitalocean.com/community/tutorials/how-to-crawl-a-web-page-with-scrapy-and-python-3#step-3-%E2%80%94-crawling-multiple-pages
