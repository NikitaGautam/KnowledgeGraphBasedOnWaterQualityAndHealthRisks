
### WebOfScienceScrapper:
- Download chrome webdriver from the following link: https://chromedriver.chromium.org/downloads
- Path of this chrome driver should be provided as in input while running scrapper.py

## Use Scrapper.py to scrape urls from WebOfScience and NationalLilbraryOfMedicine with specific keywords.

python scrapper.py driverpath=PathToChromeDriver


## Combine the extracted abstracts using combine_data.py
python combine_data.py rootdir=SourceDirectory outdir=DestinationDirectory

## Convert PDF to text files using converter.py